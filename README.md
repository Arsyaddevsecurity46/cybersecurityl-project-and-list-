# ⚡ D2S — Cybersecurity Projects & Tools

```
██████╗ ██████╗ ███████╗
██╔══██╗╚════██╗██╔════╝
██║  ██║ █████╔╝███████╗
██║  ██║██╔═══╝ ╚════██║
██████╔╝███████╗███████║
╚═════╝ ╚══════╝╚══════╝
Developer 2 Security
```

> *"We don't just build. We secure."*
> 
> — D2S, Pulau Pinang 🇲🇾

---

## 👤 About This Repo

This repository contains **hands-on cybersecurity tools and projects** built by D2S as part of an active learning journey into **ethical hacking**, **penetration testing**, and **web security**.

Every project here is built from scratch And These projects are built as part of my cybersecurity learning journey. AI is used as a learning assistant, while I study, modify, and understand the code before publishing it.— to understand the *why*, not just the *what*.

---

## ⚠️ Disclaimer

```
All tools in this repository are for:
✅ Educational purposes only
✅ Authorized testing environments
✅ CTF challenges
✅ Systems you own or have explicit permission to test

❌ NEVER use on systems without permission
❌ Unauthorized use is illegal under
   Computer Crimes Act 1997 (Malaysia)
```

---

## 🛠️ Tools & Projects

### 01 — Port Scanner
`Python` `Networking` `Recon`

```
Scan open ports pada target host.
Identify running services dan potential attack surface.
```

**Features:**
- Scan port range 1–1000
- Detect open ports dengan real-time output
- Show scan timestamp
- Keyboard interrupt handling

**Usage:**
```bash
python3 port_scanner.py
# Masukkan target IP/hostname bila prompted
# Contoh: localhost atau 192.168.1.1
```

**Sample Output:**
```
==================================================
Scanning target: localhost
Time: 2026-07-18 22:00:00
==================================================

[OPEN] Port 80
[OPEN] Port 443
[OPEN] Port 3306

Total open ports: 3
```

---

### 02 — Recon Tool — automated web reconnaissance
`Python` `Web Security`

```
Analyze a target web application for common security misconfigurations.
```
**Features:**
- DNS LOOKUP AND IP LOOKUP
- HTTP headers analysis 
- form and input analysis
- senstive files check
- technology fingerprinting or footprtinting
- robots,txt analysis
- report generation 

**Sample Output:**
```
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

  ⚠️  For authorized testing only!

  Enter target URL: localhost/sistem-kehadiran/login.php 

  Starting recon on: http://localhost/sistem-kehadiran/login.php
  2026-07-21 23:17:27


[MODULE 1] DNS & IP Lookup
─────────────────────────────────────────────
  ✅ Hostname : localhost
  ✅ IP Address: 127.0.0.1
  ✅ Reverse DNS: LAPTOP-73JMDB26

[MODULE 2] HTTP Headers Analysis
─────────────────────────────────────────────
  Status Code: 404
  Final URL  : http://localhost/sistem-kehadiran/login.php

  [Security Headers]
  ❌ MISSING: Strict-Transport-Security
     └─ HSTS — Force HTTPS
  ❌ MISSING: X-Frame-Options
     └─ Clickjacking protection
  ❌ MISSING: X-XSS-Protection
     └─ XSS filter (legacy)
  ❌ MISSING: X-Content-Type-Options
     └─ MIME sniffing protection
  ❌ MISSING: Content-Security-Policy
     └─ CSP — XSS/injection protection
  ❌ MISSING: Referrer-Policy
     └─ Referrer info control
  ❌ MISSING: Permissions-Policy
     └─ Browser features control

  [Information Disclosure]
  ⚠️  Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3 PHP/8.1.25
     └─ Risk: Version info exposed to attacker!
  ✅ X-Powered-By: Not exposed
  ✅ X-AspNet-Version: Not exposed
  ✅ X-AspNetMvc-Version: Not exposed

[MODULE 4] Sensitive Files & Directories
─────────────────────────────────────────────
  ✅ [404]: /config.php
  ✅ [404]: /.env
  ✅ [404]: /config.yml
  ✅ [404]: /config.json
  ✅ [404]: /settings.py
  ✅ [404]: /admin
  ✅ [404]: /admin.php
  ✅ [404]: /administrator
  ✅ [404]: /wp-admin
  ✅ [404]: /phpmyadmin
  ✅ [404]: /cpanel
  ✅ [404]: /backup.zip
  ✅ [404]: /backup.sql
  ✅ [404]: /backup.tar.gz
  ✅ [404]: /db.sql
  ✅ [404]: /database.sql
  ✅ [404]: /robots.txt
  ✅ [404]: /sitemap.xml
  ✅ [404]: /.git
  ✅ [404]: /.git/config
  ✅ [404]: /server-status
  ✅ [404]: /info.php
  ✅ [404]: /phpinfo.php
  ✅ [404]: /upload
  ✅ [404]: /uploads
  ✅ [404]: /files
  ✅ [404]: /shell.php

  Summary: 0 sensitive paths found!

[MODULE 6] Robots.txt Analysis
─────────────────────────────────────────────
  ⚠️  robots.txt not found (404)

[REPORT] D2S Recon Summary
═════════════════════════════════════════════
  Target  : http://localhost/sistem-kehadiran/login.php
  Date    : 2026-07-21 23:17:28
  Tool    : D2S Web Recon v1.0
═════════════════════════════════════════════

  ⚠️  FINDINGS:
  ✅ No critical issues found

═════════════════════════════════════════════
  D2S — Developer 2 Security
  📍 Pulau Pinang, Malaysia
═════════════════════════════════════════════

```


