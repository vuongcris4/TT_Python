import TCPClient
import time

TCPClient.init_connect("Vương")

TCPClient.sendMessageFromOtherFile("a")
TCPClient.sendMessageFromOtherFile("b")
TCPClient.sendMessageFromOtherFile("c")
TCPClient.sendMessageFromOtherFile("d")

before = TCPClient.SERVER_ANNOUNCE[0]
while True:
    try:
        print(TCPClient.SERVER_ANNOUNCE[0], " ", TCPClient.SERVER_ANNOUNCE[1])
        if TCPClient.SERVER_ANNOUNCE[0] != before:
            print(TCPClient.SERVER_ANNOUNCE[1])
        before = TCPClient.SERVER_ANNOUNCE[0]
    except:
        pass

# while True:
#     print(TCPClient.SERVER_ANNOUNCE[0])
#     time.sleep(0.1)