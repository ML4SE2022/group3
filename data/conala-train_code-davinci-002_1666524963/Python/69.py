from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('QPushButton')

        self.btn = QPushButton('Button', self)
        self.btn.setStyleSheet('background-color: red; color: white')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())