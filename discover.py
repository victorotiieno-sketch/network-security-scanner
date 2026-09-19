import subprocess

network = "10.0.2.0/24"

print("=" * 55)
print("          NETWORK HOST DISCOVERY")
print("=" * 55)
print(f"\nScanning network: {network}\n")

command = ["sudo", "nmap", "-sn", network]

try:
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)

except Exception as error:
    print(f"Error: {error}")
