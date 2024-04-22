from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QFileDialog,
    QWidget,
)
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys
import os


class MESSAGE(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("message_windows.ui", self)

        self.txtMessage.setFocus()
        self.btnFile.clicked.connect(self.showFileDialog)

        # self.show()

    def keyPressEvent(self, event):  # Nhấn phím enter thì click btnSend
        if event.key() == Qt.Key.Key_Return:
            self.btnSend.click()

    def showFileDialog(self):
        file_filter = "All files (*)"
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file",
            directory=os.getcwd(),
            filter=file_filter,
        )
        print(str(response))  # ('FILE path', 'All files (*)')
        self.txtMessage.setText(f'SEND_FILE: "{response[0]}"')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MESSAGE = MESSAGE()
    app.exec()
