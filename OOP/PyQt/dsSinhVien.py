from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic
import sys
from database import *

mydb = MY_DB()


class DANH_SACH(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dsSinhVien.ui", self)
        # self.show()
        self.tbSinhVien.itemSelectionChanged.connect(self.get_item_by_select)

    def load_table_student(self):
        try:
            mydb.connect()
            result = mydb.load_table_student()
            self.tbSinhVien.setRowCount(0)
            for row_num, row_data in enumerate(result):
                self.tbSinhVien.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.tbSinhVien.setItem(
                        row_num, col_num, QTableWidgetItem(str(col_data))
                    )
        except Exception as e:
            print("Error when load database: ", e)
        finally:
            mydb.disconnect()

        # mydb.disconnect()

    def get_item_by_select(self):
        select_row = self.tbSinhVien.currentRow()
        if select_row != -1:
            self.id_selected = self.tbSinhVien.item(select_row, 0).text()
        return self.id_selected

    def delete_by_id(self):
        mydb.connect()
        # print(self.id_selected)
        mydb.delete_by_id(self.id_selected)
        self.load_table_student()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # app.setQuitOnLastWindowClosed(False)
    # app.lastWindowClosed.connect(closeWindow)

    danh_sach = DANH_SACH()
    app.exec()
