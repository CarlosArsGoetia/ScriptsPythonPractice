import socket
import  sys , signal
#Scan your own computer ports

def def_handler(sig,frame):
    print("\n\n[***] Running out...[***]\n")
    sys.exit(1)

#Ctrl+C for exit
signal.signal(signal.SIGINT, def_handler)

def check_ports(ip):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

open_ports = check_ports('127.0.0.1')
print("List of Open :", open_ports)
