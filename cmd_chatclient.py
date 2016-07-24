import socket


def chat_client():
    host = input("Host IP: ")
    host = host.encode('utf-8')
    port = int(input("Port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.timeout(5)
    
    try:
    	s.connect((host,port))
    	print("connected to {0} on port {1}".format(host,port))
    	print("start your chat")

    except:
    	print("unable to connect")
    	raise
    
    message = input("Me: ")
    while message != "exit" :
   			s.send(message.encode('utf-8'))
   			data = s.recv(1024)
   			data = data.decode('utf-8')
   			print ("server: " + data)
   			message = input("Me: ") 	
    s.close()	

    		
if __name__ == '__main__':
	chat_client()

