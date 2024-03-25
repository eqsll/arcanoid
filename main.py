from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('')
        self.setFixedSize(1280, 720)
        self.main_screen()

    def main_screen(self):
        self.clear_window()

        self.setStyleSheet('background-image: url("menu.jpg");')

        btn_style = "border-radius: 35px;" \
                    "background: #008cff;" \
                    "color: #f7dfea;" \
                    "font-size: 20px"

        self.btnTs1 = QtWidgets.QPushButton('ИГРАТЬ', self)
        self.btnTs1.setGeometry(874, 106, 260, 120)
        self.btnTs1.setStyleSheet(btn_style)
        self.btnTs1.show()

        self.btnTs2 = QtWidgets.QPushButton('РЕЗУЛЬТАТЫ', self)
        self.btnTs2.setGeometry(874, 264, 260, 120)
        self.btnTs2.clicked.connect(self.second_screen)
        self.btnTs2.setStyleSheet(btn_style)
        self.btnTs2.show()

        self.btnTs3 = QtWidgets.QPushButton('ВЫХОД', self)
        self.btnTs3.setGeometry(874, 422, 260, 120)
        self.btnTs3.clicked.connect(quit)
        self.btnTs3.setStyleSheet(btn_style)
        self.btnTs3.show()

    def second_screen(self):
        self.clear_window()

        self.setStyleSheet('background-image: url("rezult.png");')

        self.btns2 = QtWidgets.QPushButton('', self)
        self.btns2.setGeometry(0, 0, 100, 100)
        self.btns2.setIcon(QtGui.QIcon('nazad.png'))
        self.btns2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btns2.show()
        self.btns2.clicked.connect(self.main_screen)


    def clear_window(self):
        self.setStyleSheet('background-image: none!important;')
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()


def run_app():
    app = QApplication([])
    window = MainWin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    run_app()