from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('ARCANOID')
        self.setGeometry(600, 150, 800, 800)

        self.zagolovok = QtWidgets.QLabel(self)
        self.zagolovok.setText('ARCANOID')
        self.zagolovok.move(375, 300)

        self.btn_start_game = QtWidgets.QPushButton(self)
        self.btn_start_game.move(310, 400)
        self.btn_start_game.setText('ИГРАТЬ')
        self.btn_start_game.setFixedSize(200, 90)


        self.btn_rezult = QtWidgets.QPushButton(self)
        self.btn_rezult.move(310, 500)
        self.btn_rezult.setText('РЕЗУЛЬТАТЫ')
        self.btn_rezult.setFixedSize(200, 90)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(310, 600)
        self.btn_exit.setText('ВЫХОД')
        self.btn_exit.setFixedSize(200, 90)
        self.btn_exit.clicked.connect(quit)

class GameWin(QtWidgets):
    def __init__(self):
        super(GameWin, self).__iniy__()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()