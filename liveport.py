# vulnerability_scanner.py
import socket
import sys

def scan_ports(ip, start_port, end_port):
    open_ports = []
    print(f"[*] Scanning {ip} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is open")
        sock.close()
    return open_ports

def check_vulnerabilities(ip, port):
    # Placeholder for vulnerability checks
    print(f"[*] Checking vulnerabilities on {ip}:{port}...")
    if port == 22:  # Example: SSH port
        print("[!] Potential vulnerability: Default SSH credentials")
    elif port == 80:  # Example: HTTP port
        print("[!] Potential vulnerability: Outdated web server")
    else:
        print("[-] No known vulnerabilities detected")

def interactive_menu():
    print("=== IoT Vulnerability Scanner ===")
    ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 1024): "))

    open_ports = scan_ports(ip, start_port, end_port)

    if open_ports:
        print("\n[+] Open ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
            check_vulnerabilities(ip, port)
    else:
        print("[-] No open ports found.")

    print("\nScan complete!")

if __name__ == "__main__":
    try:
        while True:
            interactive_menu()
            again = input("\nDo you want to scan another target? (y/n): ").lower()
            if again != 'y':
                print("[*] Exiting...")
                break
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        sys.exit(0)
