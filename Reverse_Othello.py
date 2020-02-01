import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *  # QIcon
from PyQt5.QtWidgets import *  # QApplication, QDesktopWidget, QMainWindow,
from PyQt5 import uic

# connect ui file in same path
form_class = uic.loadUiType("Reverse_Othello.ui")[0]


class CreateGame(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # visible UI
        self.initUI()

        self.BLACK_CELL = 'b'
        self.WHITE_CELL = 'w'
        self.EMPTY_CELL = '0'
        self.turn = 'b'

        self.BOARD_LEN = 8
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.plate = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                      for y in range(self.BOARD_LEN)]
        self.plateStatus = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                            for y in range(self.BOARD_LEN)]
        self.avableLocation = []
        self.createBoard()
        self.initGame()
        self.findAvaliable()
        self.showMarker()

    def findAvaliable(self):
        self.avableLocation = []

        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.BLACK_CELL:
                    print("find Black")
                    for k in range(8):
                        x, y = i, j
                        while(self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.WHITE_CELL):
                            print(f'status : {k}')
                            x = x + self.dx[k]
                            y = y + self.dy[k]
                        if x == i and y == j:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y + self.dy[k]] == self.BLACK_CELL:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y + self.dy[k]] == self.EMPTY_CELL:
                            self.avableLocation.append(
                                [x + self.dx[k], y + self.dy[k]])  # 길이 2자리 배열을 통째로
        return

    def initGame(self):
        self.plateStatus[3][3] = self.WHITE_CELL
        self.plateStatus[4][4] = self.WHITE_CELL
        self.plateStatus[3][4] = self.BLACK_CELL
        self.plateStatus[4][3] = self.BLACK_CELL
        # 정보 바탕으로 돌 그리기

    def showMarker(self):
        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.BLACK_CELL:
                    self.plate[i][j].setIcon(QIcon("./image/black.png"))
                    self.plate[i][j].setIconSize(QSize(50, 50))
                elif self.plateStatus[i][j] == self.WHITE_CELL:
                    self.plate[i][j].setIcon(QIcon("./image/white.png"))
                    self.plate[i][j].setIconSize(QSize(50, 50))

        for i in range(len(self.avableLocation)):
            x = self.avableLocation[i][0]
            y = self.avableLocation[i][1]
            self.plate[x][y].setIcon(QIcon("./image/Othello icon.png"))
            self.plate[x][y].setIconSize(QSize(20, 20))

    def initUI(self):

        self.setWindowTitle('Reverse Othello')
        self.setWindowIcon(QIcon('./image/Othello icon.png'))
        self.center()
        # self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createBoard(self):
        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                self.plate[i][j] = QPushButton("", self)
                self.plate[i][j].move(10+60*i, 10+60*j)
                self.plate[i][j].resize(60, 60)


if __name__ == '__main__':
    # QApplication : program start class
    app = QApplication(sys.argv)
    myWindow = CreateGame()  # create ReverseOthello instance
    myWindow.show()
    # myWindow2 = Reversi()  # create Reversi instance
    # myWindow2.show()
    # Enters the program into the event loop (running the program)
    app.exec_()
