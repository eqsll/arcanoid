import random

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import QTimer, Qt

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.colblock = 5
        self.kolohehi = 0
        self.lives = 3
        self.setWindowTitle('ARCANOID')
        self.setFixedSize(1280, 720)
        self.main_screen()

    def game_over(self):
        self.clear_window()
        self.setStyleSheet('background-image: url("gameov.jpg");')

    def game_win(self):
        self.clear_window()
        self.setStyleSheet('background-image: url("gamewin.png");')

    def main_screen(self):
        self.clear_window()
        self.setStyleSheet('background-image: url("menu.jpg");')
        btn_style = "border-radius: 35px;" \
                    "background: #008cff;" \
                    "color: #f7dfea;" \
                    "font-size: 20px"
        self.btnTs1 = QtWidgets.QPushButton('ИГРАТЬ', self)
        self.btnTs1.setGeometry(874, 106, 260, 120)
        self.btnTs1.clicked.connect(self.start_game)
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

    def start_game(self):
        self.clear_window()
        self.setStyleSheet('background-image: url("play.jpg");')

        for i in range(5):
            block = QLabel(self)
            block.setStyleSheet("""
                                    border-radius: 0px;
                                    min-height: 30px;
                                    max-height: 30px;
                                    min-width: 105px;
                                    max-width: 105px;
                                    background: red;
                                """)
            block.move(285 + i * 150, 90)  # Размещение платформ на равном расстоянии друг от друга
            block.show()

        self.fongame = QLabel(self)
        self.fongame.setStyleSheet("""
                                    border-radius: 0px;
                                    min-height: 600px;
                                    max-height: 600px;
                                    min-width: 800px;
                                    max-width: 800px;
                                    background: white;
                                """)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7)
        self.fongame.setGraphicsEffect(opacity_effect)
        self.fongame.move(240, 60)
        self.fongame.setMaximumWidth(800)
        self.fongame.setMaximumHeight(600)
        self.fongame.setMinimumWidth(800)
        self.fongame.setMinimumHeight(600)
        self.fongame.show()

        self.line = QLabel(self)
        self.line.setStyleSheet("""
                                    min-height: 10px;
                                    max-height: 10px;
                                    min-width: 800px;
                                    max-width: 800px;
                                    background: black;
                                """)
        self.line.move(240, 601)
        self.line.show()

        self.x_speed = random.choice([-1, 1])
        self.y_speed = random.choice([-1, 1])

        self.ball = QLabel(self)
        self.ball.setStyleSheet("""
                                    border-radius: 15;
                                    min-height: 30px;
                                    max-height: 30px;
                                    min-width: 30px;
                                    max-width: 30px;
                                    background: black;
                                """)
        self.ball.move(640, 520)
        self.ball.show()

        self.platform = QLabel(self)
        self.platform.setStyleSheet("""
                                    border-radius: 0px;
                                    min-height: 25px;
                                    max-height: 25px;
                                    min-width: 100px;
                                    max-width: 100px;
                                    background: black;
                                """)
        self.platform.move(590, 550)
        self.platform.show()

        self.score = QLabel(self)
        self.score.setText(str(self.lives))
        self.score.setStyleSheet("""
                                    min-height: 30px;
                                    max-height: 30px;
                                    min-width: 30px;
                                    max-width: 30px;
                                    background: transparent;
                                    font-size: 30px;
                                    text-align: center;
                                """)
        self.score.move(940, 620)
        self.score.show()

        self.ohehi = QLabel(self)
        self.ohehi.setText(str(self.kolohehi))
        self.ohehi.setStyleSheet("""
                                            min-height: 30px;
                                            max-height: 30px;
                                            min-width: 30px;
                                            max-width: 30px;
                                            background: transparent;
                                            font-size: 30px;
                                            text-align: center;
                                        """)
        self.ohehi.move(330, 620)
        self.ohehi.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(10)

    def game_loop(self):
        self.ball.move(self.ball.x() + self.x_speed, self.ball.y() + self.y_speed)

        if self.ball.x() <= 240 or self.ball.x() >= 1040 - self.ball.width():
            self.x_speed *= -1

        if self.ball.y() <= 60:
            self.y_speed *= -1

        if self.ball.y() >= 600 - self.ball.height():
            self.lives -= 1  # Уменьшаем количество жизней при вылете мяча за нижнюю границу
            self.score.setText(str(self.lives))
            if self.lives == 0:
                self.timer.stop()
                self.game_over()
                self.lives += 3
                self.kolohehi = 0
            else:
                self.ball.move(640, 520)  # Возвращаем мяч в начальное положение
                self.platform.move(590, 550) # Возвращаем платформу в начальное положение
        else:
            if self.ball.geometry().intersects(self.platform.geometry()):
                self.y_speed *= -1

        for block in self.findChildren(QtWidgets.QLabel):
            if (block.geometry().width() == 105) and (self.ball.geometry().intersects(block.geometry())):
                self.y_speed *= -1
                self.colblock -= 1
                block.deleteLater()

                if self.colblock == 0:
                    if self.lives < 3:
                        self.lives += 1
                    self.clear_window()
                    self.start_game()
                    self.kolohehi += 20
                    self.ohehi.setText(str(self.kolohehi))
                    self.colblock += 5

                    if self.kolohehi >= 100:
                        self.kolohehi = 0
                        self.timer.stop()
                        self.game_win()





        self.ball.move(self.ball.x() + self.x_speed, self.ball.y() + self.y_speed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Space:
            self.main_screen()
        if event.key() == Qt.Key_Left:
            if self.platform.x() <= 240:
                self.platform.move(self.platform.x() - 0, self.platform.y())
            else:
                self.platform.move(self.platform.x() - 50, self.platform.y())
        elif event.key() == Qt.Key_Right:
            if self.platform.x() + 150 <= 1040:
                self.platform.move(self.platform.x() + 50, self.platform.y())
            else:
                self.platform.move(self.platform.x() + 0, self.platform.y())

    def second_screen(self):
        self.clear_window()
        self.setStyleSheet("""background-image: url("rezult.png");""")
        self.btns2 = QtWidgets.QPushButton('', self)
        self.btns2.setGeometry(0, 0, 100, 100)
        self.btns2.setStyleSheet("""
                                    background-image: url("naz.jpg");
                                    min-height: 93px;
                                    max-height: 93px;
                                    min-width: 100px;
                                    max-width: 100px;
                                    border: none;
                                    margin: 0px;
                                    padding: 0px;
                                    """)
        self.btns2.clicked.connect(self.main_screen)
        self.btns2.show()

        self.fonrez = QLabel(self)
        self.fonrez.setStyleSheet("""
                                        border-radius: 110px;
                                        min-height: 600px;
                                        max-height: 600px;
                                        min-width: 800px;
                                        max-width: 800px;
                                        background: white;
                                        """)
        opacity_effect = QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.2)
        self.fonrez.setGraphicsEffect(opacity_effect)
        self.fonrez.move(240, 60)
        self.fonrez.setMaximumWidth(800)
        self.fonrez.setMaximumHeight(600)
        self.fonrez.setMinimumWidth(800)
        self.fonrez.setMinimumHeight(600)
        self.fonrez.show()

        self.rezline = QLabel(self)
        self.rezline.setStyleSheet("""
                                        border-radius: 5; 
                                        min-height: 10px;
                                        max-height: 10px;
                                        min-width: 700px;
                                        max-width: 700px;
                                        background: black;
                                        """)
        self.rezline.move(290, 130)
        self.rezline.show()

        self.label = QLabel('ПОПЫТКА', self)
        self.label.setStyleSheet('background: transparent;')  # Установка прозрачного фона
        self.label.setFont(QFont('Arial', 20))
        self.label.adjustSize()
        self.label.move(320, 160)
        self.label.show()

        self.label = QLabel('ОЧКИ', self)
        self.label.setStyleSheet('background: transparent;')
        self.label.setFont(QFont('Arial', 20))
        self.label.adjustSize()
        self.label.move(800, 160)
        self.label.show()

        self.label = QLabel('РЕЗУЛЬТАТЫ', self)
        self.label.setStyleSheet('background: transparent;')
        self.label.setFont(QFont('Arial', 25))
        self.label.adjustSize()
        self.label.move(510, 80)
        self.label.show()

    def clear_window(self):
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()


if __name__ == "__main__":
    app = QApplication([])
    main_win = MainWin()
    main_win.show()
    app.exec_()