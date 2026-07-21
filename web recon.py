"""
╔══════════════════════════════════════╗
║   D2S — Developer 2 Security        ║
║   Web Reconnaissance Tool v1.0      ║
║   Educational purposes only         ║
╚══════════════════════════════════════╝

⚠️  WARNING: Only use on systems you own
    or have explicit permission to test.
    Unauthorized scanning is illegal.
"""

import requests
from bs4 import BeautifulSoup
import socket
import sys
import re
from datetime import datetime
from urllib.parse import urljoin, urlparse

class Color:
    RED    = '\033[91m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    BLUE   = '\033[94m'
    PURPLE = '\033[95m'
    CYAN   = '\033[96m'
    WHITE  = '\033[97m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'

def red(text):    return f"{Color.RED}{text}{Color.RESET}"
def green(text):  return f"{Color.GREEN}{text}{Color.RESET}"
def yellow(text): return f"{Color.YELLOW}{text}{Color.RESET}"
def blue(text):   return f"{Color.BLUE}{text}{Color.RESET}"
def cyan(text):   return f"{Color.CYAN}{text}{Color.RESET}"
def bold(text):   return f"{Color.BOLD}{text}{Color.RESET}"

def banner():
    print(cyan("""
╔══════════════════════════════════════════╗
║                                          ║
║   ██████╗ ██████╗ ███████╗              ║
║   ██╔══██╗╚════██╗██╔════╝              ║
║   ██║  ██║ █████╔╝███████╗              ║
║   ██║  ██║██╔═══╝ ╚════██║              ║
║   ██████╔╝███████╗███████║              ║
║   ╚═════╝ ╚══════╝╚══════╝              ║
║                                          ║
║   Web Reconnaissance Tool v1.0           ║
║   Developer 2 Security                   ║
║   Pulau Pinang, Malaysia 🇲🇾             ║
║                                          ║
╚══════════════════════════════════════════╝
"""))
    print(yellow("  ⚠️  For authorized testing only!\n"))

def dns_lookup(target):
    print(bold(cyan("\n[MODULE 1] DNS & IP Lookup")))
    print("─" * 45)

    try:
    
        clean = target.replace('https://', '').replace('http://', '').split('/')[0]

        ip = socket.gethostbyname(clean)
        print(green(f"  ✅ Hostname : {clean}"))
        print(green(f"  ✅ IP Address: {ip}"))

        # Reverse DNS
        try:
            reverse = socket.gethostbyaddr(ip)
            print(green(f"  ✅ Reverse DNS: {reverse[0]}"))
        except:
            print(yellow("  ⚠️  Reverse DNS: Not available"))

        return ip

    except socket.gaierror as e:
        print(red(f"  ❌ DNS Lookup failed: {e}"))
        return None


def check_headers(url):
    print(bold(cyan("\n[MODULE 2] HTTP Headers Analysis")))
    print("─" * 45)

    # Security headers yang patut ada
    security_headers = {
        'Strict-Transport-Security': 'HSTS — Force HTTPS',
        'X-Frame-Options': 'Clickjacking protection',
        'X-XSS-Protection': 'XSS filter (legacy)',
        'X-Content-Type-Options': 'MIME sniffing protection',
        'Content-Security-Policy': 'CSP — XSS/injection protection',
        'Referrer-Policy': 'Referrer info control',
        'Permissions-Policy': 'Browser features control',
    }

    info_headers = {
        'Server': 'Server software version',
        'X-Powered-By': 'Backend technology',
        'X-AspNet-Version': 'ASP.NET version',
        'X-AspNetMvc-Version': 'MVC version',
    }

    try:
        response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; D2S-Recon/1.0)'},
            timeout=10,
            allow_redirects=True
        )

        print(f"  Status Code: {green(str(response.status_code))}")
        print(f"  Final URL  : {response.url}")

    
        print(yellow("\n  [Security Headers]"))
        for header, description in security_headers.items():
            if header in response.headers:
                print(green(f"  ✅ {header}"))
                print(f"     └─ {response.headers[header][:60]}")
            else:
                print(red(f"  ❌ MISSING: {header}"))
                print(f"     └─ {description}")

        
        print(yellow("\n  [Information Disclosure]"))
        for header, description in info_headers.items():
            if header in response.headers:
                print(red(f"  ⚠️  {header}: {response.headers[header]}"))
                print(f"     └─ Risk: Version info exposed to attacker!")
            else:
                print(green(f"  ✅ {header}: Not exposed"))

        return response

    except requests.exceptions.ConnectionError:
        print(red(f"  ❌ Cannot connect to {url}"))
        return None
    except requests.exceptions.Timeout:
        print(red(f"  ❌ Connection timeout"))
        return None

