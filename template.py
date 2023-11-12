import sys

from io import StringIO
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel



class Template(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5')
        self.setGeometry(300, 300, 300, 300)
        self.button = QPushButton('PyQt5 button', self)
        self.button.resize(100, 100)
        self.button.move(100, 100)
        self.label = QLabel('') 
        self.label.resize(50, 250)
        self.label.move(25, 240)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoComb()
    ex.show()
    sys.exit(app.exec())
