import socket
import time

def scan_ports(target):
    print(f"Scanning target:{target}")
    print("Scanning ports ")
    start_time = time.time()
    open_ports = []
    try:
        # Resolve hostname to IP
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Invalid hostname")
        return
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)

            sock.close()

    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        return
    except socket.error:
        print("Socket error occurred.")
        return

    end_time = time.time()
    print("Scan completed.")
    print(f"Open ports: {open_ports}")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")


if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    scan_ports(target)
