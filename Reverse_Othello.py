import sys
import signal
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
        #self.turn = 'b'
        self.MY_CELL = 'b'
        self.OP_CELL = 'w'

        self.BOARD_LEN = 8
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.plate = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                      for y in range(self.BOARD_LEN)]
        self.plateStatus = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                            for y in range(self.BOARD_LEN)]
        self.avaliableLocation = []
        self.createBoard()
        self.initGame()
        self.findAvaliable()
        self.showMarker()

    # def cell_count(self):
    #     white = 0
    #     black = 0

    #     for i in range(self.BOARD_LEN):
    #         for j in range(self.BOARD_LEN):
    #             if self.board[i][j] == self.WHITE_CELL:
    #                 white += 1
    #             elif self.board[i][j] == self.BLACK_CELL:
    #                 black += 1

    #     return black, white

    def findAvaliable(self):
        self.avaliableLocation = []

        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.MY_CELL:
                    print("find Black")
                    for k in range(8):
                        x, y = i, j
                        # (i, j)를 기준으로 상하좌우 대각선을 dx, dy로 점검
                        while(self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.OP_CELL):
                            print(f'status : {k}')
                            x = x + self.dx[k]
                            y = y + self.dy[k]
                        if x == i and y == j:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y + self.dy[k]] == self.MY_CELL:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y + self.dy[k]] == self.EMPTY_CELL:
                            self.avaliableLocation.append(
                                [x + self.dx[k], y + self.dy[k]])  # 길이 2자리 배열을 통째로
        return

    def initGame(self):
        self.plateStatus[3][3] = self.WHITE_CELL
        self.plateStatus[4][4] = self.WHITE_CELL
        self.plateStatus[3][4] = self.BLACK_CELL
        self.plateStatus[4][3] = self.BLACK_CELL
        # 정보 바탕으로 돌 그리기

    def clickedButton(self, btn):
        print(btn)
        print('clicked')
        position = btn.objectName()
        print(f'position : {position}')
        print(type(position))
        x = int(position[0])
        y = int(position[1])

        self.plateStatus[x][y] = self.OP_CELL

        for i in range(8):
            self.updateBoard(x, y, i)

        print('call show')
        print(self.plateStatus)
        self.showMarker()

        # self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL

        # self.findAvaliable()
        # self.showMarker()

    def updateBoard(self, x, y, direction):
        if self.plateStatus[x][y] == self.MY_CELL:
            print('found!!!')
            return 1
        elif self.plateStatus[x][y] == self.EMPTY_CELL:
            return 0

        cur_x = x
        cur_y = y

        cur_x = cur_x + self.dx[direction]
        cur_y = cur_y + self.dy[direction]

        tmp = self.updateBoard(cur_x, cur_y, direction)

        if tmp:
            print(f'return 1 : {self.plateStatus[x][y]}')
            self.plateStatus[x][y] = self.MY_CELL
            return 1

        return 0

    def showMarker(self):
        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.BLACK_CELL:
                    self.plate[i][j].setIcon(QIcon("./image/black.png"))
                    self.plate[i][j].setIconSize(QSize(50, 50))
                elif self.plateStatus[i][j] == self.WHITE_CELL:
                    self.plate[i][j].setIcon(QIcon("./image/white.png"))
                    self.plate[i][j].setIconSize(QSize(50, 50))
                elif self.plateStatus[i][j] == self.EMPTY_CELL:
                    self.plate[i][j].setEnabled(False)

        print(self.avaliableLocation)
        for i in range(len(self.avaliableLocation)):
            x = self.avaliableLocation[i][0]
            y = self.avaliableLocation[i][1]
            self.plate[x][y].setIcon(QIcon("./image/Othello icon.png"))
            self.plate[x][y].setIconSize(QSize(20, 20))
            # Avaliable Button Activate
            self.plate[x][y].setEnabled(True)

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
                #curPlate = self.plate[i][j]
                self.plate[i][j] = QPushButton("", self)
                self.plate[i][j].setObjectName(str(i)+str(j))
                # self.plate[i][j].clicked.connect(
                #     lambda: self.clickedButton(self.plate[i][j]))
                self.plate[i][j].move(10+60*i, 10+60*j)
                self.plate[i][j].resize(60, 60)


if __name__ == '__main__':
    # QApplication : program start class
    app = QApplication(sys.argv)
    myWindow = CreateGame()  # create ReverseOthello instance
    myWindow.show()
    # Enters the program into the event loop (running the program)
    app.exec_()