def analyze_forms(response, url):
    print(bold(cyan("\n[MODULE 3] Form & Input Analysis")))
    print("─" * 45)

    if not response:
        print(red("  ❌ No response to analyze"))
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')

    print(f"  Forms found: {len(forms)}")

    for i, form in enumerate(forms, 1):
        print(yellow(f"\n  [Form {i}]"))
        print(f"  Action : {form.get('action', 'N/A')}")
        print(f"  Method : {form.get('method', 'GET').upper()}")
        
        inputs = form.find_all('input')
        print(f"  Inputs : {len(inputs)}")

        for inp in inputs:
            inp_type = inp.get('type', 'text')
            inp_name = inp.get('name', 'unnamed')
            print(f"    └─ [{inp_type}] name='{inp_name}'")

        # Check CSRF token
        csrf_patterns = ['csrf', 'token', '_token', 'authenticity_token']
        has_csrf = False

        for pattern in csrf_patterns:
            csrf = form.find('input', {
                'name': re.compile(pattern, re.I)
            })
            if csrf:
                has_csrf = True
                print(green(f"  ✅ CSRF Token: Found ({csrf.get('name')})"))
                break

        if not has_csrf:
            print(red("  ❌ CSRF Token: MISSING — Potential CSRF vulnerability!"))

        # Check method
        if form.get('method', 'GET').upper() == 'GET':
            print(yellow("  ⚠️  GET method — sensitive data may appear in URL"))


