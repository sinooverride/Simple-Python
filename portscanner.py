import socket
import subprocess
import sys

def scan_host(startport, endport, serverIP):
    i = 0
    for port in range(startport,endport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        output = s.connect_ex((serverIP, port))
        if output == 0:
            print ("Port {}:  Open".format(port))
            i = +1
            s.close()
    print("\n")
    if i == 0:
        print("Open Ports:  0!")



if __name__ == "__main__":
    subprocess.call('clear', shell=True)
    socket.setdefaulttimeout(0.5)
    print("Portscanner")
    print("-"*20)
    print("\n")

    try:
        server = input("Enter host: ")
        serverIP = socket.gethostbyname(server)
        print("Define portrange")
        startport = int(input("From: "))
        endport = int(input("To: "))
        print("\n")
        print("scanning for {0} with IP: {1} on Port {2}-{3}".format(server, serverIP, startport, endport))
        print("...")
        scan_host(startport,endport,serverIP)
    except socket.gaierror:
        print("no servername...")
        pass







