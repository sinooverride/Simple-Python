import socket

def chat_server():
    host = '127.0.0.1'
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    print("Server is running.")


    while True:
        data, user = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("message from: " + str(user))
        print(": " + data)
        message = input("message: ")
        s.sendto(message.encode('utf-8'), user)
    s.close()

if __name__ == '__main__':
    chat_server()