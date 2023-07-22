import socket

ip_or_domain = [""]  # insert ip or domain here
ports = []  # insert port(s)

services = len(ip_or_domain)
for j in range(services):
    print(f"[*] Scanning {ip_or_domain[j]}")
    for i in range(len(ports)):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)

        code = client.connect_ex((ip_or_domain[j], int(ports[i])))

        if code == 0:
            print(f"[*] - {ports[i]}  OPEN")
        else:
            print(f"[-] - {ports[i]} CLOSED")
        
        if i == len(ports) - 1:
            print("\n")
