from socket import *
serverPort = 8000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()
    print(message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    