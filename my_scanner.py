import subprocess
print("Network Scanner is starting...")
result = subprocess.run(["arp", "-a"], capture_output=True, text=True)

print("ARP table found")
lines = result.stdout.splitlines()
for line in lines:
    parts = line.split()
    ip = parts[1]
    ip = ip.strip("()")
    print(ip)