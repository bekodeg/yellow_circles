import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.btn.clicked.connect(self.paint)
        self.pixmap = None

    def paint(self):
        qp = QPainter(self)
        if self.pixmap is None:
            self.pixmap = QPixmap(self.out.width(), self.out.height())
            self.pixmap.fill(QColor(255, 255, 255))
        # Начинаем процесс рисования
        qp.begin(self.pixmap)
        qp.setBrush(QColor(255, 255, 0))
        r = randint(10, 200)
        x = randint(10, max(11, self.pixmap.width() - r))
        y = randint(10, max(11, self.pixmap.height() - r))
        qp.drawEllipse(x, y, r, r)
        print('ok')
        # Завершаем рисование
        qp.end()
        self.out.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())