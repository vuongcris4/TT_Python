import socket
import threading
import os
from time import sleep

HEADER = 64
PORT = 8000
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!exit"
SERVER = "9618lethirieng.ddns.net"
ADDR = (SERVER, PORT)

TIN_NHAN = ""
SERVER_ANNOUNCE = (0, "nothing")

def sendMessageFromOtherFile(msg):
    global isButtonPressed
    isButtonPressed = True  # True
    global TIN_NHAN
    TIN_NHAN = msg
    sleep(0.1)  # Không có delay thì Send liên tiếp chỉ send cái cuối



def init_connect(name):
    global NAME
    NAME = name

    flag = ""
    while flag != "!OK!":  # Check trường hợp chưa bật TCPServer.py
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP
        try:
            client.connect(ADDR)
            client.send(NAME.encode(FORMAT))  # Gửi riêng NAME tới server trước
            global connected
            connected = True
            flag = client.recv(HEADER).decode(
                FORMAT
            )  # Chờ server phản hồi !OK! nghĩa là thiết lập kết nối thành công
        except ConnectionRefusedError:
            print("...Đang chờ server phản hồi...")
            sleep(2)

    print(f'Kết nối tới "{SERVER}" thành công')

    thread_rev = threading.Thread(target=handle_rev, args=(client,))
    thread_rev.start()

    thread_send = threading.Thread(target=handle_send, args=(client,))
    thread_send.start()


def handle_rev(client):
    global connected
    receivedAnnouncement = 0    # Đánh số thứ tự gói tin đến để kiểm tra có gói tin mới đến
    try:
        while connected:
            msg = client.recv(HEADER).decode(FORMAT)
            if not msg:  # Server không gửi gì -> server bị tắt -> dừng chương trình
                receivedAnnouncement+=1
                global SERVER_ANNOUNCE
                SERVER_ANNOUNCE=(receivedAnnouncement, "SERVER IS CLOSED")
                # print(SERVER_ANNOUNCE)
                connected = False
                break
            print(msg)
    except ConnectionResetError:  # Khi tắt server thì catch lỗi này
        receivedAnnouncement+=1
        SERVER_ANNOUNCE=(receivedAnnouncement, "SERVER IS CLOSED")
        # print(SERVER_ANNOUNCE)

        connected = False
    client.close()
    os._exit(1)


def handle_send(client):
    global connected
    global isButtonPressed
    isButtonPressed = False

    while connected:
        if isButtonPressed:  # Khi nhấn nút SEND thì biến này thành TRUE để send message
            send(f"[{NAME}]: {TIN_NHAN}")  # SEND NAME (nhập từ bàn phím), msg
            if DISCONNECT_MESSAGE in TIN_NHAN:
                connected = False
            isButtonPressed = False  # Gán lại FALSE để chạy 1 lần duy nhất

    client.close()
    os._exit(1)


def send(msg):
    message = msg.encode(FORMAT)
    message += b" " * (HEADER - len(message))  # Thêm dấu cách cho đủ 64 byte
    client.send(message)
