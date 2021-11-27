import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5 import uic, Qt, QtCore, QtGui
from random import randint, sample
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_flag(painter)
            painter.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, painter):
        color = QtGui.QColor(*sample(range(255), 3))
        painter.setPen(QPen(color, 8, QtCore.Qt.SolidLine))
        painter.setBrush(QBrush(color, QtCore.Qt.SolidPattern))
        diameter = randint(1, 600)
        painter.drawEllipse(200, 200, diameter, diameter)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())