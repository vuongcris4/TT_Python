from socket import *

serverName = "9618lethirieng.ddns.net"
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # ipv4, UDP

while True:
    message = input("Input lowercase sentence: ")
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("UPPERCASE: " + modifiedMessage.decode())

clientSocket.close()
