import socket

ip_or_domain = input("Enter IP or domain: ")
ports = input("Port(s) separated by comma (e.g.: 21,22,23): ")

portsList = []

if ',' in ports:
    portsList = ports.split(",")
else:
    portsList = ports

for i in range(len(portsList)):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    
    code = client.connect_ex((ip_or_domain, int(portsList[i])))
    
    if code == 0:
        print(f"[*] - {portsList[i]}  OPEN")
    # else:
        # print(f"[*] - {portsList[i]} CLOSED")

