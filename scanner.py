import subprocess
from datetime import datetime
from pathlib import Path

print("=" * 50)
print("       NETWORK SECURITY SCANNER")
print("=" * 50)

target = input("Enter target IP address: ").strip()

if not target:
    print("Error: IP address cannot be empty.")
    exit()

reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = reports_dir / f"scan_{timestamp}.txt"

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
    
    report_file.write_text(result.stdout + "\n\n" + "=" * 50 + "\n          SECURITY RISK ANALYSIS\n" + "=" * 50 + "\n" + ("\n".join(findings) if findings else "No monitored ports requiring risk classification were detected."))
    
    print("\nScan complete.")
    print(f"Report saved to: {report_file}")

except FileNotFoundError:
    print("Error: Nmap is not installed or cannot be found.")
except Exception as error:
    print(f"Error: {error}")
