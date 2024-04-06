from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QLabel, \
    QGraphicsEllipseItem, QGraphicsOpacityEffect
from PyQt5.QtCore import QTimer, Qt


# class Ball(QGraphicsEllipseItem):
#     def __init__(self):
#         super().__init__()
#         self.setRect(0, 0, 20, 20)
#         self.setPos(640, 630)
#         self.x_speed = 5
#         self.y_speed = -5

# class Platform(QGraphicsRectItem):
#     def __init__(self):
#         super().__init__()
#         self.setRect(590, 650, 100, 20)

# class GameScene(QGraphicsScene):
#     def __init__(self):
#         super().__init__()
#         self.ball = Ball()
#         self.platform = Platform()
#         self.addItem(self.ball)
#         self.addItem(self.platform)

# class GameWindow(QGraphicsView):
#     def __init__(self):
#         super().__init__()
#         self.setStyleSheet('background-image: url("play.jpg");')
#         self.setFixedSize(100, 600)
#         # self.scene = GameScene()
#         # self.setScene(self.scene)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.game_loop)
#         self.timer.start(10)


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fongame = None
        self.setWindowTitle('ARCANOID')
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
        self.btns2 = QtWidgets.QPushButton('', self)
        self.btns2.setGeometry(0, 0, 100, 100)
        self.btns2.setIcon(QtGui.QIcon('nazad.png'))
        self.btns2.setStyleSheet('background: blue; border: 2px dashed yellow')
        self.btns2.show()
        self.btns2.clicked.connect(self.main_screen)

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

        self.ball = QLabel(self.fongame)
        self.x_speed = 1
        self.y_speed = -1
        self.ball.setStyleSheet("""
                            border-radius: 10px;
                            min-height: 30px;
                            max-height: 30px;
                            min-width: 30px;
                            max-width: 30px;
                            border-image: url("ball.png");
                        """)
        self.ball.move(140, 130)
        self.ball.show()

        self.platform = QLabel(self.fongame)
        self.platform.setStyleSheet("""
                                    border-radius: 0px;
                                    min-height: 30px;
                                    max-height: 30px;
                                    min-width: 100px;
                                    max-width: 100px;
                                    border-image: url("plat.png");
                                """)
        self.platform.move(350, 490)
        self.platform.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(5)

    def game_loop(self):
        self.ball.move(self.ball.x() + self.x_speed, self.ball.y() + self.y_speed)
        if self.ball.x() <= 0 or self.ball.x() >= self.width() - self.ball.width():
            self.x_speed *= -1
        if self.ball.y() <= 0 or self.ball.y() >= self.height() - self.ball.height():
            self.y_speed *= -1

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.platform.x() <= 0:
                self.platform.move(self.platform.x() - 0, self.platform.y())
            else:
                self.platform.move(self.platform.x() - 25, self.platform.y())
            print(self.platform.x(), self.platform.y())
        elif event.key() == Qt.Key_Right:
            if self.platform.x() + 125 <= 800:
                self.platform.move(self.platform.x() + 25, self.platform.y())
            else:
                self.platform.move(self.platform.x() + 0, self.platform.y())
            print(self.platform.x(), self.platform.y())

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
        for widget in self.findChildren(QtWidgets.QWidget):
            widget.deleteLater()


if __name__ == "__main__":
    app = QApplication([])
    main_win = MainWin()
    main_win.show()
    app.exec_()
