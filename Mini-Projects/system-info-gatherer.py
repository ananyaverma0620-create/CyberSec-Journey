import platform
import socket
import getpass
import psutil


print(f" System Info Gatherer ")

# 1. OS Information
print("1. OS Information:")
print("System:", platform.system())
print("Version:", platform.version())
print()

# 2. Current User
print("2. Current User:")
print(getpass.getuser())
print()

# 3. IP Address
print("3. IP Address:")
try:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(ip)
except:
    print("Could not get IP")
print()

# 4. Running Processes Count
print("4. Running Processes:")
try:
    print(len(psutil.pids()))
except:
    print("Error getting process count")
print()

# 5. Disk Usage
print("5. Disk Usage:")
try:
    disk = psutil.disk_usage('/')
    print("Total:", disk.total // (1024**3), "GB")
    print("Used:", disk.used // (1024**3), "GB")
    print("Free:", disk.free // (1024**3), "GB")
except:
    print("Error getting disk info")
print()

# 6. Network Interfaces
print("6. Network Interfaces:")
try:
    interfaces = psutil.net_if_addrs()
    for name, addresses in interfaces.items():
        print("Interface:", name)
        for addr in addresses:
            if addr.family == socket.AF_INET:
                print("IP:", addr.address)
except:
    print("Error getting network info")
