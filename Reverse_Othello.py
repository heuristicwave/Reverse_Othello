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
        self.MY_CELL = 'b'
        self.OP_CELL = 'w'
        #self.turn = 'b'

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
        self.objectNameActivate()

    def objectNameActivate(self):
        # fix error using lambda (TypeError: argument 1 has unexpected type 'NoneType')
        self.plate[0][0].clicked.connect(lambda: self.clickedButton(self.plate[0][0]))
        self.plate[0][1].clicked.connect(lambda: self.clickedButton(self.plate[0][1]))
        self.plate[0][2].clicked.connect(lambda: self.clickedButton(self.plate[0][2]))        
        self.plate[0][3].clicked.connect(lambda: self.clickedButton(self.plate[0][3]))
        self.plate[0][4].clicked.connect(lambda: self.clickedButton(self.plate[0][4]))
        self.plate[0][5].clicked.connect(lambda: self.clickedButton(self.plate[0][5]))        
        self.plate[0][6].clicked.connect(lambda: self.clickedButton(self.plate[0][6]))        
        self.plate[0][7].clicked.connect(lambda: self.clickedButton(self.plate[0][7]))
        self.plate[1][0].clicked.connect(lambda: self.clickedButton(self.plate[1][0]))
        self.plate[1][1].clicked.connect(lambda: self.clickedButton(self.plate[1][1]))
        self.plate[1][2].clicked.connect(lambda: self.clickedButton(self.plate[1][2]))
        self.plate[1][3].clicked.connect(lambda: self.clickedButton(self.plate[1][3]))
        self.plate[1][4].clicked.connect(lambda: self.clickedButton(self.plate[1][4]))
        self.plate[1][5].clicked.connect(lambda: self.clickedButton(self.plate[1][5]))
        self.plate[1][6].clicked.connect(lambda: self.clickedButton(self.plate[1][6]))
        self.plate[1][7].clicked.connect(lambda: self.clickedButton(self.plate[1][7]))
        self.plate[2][0].clicked.connect(lambda: self.clickedButton(self.plate[2][0]))
        self.plate[2][1].clicked.connect(lambda: self.clickedButton(self.plate[2][1]))
        self.plate[2][2].clicked.connect(lambda: self.clickedButton(self.plate[2][2]))        
        self.plate[2][3].clicked.connect(lambda: self.clickedButton(self.plate[2][3]))
        self.plate[2][4].clicked.connect(lambda: self.clickedButton(self.plate[2][4]))
        self.plate[2][5].clicked.connect(lambda: self.clickedButton(self.plate[2][5]))        
        self.plate[2][6].clicked.connect(lambda: self.clickedButton(self.plate[2][6]))        
        self.plate[2][7].clicked.connect(lambda: self.clickedButton(self.plate[2][7]))
        self.plate[3][0].clicked.connect(lambda: self.clickedButton(self.plate[3][0]))
        self.plate[3][1].clicked.connect(lambda: self.clickedButton(self.plate[3][1]))
        self.plate[3][2].clicked.connect(lambda: self.clickedButton(self.plate[3][2]))        
        self.plate[3][3].clicked.connect(lambda: self.clickedButton(self.plate[3][3]))
        self.plate[3][4].clicked.connect(lambda: self.clickedButton(self.plate[3][4]))
        self.plate[3][5].clicked.connect(lambda: self.clickedButton(self.plate[3][5]))        
        self.plate[3][6].clicked.connect(lambda: self.clickedButton(self.plate[3][6]))        
        self.plate[3][7].clicked.connect(lambda: self.clickedButton(self.plate[3][7]))
        self.plate[4][0].clicked.connect(lambda: self.clickedButton(self.plate[4][0]))
        self.plate[4][1].clicked.connect(lambda: self.clickedButton(self.plate[4][1]))
        self.plate[4][2].clicked.connect(lambda: self.clickedButton(self.plate[4][2]))        
        self.plate[4][3].clicked.connect(lambda: self.clickedButton(self.plate[4][3]))
        self.plate[4][4].clicked.connect(lambda: self.clickedButton(self.plate[4][4]))
        self.plate[4][5].clicked.connect(lambda: self.clickedButton(self.plate[4][5]))        
        self.plate[4][6].clicked.connect(lambda: self.clickedButton(self.plate[4][6]))        
        self.plate[4][7].clicked.connect(lambda: self.clickedButton(self.plate[4][7]))
        self.plate[5][0].clicked.connect(lambda: self.clickedButton(self.plate[5][0]))
        self.plate[5][1].clicked.connect(lambda: self.clickedButton(self.plate[5][1]))
        self.plate[5][2].clicked.connect(lambda: self.clickedButton(self.plate[5][2]))        
        self.plate[5][3].clicked.connect(lambda: self.clickedButton(self.plate[5][3]))
        self.plate[5][4].clicked.connect(lambda: self.clickedButton(self.plate[5][4]))
        self.plate[5][5].clicked.connect(lambda: self.clickedButton(self.plate[5][5]))        
        self.plate[5][6].clicked.connect(lambda: self.clickedButton(self.plate[5][6]))        
        self.plate[5][7].clicked.connect(lambda: self.clickedButton(self.plate[5][7]))
        self.plate[6][0].clicked.connect(lambda: self.clickedButton(self.plate[6][0]))
        self.plate[6][1].clicked.connect(lambda: self.clickedButton(self.plate[6][1]))
        self.plate[6][2].clicked.connect(lambda: self.clickedButton(self.plate[6][2]))        
        self.plate[6][3].clicked.connect(lambda: self.clickedButton(self.plate[6][3]))
        self.plate[6][4].clicked.connect(lambda: self.clickedButton(self.plate[6][4]))
        self.plate[6][5].clicked.connect(lambda: self.clickedButton(self.plate[6][5]))        
        self.plate[6][6].clicked.connect(lambda: self.clickedButton(self.plate[6][6]))        
        self.plate[6][7].clicked.connect(lambda: self.clickedButton(self.plate[6][7]))
        self.plate[7][0].clicked.connect(lambda: self.clickedButton(self.plate[7][0]))
        self.plate[7][1].clicked.connect(lambda: self.clickedButton(self.plate[7][1]))
        self.plate[7][2].clicked.connect(lambda: self.clickedButton(self.plate[7][2]))        
        self.plate[7][3].clicked.connect(lambda: self.clickedButton(self.plate[7][3]))
        self.plate[7][4].clicked.connect(lambda: self.clickedButton(self.plate[7][4]))
        self.plate[7][5].clicked.connect(lambda: self.clickedButton(self.plate[7][5]))        
        self.plate[7][6].clicked.connect(lambda: self.clickedButton(self.plate[7][6]))        
        self.plate[7][7].clicked.connect(lambda: self.clickedButton(self.plate[7][7]))
        # iterator로 아래처럼하면 소멸되어 7,7 만남음
        # curPlate = self.plate[i][j]
        # self.plate[i][j].clicked.connect(lambda: self.clickedButton(curPlate))

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
                    print("find AVALIABLE")
                    for k in range(8):
                        x, y = i, j

                        # (i, j)를 기준으로 상하좌우 대각선을 dx, dy로 점검
                        while(self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.OP_CELL):
                            print(f'status : {k}')
                            x = x + self.dx[k]
                            y = y + self.dy[k]

                        if x == i and y == j:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.MY_CELL:
                            continue
                        elif self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.EMPTY_CELL:
                            cur_x = x+self.dx[k]
                            cur_y = y+self.dy[k]
                            # (0, -1) 같은게 안나오도록
                            if cur_x < 0:
                                cur_x = 0
                            elif cur_y < 0:
                                cur_y = 0

                            self.avaliableLocation.append([cur_x, cur_y])
        return

    def initGame(self):
        self.plateStatus[3][3] = self.WHITE_CELL
        self.plateStatus[4][4] = self.WHITE_CELL
        self.plateStatus[3][4] = self.BLACK_CELL
        self.plateStatus[4][3] = self.BLACK_CELL
        # 정보 바탕으로 돌 그리기

    def clearAvaliableLoc(self):
        print('removing...')
        for i in range(len(self.avaliableLocation)):
            x = self.avaliableLocation[i][0]
            y = self.avaliableLocation[i][1]
            print(x,y)
            self.plate[x][y].setIcon(QIcon())

    def clickedButton(self, btn):        
        self.clearAvaliableLoc() # 이미지 삭제
        position = btn.objectName() # type(position) => <class 'str'>
        print(f'position : {position}')
        x = int(position[0])
        y = int(position[1])

        self.plateStatus[x][y] = self.OP_CELL

        for i in range(8):
            self.updateBoard(x, y, i)

        print(self.plateStatus)
        # self.findAvaliable()

        self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL

        self.findAvaliable()
        self.showMarker()

    def updateBoard(self, x, y, direction):
        if self.plateStatus[x][y] == self.MY_CELL:
            print(f'{self.MY_CELL} found!!!')
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
                self.plate[i][j] = QPushButton("", self)
                self.plate[i][j].setObjectName(str(i)+str(j))
                self.plate[i][j].move(10+60*i, 10+60*j)
                self.plate[i][j].resize(60, 60)


if __name__ == '__main__':
    # QApplication : program start class
    app = QApplication(sys.argv)
    myWindow = CreateGame()  # create ReverseOthello instance
    myWindow.show()
    # Enters the program into the event loop (running the program)
    app.exec_()
