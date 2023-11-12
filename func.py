import sys

from io import StringIO
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



class DoComb(QMainWindow):
    def __init__(self):
        super().__init__()
        f = StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.create_circle)

    def create_circle(self):
        self.label.setText('Нажал на кнопку')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoComb()
    ex.show()
    sys.exit(app.exec())
