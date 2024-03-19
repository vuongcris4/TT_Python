from PyQt6.QtWidgets import QApplication

from main import MAIN
from show_diem import SHOW_DIEM
from dsSinhVien import DANH_SACH

from database import *

mydb = MY_DB()

 
class UI:
    def __init__(self):
        self.main = MAIN()
        self.main.show()
        self.main.btnCalculate.clicked.connect(lambda: self.changeUI("show_diem"))

        self.show_diem = SHOW_DIEM()
        self.show_diem.btnCancel.clicked.connect(lambda: self.changeUI("main"))
        self.show_diem.btnSave.clicked.connect(lambda: self.main.saveToStudentDB())
        self.show_diem.btnSave.clicked.connect(lambda: self.changeUI("main"))

        self.main.btnLoad.clicked.connect(lambda: self.changeUI("dsSinhVien"))
        self.main.btnLoad.clicked.connect(lambda: self.dsSinhVien.load_table_student())

        self.dsSinhVien = DANH_SACH()
        self.dsSinhVien.btnOK.clicked.connect(lambda: self.changeUI("main"))
        self.dsSinhVien.btnRemove.clicked.connect(lambda: self.dsSinhVien.delete_by_id())

    def changeUI(self, i):
        if i == "show_diem":  # khi bấm nút btnCalculate
            self.main.hide()
            self.show_diem.lbDiem.setText(
                self.main.average()
            )  # Lấy kết quả từ hàm average ở main.py gán vào lbDiem ở show_diem.ui
            self.show_diem.show()
        elif i == "main":
            self.show_diem.hide()
            self.dsSinhVien.hide()
            self.main.show()
        elif i == "dsSinhVien":
            self.main.hide()
            self.dsSinhVien.show()


if __name__ == "__main__":
    app = QApplication([])
    ui = UI()
    app.exec()
