from PyQt6.QtWidgets import QApplication, QMessageBox, QListWidgetItem
from PyQt6.QtCore import QObject, pyqtSignal, QThread, Qt

from logging_windows import LOGGING
from message_windows import MESSAGE

import socket
import os
from time import sleep


HEADER = 1024
PORT = 8000
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!exit"
SERVER = "9618lethirieng.ddns.net"
ADDR = (SERVER, PORT)

client = ""
connected = False


# Tạo một thread mới song song Main Thread để connect to server, kiểm tra kết nối, nhận gói tin
class Connect_ReceiveMessage(QThread):
    gui_tin_hieu = pyqtSignal(str)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def run(self):
        global client

        global connected
        connected = False

        global received_msg

        while True:
            try:
                if connected == False:  # Nếu kết nối lỗi (realtime check)
                    client = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM
                    )  # ipv4, TCP
                    client.connect(ADDR)
                    client.send(NAME.encode(FORMAT))  # Gửi riêng NAME tới server trước
                    received_msg = client.recv(HEADER).decode(FORMAT)
                    if received_msg != "":
                        connected = True
                        self.gui_tin_hieu.emit(f'Kết nối tới "{SERVER}" thành công')
                    sleep(2)
            except Exception as e:
                # error_message = f"An error occurred: {e}"
                error_message = f"....Đang cố gắng kết nối tới server....."
                self.gui_tin_hieu.emit(error_message)
                connected = False
                sleep(1)

            if connected == True:  # Kết nối thành công thì nhận gói tin
                try:
                    received_msg = client.recv(HEADER).decode(FORMAT)  # GÓI TIN CẦN TÌM
                    # item = QListWidgetItem(
                    #     str(received_msg)
                    # )  # Add từng item kiểu này để scroll xuống được
                    self.ui.message.lstMessage.addItem(received_msg)
                    sleep(0.1)  # Add xong cần một tí thời gian mới scrollDown được
                    self.ui.message.lstMessage.scrollToBottom()
                    # print(received_msg)

                    if received_msg == "":  # Nếu trả về gói tin rỗng thì server bị tắt
                        self.gui_tin_hieu.emit("Lỗi server")
                        connected = False
                        sleep(1)
                except ConnectionResetError:  # Server bị tắt thì gặp lỗi này
                    self.gui_tin_hieu.emit("Server đã bị tắt")
                    connected = False
                    sleep(3)


class UI:
    def __init__(self):
        self.logging = LOGGING()
        self.message = MESSAGE()

        self.logging.show()
        self.logging.btnEnter.clicked.connect(lambda: self.changeUI("message"))
        # self.logging.btnEnter.setShortcut('Enter')
        # btnSend  txtMessage lstMessage
        self.message.btnSend.clicked.connect(self.send_message)

    def changeUI(self, i):
        if i == "message":
            self.logging.hide()
            global NAME
            NAME = self.logging.txtName.text()
            self.message.lbName.setText(NAME)
            self.message.show()
            self.init_connect()  # Khởi tạo kết nối tới server với tên NAME

    def init_connect(self):
        self.connection_thread = Connect_ReceiveMessage(self)
        self.connection_thread.gui_tin_hieu.connect(self.message.lbAnnouce.setText)
        self.connection_thread.start()

    def send_message(self):
        msg = self.message.txtMessage.text()
        # if message:  # Chỉ gửi tin nhắn nếu có nội dung
        # send_thread = SendMessageThread(message)
        # send_thread.send_signal.connect(self.handle_send_result)
        # send_thread.start()
        # print(msg)
        if connected and msg != "":
            item = QListWidgetItem(
                "\t" * 4 + "[Tôi]: " + msg
            )  # Add từng item kiểu này để scroll xuống được
            self.message.lstMessage.addItem(item)  # align right
            self.message.lstMessage.scrollToItem(item)
            self.message.txtMessage.setText("")

        try:
            if msg != "":
                if "SEND_FILE: " not in msg:
                    send_msg(f"[{NAME}]: {msg}")  # SEND NAME (nhập từ bàn phím), msg
                else:
                    send_msg(f"[{NAME}]: {msg}")  # Gửi đường dẫn file
                    send_file(msg)

        except Exception as e:
            print(e)
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Icon.Warning)
            alert.setWindowTitle("Thông báo")
            alert.setText("Chưa kết nối tới server")
            alert.exec()


def send_file(file_path):
    file_path = file_path[
        len("SEND_FILE: ") + 1 : -1
    ]  # Lấy đường dẫn file (bỏ dấu ngoặc kép)
    size_file = str(os.path.getsize(file_path))
    send_msg(size_file + (" " * (HEADER - len(size_file))))  # Gửi kích thước file

    print(file_path)
    with open(file_path, "rb") as file:  # binary mode
        while True:
            data = file.read(1024)
            if not data:
                print(data)
                break  # End of file
            client.sendall(data)
        print("send done")


def send_msg(msg):
    message = msg.encode(FORMAT)
    # message += b" " * (HEADER - len(message))  # Thêm dấu cách cho đủ 64 byte
    client.send(message)


if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    app.exec()
