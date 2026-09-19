# Network Security Scanner

A Python-based network security scanning project built with Kali Linux and Nmap. The project discovers active devices on an authorized network and performs service and port detection against selected hosts.

## Features

* Discover active hosts on a network
* Detect open TCP ports
* Identify running services
* Perform service and version detection
* Save scan results to report files
* Maintain separate discovery and scanning tools
* Designed for authorized security testing and lab environments

## Technologies

* Python 3
* Nmap
* Kali Linux
* Linux command line

## Project Structure

```text
network-security-scanner/
├── scanner.py
├── scanner_backup.py
├── discover.py
├── discover_backup.py
├── reports/
└── scan-results.txt
```

## Host Discovery

The discovery tool uses Nmap host discovery to identify active devices on the lab network.

```bash
python3 discover.py
```

Current lab network:

```text
10.0.2.0/24
```

Example discovered hosts:

```text
10.0.2.2
10.0.2.3
10.0.2.15
```

## Service Scanning

The scanner accepts a target IP address and performs Nmap service/version detection.

```bash
python3 scanner.py
```

Example target:

```text
10.0.2.2
```

The scanner saves the results inside the `reports/` directory.

## Example Results

A test scan identified the following open TCP ports on the lab host `10.0.2.2`:

| Port | State | Service        |
| ---- | ----- | -------------- |
| 135  | Open  | MSRPC          |
| 445  | Open  | Microsoft-DS   |
| 5357 | Open  | HTTP           |
| 7070 | Open  | SSL/RealServer |

Nmap also identified the host as a Windows system.

## Learning Objectives

This project demonstrates practical experience with:

* Network reconnaissance
* Host discovery
* Port scanning
* Service identification
* Nmap automation
* Python subprocess execution
* Security report generation
* Linux command-line operations

## Security Notice

This project is intended for authorized security testing, personal laboratories, and systems for which permission has been granted.

Do not scan networks or systems without authorization.

## Future Improvements

Planned improvements include:

* Automated host selection
* Security risk classification
* Improved report formatting
* CSV and JSON report generation
* Configurable network ranges
* Additional Nmap scanning options
* Vulnerability assessment capabilities

## Author

Victor Otieno

ICT Professional | Networking | Web Development | Cybersecurity | Technical Support