def check_sensitive_files(base_url):
    print(bold(cyan("\n[MODULE 4] Sensitive Files & Directories")))
    print("─" * 45)

    sensitive_paths = [
        '/config.php',
        '/.env',
        '/config.yml',
        '/config.json',
        '/settings.py',

        
        '/admin',
        '/admin.php',
        '/administrator',
        '/wp-admin',
        '/phpmyadmin',
        '/cpanel',

    
        '/backup.zip',
        '/backup.sql',
        '/backup.tar.gz',
        '/db.sql',
        '/database.sql',
        '/robots.txt',
        '/sitemap.xml',
        '/.git',
        '/.git/config',
        '/server-status',
        '/info.php',
        '/phpinfo.php',

        
        '/upload',
        '/uploads',
        '/files',
        '/shell.php',
    ]

    found = []
    not_found = []

    for path in sensitive_paths:
        url = base_url.rstrip('/') + path
        try:
            r = requests.get(
                url,
                timeout=5,
                allow_redirects=False,
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            if r.status_code == 200:
                print(red(f"  🚨 FOUND [{r.status_code}]: {path}"))
                found.append(path)
            elif r.status_code == 403:
                print(yellow(f"  ⚠️  FORBIDDEN [{r.status_code}]: {path} (exists but blocked)"))
                found.append(path)
            else:
                print(green(f"  ✅ [{r.status_code}]: {path}"))

        except:
            pass

    print(f"\n  Summary: {len(found)} sensitive paths found!")
    return found


def fingerprint_tech(response):
    print(bold(cyan("\n[MODULE 5] Technology Fingerprinting")))
    print("─" * 45)

    if not response:
        print(red("  ❌ No response to analyze"))
        return

    tech_found = []


    header_signatures = {
        'X-Powered-By': {
            'PHP': 'PHP',
            'ASP.NET': 'ASP.NET',
            'Express': 'Node.js/Express',
        },
        'Server': {
            'Apache': 'Apache Web Server',
            'nginx': 'Nginx Web Server',
            'IIS': 'Microsoft IIS',
            'LiteSpeed': 'LiteSpeed Server',
        }
    }

    for header, signatures in header_signatures.items():
        if header in response.headers:
            value = response.headers[header]
            for sig, name in signatures.items():
                if sig.lower() in value.lower():
                    print(yellow(f"  ⚠️  Detected: {name}"))
                    print(f"     └─ Header: {header}: {value}")
                    tech_found.append(name)

    
    content_signatures = {
        'WordPress': ['wp-content', 'wp-includes', 'wordpress'],
        'Laravel': ['laravel_session', 'Laravel'],
        'jQuery': ['jquery.min.js', 'jquery.js'],
        'Bootstrap': ['bootstrap.min.css', 'bootstrap.js'],
        'React': ['react.js', 'react.min.js', '__REACT'],
        'Vue.js': ['vue.js', 'vue.min.js'],
        'PHP': ['<?php', '.php'],
        'XAMPP': ['xampp', 'XAMPP'],
    }

    content = response.text.lower()

    print(yellow("\n  [Content Analysis]"))
    for tech, signatures in content_signatures.items():
        for sig in signatures:
            if sig.lower() in content:
                print(cyan(f"  🔍 Found: {tech}"))
                tech_found.append(tech)
                break

    
    if response.cookies:
        print(yellow("\n  [Cookies]"))
        for cookie in response.cookies:
            secure = "✅ Secure" if cookie.secure else "❌ NOT Secure"
            httponly = "✅ HttpOnly" if cookie.has_nonstandard_attr('HttpOnly') else "⚠️  No HttpOnly"
            print(f"  Cookie: {cookie.name}")
            print(f"    └─ {secure} | {httponly}")

    return tech_found


def check_robots(base_url):
    print(bold(cyan("\n[MODULE 6] Robots.txt Analysis")))
    print("─" * 45)

    robots_url = base_url.rstrip('/') + '/robots.txt'

    try:
        r = requests.get(robots_url, timeout=5)

        if r.status_code == 200:
            print(green(f"  ✅ robots.txt found!\n"))
            print(f"  Content:")
            print("  " + "─" * 30)

            disallowed = []
            for line in r.text.split('\n'):
                line = line.strip()
                if line:
                    print(f"  {line}")
                    if line.lower().startswith('disallow:'):
                        path = line.split(':', 1)[1].strip()
                        if path and path != '/':
                            disallowed.append(path)

            if disallowed:
                print(yellow(f"\n  ⚠️  Interesting disallowed paths:"))
                for path in disallowed:
                    print(yellow(f"     → {path} (hidden from Google — worth checking!)"))
        else:
            print(yellow(f"  ⚠️  robots.txt not found (404)"))

    except Exception as e:
        print(red(f"  ❌ Error: {e}"))

def generate_report(target, results):
    print(bold(cyan("\n[REPORT] D2S Recon Summary")))
    print("═" * 45)
    print(f"  Target  : {target}")
    print(f"  Date    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Tool    : D2S Web Recon v1.0")
    print("═" * 45)

    print(yellow("\n  ⚠️  FINDINGS:"))
    if results:
        for finding in results:
            print(f"  → {finding}")
    else:
        print(green("  ✅ No critical issues found"))

    print("\n" + cyan("═" * 45))
    print(cyan("  D2S — Developer 2 Security"))
    print(cyan("  📍 Pulau Pinang, Malaysia"))
    print(cyan("═" * 45) + "\n")


def main():
    banner()

    
    target = input("  Enter target URL: ").strip()

    if not target:
        print(red("  ❌ No target provided!"))
        sys.exit()

    
    if not target.startswith('http'):
        target = 'http://' + target

    print(f"\n  {bold('Starting recon on:')} {cyan(target)}")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    findings = []

    
    ip = dns_lookup(target)

    response = check_headers(target)

    if response:
        analyze_forms(response, target)
        fingerprint_tech(response)

    sensitive = check_sensitive_files(target)
    if sensitive:
        for path in sensitive:
            findings.append(f"Sensitive file found: {path}")

    check_robots(target)
    generate_report(target, findings)

if __name__ == "__main__":
    main()