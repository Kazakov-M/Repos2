import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.pushButton:
            qp = QPainter()
            qp.begin(self)
            self.surcle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def surcle(self, qp):
        qp.setBrush(QColor(254,216,0))
        x = random.randrange(50, 500)
        y = random.randrange(50, 500)
        x_x = random.randrange(50, 500)
        qp.drawEllipse(x, y, x_x, x_x)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())