### 03 — Coming Soon 🚧
`Python` `Cryptography`

```
Hash Identifier & Cracker
```

---

### 04 — Coming Soon 🚧
`Python` `Web Security`

```
XSS Payload Generator
```

---

### 05 — Coming Soon 🚧
`Python` `Web Security`

```
SQL Injection Tester
```

---

## 🗺️ Roadmap

```
Phase 1 — Foundation Tools (Current)
├── ✅ Port Scanner
├── 🚧 Recon Tool
└── 🚧 Hash Cracker

Phase 2 — Web Attack Tools
├── 🔒 XSS Generator
├── 🔒 SQLi Tester
└── 🔒 CSRF PoC Generator

Phase 3 — D2S Security Toolkit
└── 🔒 All tools bundled into one CLI toolkit
```

---

## 📚 What I'm Learning

```
✅ Python for Security Automation
✅ Network Scanning & Recon
✅ OWASP Top 10
✅ Web Application Pentesting
✅ Linux Security & Permissions
✅ Cryptography Fundamentals

🔄 Currently:
   → PortSwigger Web Security Academy
   → TryHackMe Jr Pentester Path
   → DVWA Practice Lab
   → HackerOne Bug Bounty (coming soon)
```

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Kali](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)

---

## 🔐 Security Philosophy

```
┌─────────────────────────────────────┐
│                                     │
│   "Security is not a product,       │
│    it's a process."                 │
│                                     │
│   Every line of code I write        │
│   is written with security          │
│   in mind — from day one.           │
│                                     │
└─────────────────────────────────────┘
```

---

## 📂 Other Projects

| Project | Description | Tech | Link |
|---------|-------------|------|------|
| F2A Attendance System | Face Recognition Attendance | PHP, MySQL | [View](https://github.com/Arsyaddevsecurity46/face-attendance-system-) |
| Restaurant Website | Frontend Demo | HTML, CSS, JS | [View](https://github.com/Arsyaddevsecurity46/demo-website-for-restaurant-design-) |

---

## 📬 Contact

```
👤 D2S — Developer 2 Security
📍 Pulau Pinang, Malaysia
🌐 github.com/Arsyaddevsecurity46
📘 Facebook: D2S — Developer 2 Security
📩 Available for freelance & consultation
```

---

<div align="center">

```
┌──────────────────────────────────┐
│   Built with curiosity,          │
│   driven by passion,             │
│   secured by knowledge. 🔐       │
└──────────────────────────────────┘
```

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=Arsyaddevsecurity46.cybersecurity)

*© 2026 D2S — Developer 2 Security | Pulau Pinang, Malaysia*

</div>
