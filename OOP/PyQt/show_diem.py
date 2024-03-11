from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys
from database import *
mydb = MY_DB()

class SHOW_DIEM(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("show_diem.ui", self)
        # self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_diem = SHOW_DIEM()
    app.exec()
