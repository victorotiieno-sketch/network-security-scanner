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

try:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)
    
    report_file.write_text(result.stdout)
    
    print("\nScan complete.")
    print(f"Report saved to: {report_file}")

except FileNotFoundError:
    print("Error: Nmap is not installed or cannot be found.")
except Exception as error:
    print(f"Error: {error}")
