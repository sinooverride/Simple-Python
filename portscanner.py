import socket
import subprocess
import sys

def scan_host():
    i = 1
    while i < 2:
        try:
            server = input("Enter Host:")
            serverIP = socket.gethostbyname(server)
            print("scanning for {0} with IP: {1} on Port 1-1024".format(server,serverIP))
            print("...")

            for port in range(1,1024):  
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                output = s.connect_ex((serverIP, port))
                if output == 0:
                    print ("Port {}:  Open".format(port))
                s.close()
            print("\n")
            i = 2

        except socket.gaierror:
            print("no servername...")


if __name__ == "__main__":
    subprocess.call('clear', shell=True)
    socket.setdefaulttimeout(0.5)
    print("Portscanner")
    print("-"*20)
    print("\n")

    scan_host()





