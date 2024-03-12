from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys

from database import *
mydb = MY_DB()


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        # self.show()

        self.btnCalculate.clicked.connect(self.average)

    def average(self):
        Toan = float(self.edtToan.text())
        Li = float(self.edtLi.text())
        Anh = float(self.edtAnh.text())
        average = (Toan + Li + Anh) / 3
        return str(round(average, 2))

    def saveToStudentDB(self):
        ID = self.edtID.text()
        Ten = self.edtTen.text()
        Toan = float(self.edtToan.text())
        Li = float(self.edtLi.text())
        Anh = float(self.edtAnh.text())
        mydb.connect()
        mydb.insert_row(ID, Ten, Toan, Li, Anh)
        # mydb.disconnect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MAIN()
    app.exec()
