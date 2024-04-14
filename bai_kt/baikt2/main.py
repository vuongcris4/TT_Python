from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys

from classroom import *


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.show()
        self.lop_hoc = CLASSROOM()

        self.btnAdd.clicked.connect(self.addStudent)

    def addStudent(self):
        ID = str(self.edtID.text())
        Name = str(self.edtName.text())
        GPA = float(self.edtGPA.text())
        student = STUDENT(ID, Name, GPA)
        self.lop_hoc.DS.append(student)
        self.load_table_student()

    def load_table_student(self):
        self.tbStudent.setRowCount(0)
        for student in self.lop_hoc.DS:
            student.View()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MAIN()
    app.exec()
