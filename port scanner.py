# port_scanner.py
import socket
import sys
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"Scanning target: {target}")
    print(f"Time: {datetime.now()}")
    print(f"{'='*50}\n")
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname tidak boleh resolve!")
        sys.exit()
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(
                socket.AF_INET, 
                socket.SOCK_STREAM
            )
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)
            sock.close()
            
        except KeyboardInterrupt:
            print("\nScan dihentikan.")
            sys.exit()
    
    print(f"\nTotal open ports: {len(open_ports)}")
    return open_ports


if __name__ == "__main__":
    target = input("Masukkan target IP/hostname: ")
    scan_ports(target, 1, 1000)