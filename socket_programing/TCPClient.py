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

NAME = input("Nhập tên của bạn: ")

flag = ""
while flag != "!OK!":   # Check trường hợp chưa bật TCPServer.py
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, TCP
    try:
        client.connect(ADDR)
        client.send(NAME.encode(FORMAT))  # Gửi riêng NAME tới server trước
        connected = True
        flag = client.recv(HEADER).decode(
            FORMAT
        )  # Chờ server phản hồi !OK! nghĩa là thiết lập kết nối thành công
    except ConnectionRefusedError:
        print("...Đang chờ server phản hồi...")
        sleep(2)

print(f'Kết nối tới "{SERVER}" thành công')


def handle_rev(client):
    global connected
    try:
        while connected:
            msg = client.recv(HEADER).decode(FORMAT)
            if not msg:  # Server không gửi gì -> server bị tắt -> dừng chương trình
                print("SERVER IS CLOSED")
                connected = False
                break
            print(msg)
    except ConnectionResetError:  # Khi tắt server thì catch lỗi này
        print("SERVER IS CLOSED")
        connected = False
    client.close()
    os._exit(1)


def handle_send(client):
    global connected
    while connected:
        msg = input()
        send(f"[{NAME}]: {msg}")  # SEND NAME (nhập từ bàn phím), msg
        if DISCONNECT_MESSAGE in msg:
            connected = False
    client.close()
    os._exit(1)


def send(msg):
    message = msg.encode(FORMAT)
    message += b" " * (HEADER - len(message))  # Thêm dấu cách cho đủ 64 byte
    client.send(message)


thread_rev = threading.Thread(target=handle_rev, args=(client,))
thread_rev.start()

thread_send = threading.Thread(target=handle_send, args=(client,))
thread_send.start()

# thread_rev.join()  # Wait for the threads to finish before exiting
# thread_send.join()
