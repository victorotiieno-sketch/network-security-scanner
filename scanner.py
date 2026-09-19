import subprocess
import csv
import json
from datetime import datetime
from pathlib import Path

print("=" * 50)
print("       NETWORK SECURITY SCANNER")
print("Network: 10.0.2.0/24")

network = "10.0.2.0/24"
print("=" * 50)



print("\nDiscovering active hosts...")
discovery = subprocess.run(
    ["nmap", "-sn", network],
    capture_output=True,
    text=True
)

hosts = []

for line in discovery.stdout.splitlines():
    if "Nmap scan report for" in line:
        host = line.split()[-1]
        hosts.append(host)

print("\nActive hosts found:")

for number, host in enumerate(hosts, 1):
    print(f"{number}. {host}")

if not hosts:
    print("No active hosts found.")
    exit()

choice = input("\nSelect a host number to scan: ").strip()

if not choice.isdigit() or not 1 <= int(choice) <= len(hosts):
    print("Invalid selection.")
    exit()

target = hosts[int(choice) - 1]

if not target:
    print("Error: IP address cannot be empty.")
    exit()

reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = reports_dir / f"scan_{timestamp}.txt"
json_report = reports_dir / f"scan_{timestamp}.json"
csv_report = reports_dir / f"scan_{timestamp}.csv"

print(f"\nScanning target: {target}")
print("Please wait...\n")

command = ["nmap", "-sV", target]

risk_ports = {21: ("FTP", "Medium"), 23: ("Telnet", "High"), 25: ("SMTP", "Medium"), 139: ("NetBIOS", "High"), 445: ("SMB", "High"), 3389: ("RDP", "High"), 5900: ("VNC", "High")}

try:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print("\n" + "=" * 50)
    print("          SECURITY RISK ANALYSIS")
    print("=" * 50)

    findings = []

    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 3 and "/tcp" in parts[0] and parts[1] == "open":
            port = parts[0].split("/")[0]
            if port.isdigit() and int(port) in risk_ports:
                service, risk = risk_ports[int(port)]
                finding = f"Port {port} ({service}) - Risk: {risk}"
                findings.append(finding)
                print(finding)

    if not findings:
        print("No monitored ports requiring risk classification were detected.")

    report_data = {"target": target, "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "findings": findings}
    
    report_file.write_text(result.stdout + "\n\n" + "=" * 50 + "\n          SECURITY RISK ANALYSIS\n" + "=" * 50 + "\n" + ("\n".join(findings) if findings else "No monitored ports requiring risk classification were detected."))
    
    with csv_report.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["target", "scan_time", "finding"])
        writer.writeheader()
        for finding in findings:
            writer.writerow({"target": target, "scan_time": report_data["scan_time"], "finding": finding})
    json_report.write_text(json.dumps(report_data, indent=4))
    print("\nScan complete.")
    print(f"Report saved to: {report_file}")

except FileNotFoundError:
    print("Error: Nmap is not installed or cannot be found.")
except Exception as error:
    print(f"Error: {error}")
