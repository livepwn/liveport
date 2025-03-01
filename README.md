# Live Port
## Port Scanner
### A Python-based port scanner. This tool captures and analyzes ports that which ports are open.It provides an interactive command-line interface (CLI) for users to select range from x port to some x port. and analyze port in real-time.

## Features
 ### Interactive Input:

- Users can input the target IP address and port range.

- The scanner will ask if the user wants to scan another target after completing a scan.

### Port Scanning:

- Scans a range of ports on the target IP address.

- Detects open ports and displays them.

### Vulnerability Detection:

- Checks for common vulnerabilities on open ports (e.g., default SSH credentials, outdated web servers).

### User-Friendly:

- Provides clear output and prompts for user interaction.

## Installation
### Prerequisites
- Python 3.x


## Steps
- Clone the repository:

```
git clone https://github.com/livepwn/liveport.git

cd liveport
```
- Run the script:


```
chmod +x liveport.py
or
sudo python liveport.py


```

## Usage
Running the Analyzer
Start the script:
```
sudo python liveport.py
```
Follow the on-screen prompts:
```
=== IoT Vulnerability Scanner ===
Enter the target IP address: 192.168.1.100
Enter the starting port (e.g., 1): 1
Enter the ending port (e.g., 1024): 1024
[*] Scanning 192.168.1.100 from port 1 to 1024...
[+] Port 22 is open
[+] Port 80 is open

[+] Open ports found:
Port 22 is open
[*] Checking vulnerabilities on 192.168.1.100:22...
[!] Potential vulnerability: Default SSH credentials
Port 80 is open
[*] Checking vulnerabilities on 192.168.1.100:80...
[!] Potential vulnerability: Outdated web server

Scan complete!

Do you want to scan another target? (y/n): n
[*] Exiting...

```
## Advantages
### **Ease of Use:**
  - The interactive CLI makes it easy for users to 

### **Real-Time Analysis:**

- Scan for ports in real-time, providing immediate insights into network traffic.


### **Lightweight:**

- Built with Python , the tool is lightweight and does not require heavy dependencies.



## Future Enhancements

- Add more vulnerability checks (e.g., for FTP, Telnet, or custom services).

- Integrate with databases like CVE (Common Vulnerabilities and Exposures) for detailed vulnerability information.

- Add multithreading to speed up port scanning.



## Contact
- For questions or feedback, please open an issue on GitHub or contact:

Your Name: livepwn@gmail.com

GitHub: [livepwn](https://github.com/livepwn)