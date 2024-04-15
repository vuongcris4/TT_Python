# from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
# from PyQt6.QtCore import Qt, pyqtSignal

# class EnterLineEdit(QLineEdit):
#     enterPressed = pyqtSignal()

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Return:
#             self.enterPressed.emit()
#         else:
#             super().keyPressEvent(event)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Press Enter to Click Button")

#         central_widget = QWidget()  # Tạo widget
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)

#         self.input_field = EnterLineEdit()
#         layout.addWidget(self.input_field)

#         self.button = QPushButton("Click Me")
#         layout.addWidget(self.button)

#         self.input_field.enterPressed.connect(self.button.click)
#         self.button.clicked.connect(self.on_button_clicked)

#     def on_button_clicked(self):
#         print(self.input_field.text())

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem


def main():
    app = QApplication(sys.argv)

    w = QListWidget()
    w.resize(320, 240)
    w.show()

    def on_timeout():
        item = QListWidgetItem(f"item-{w.count()}")
        w.addItem(item)
        w.scrollToItem(item)

    timer = QTimer(interval=1000, timeout=on_timeout)
    timer.start()

    sys.exit(app.exec_())


main()
