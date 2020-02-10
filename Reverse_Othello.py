import sys
import os
import signal
import threading
from PyQt5.QtCore import QThread, QSize, QTimer, QTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QPushButton, QMessageBox, QInputDialog, QLineEdit, QDialog, QLabel, QGridLayout
from PyQt5 import uic
from lib.python.othello import *
from communication import *
from minmax import *
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
        self.TURN = 0
        self.gameType = 'Alone'
        self.playStrategy = 0    # index_0 : human, index_1 : AI
        self.remainTime = 15
        othelloLib = 0

        self.BOARD_LEN = 8
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.plate = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                      for y in range(self.BOARD_LEN)]
        self.plateStatus = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                            for y in range(self.BOARD_LEN)]
        self.availableLocation = []
        self.createBoard()
        self.objectNameActivate()

        self.btn_1.clicked.connect(self.gameStart)
        self.btn_2.clicked.connect(self.close)  # TO-DO : Game Init
        self.btn_3.clicked.connect(self.close)

    def printTime(self):
        self.remainTime -= 1
        self.lcdNumber.display(self.remainTime)

    def gameOver(self):
        black, white = self.cell_count()
        if white < black:
            QMessageBox.information(
                self, "GAME OVER", "WHITE WIN \n" + "White = " + str(white) + "\nBlack = " + str(black))
        elif black < white:
            QMessageBox.information(
                self, "GAME OVER", "BLACK WIN\n" + "Black = " + str(black) + "\nWhite = " + str(white))
        else:
            QMessageBox.information(self, "GAME OVER", "DRAW")

    def gameStart(self):
        if self.radioButton_2.isChecked():
            self.gameType = 'Together'
        self.playStrategy = self.comboBox.currentIndex()

        timerVar = QTimer(self)
        timerVar.setInterval(1000)
        timerVar.timeout.connect(self.printTime)
        timerVar.start()

        if self.gameType is 'Alone':
            self.initGame()
            self.findavailable()
        elif self.gameType is 'Together':
            self.serverConnectClicked()

        self.showMarker()

    def serverConnectClicked(self):
        dialog = ServerConnectDialog()
        dialog.exec_()
        serverIp = dialog.ip
        serverPort = int(dialog.port)

        # connect server
        self.othelloLib = Othello(serverIp, serverPort)
        self.othelloLib.start()
        print(f'print boardStr : {self.othelloLib.board}')
        self.str_to_board(self.othelloLib.board)
        self.label_5.setText("ip: %s port: %s" % (serverIp, serverPort))

        # Create Thread
        showMarkerTh = threading.Thread(target=self.showMarker)
        showMarkerTh.start()
        clientTurnTh = threading.Thread(target=self.clientTurn)
        clientTurnTh.start()

    def clientTurn(self):
        while True:  # 흠...
            code, data = self.othelloLib.wait_for_turn()
            if code == 'end':
                print_board(str_to_board(data['board']))
                print("status: " + data['status'] + ' score: ' + data['score'])
                self.gameOver()
                os._exit(1)
                break  # if not use while, move to another func
            elif code == 'turn':
                self.availableLocation = []
                self.str_to_board(self.othelloLib.board)
                print_board(str_to_board(self.othelloLib.board))
                print('available: ' + data['available'])
                getAvailable = data['available'].split()
                for i in getAvailable:
                    xyTuple = convert_1A_to_ij(i)
                    self.availableLocation.append([xyTuple[0], xyTuple[1]])

                th = threading.Thread(target=self.showMarker)
                th.start()

                if self.playStrategy:  # default : Human(0) / AI(1)
                    self.clickedByAI()

    def str_to_board(self, board_str):
        l = 0
        #board = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)] for y in range(self.BOARD_LEN)]
        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                self.plateStatus[i][j] = board_str[l]
                l += 1

        return self.plateStatus

    def initGame(self):
        self.plateStatus[3][3] = self.WHITE_CELL
        self.plateStatus[4][4] = self.WHITE_CELL
        self.plateStatus[3][4] = self.BLACK_CELL
        self.plateStatus[4][3] = self.BLACK_CELL

    def objectNameActivate(self):
        # fix error using lambda (TypeError: argument 1 has unexpected type 'NoneType')
        self.plate[0][0].clicked.connect(
            lambda: self.clickedButton(self.plate[0][0]))
        self.plate[0][1].clicked.connect(
            lambda: self.clickedButton(self.plate[0][1]))
        self.plate[0][2].clicked.connect(
            lambda: self.clickedButton(self.plate[0][2]))
        self.plate[0][3].clicked.connect(
            lambda: self.clickedButton(self.plate[0][3]))
        self.plate[0][4].clicked.connect(
            lambda: self.clickedButton(self.plate[0][4]))
        self.plate[0][5].clicked.connect(
            lambda: self.clickedButton(self.plate[0][5]))
        self.plate[0][6].clicked.connect(
            lambda: self.clickedButton(self.plate[0][6]))
        self.plate[0][7].clicked.connect(
            lambda: self.clickedButton(self.plate[0][7]))
        self.plate[1][0].clicked.connect(
            lambda: self.clickedButton(self.plate[1][0]))
        self.plate[1][1].clicked.connect(
            lambda: self.clickedButton(self.plate[1][1]))
        self.plate[1][2].clicked.connect(
            lambda: self.clickedButton(self.plate[1][2]))
        self.plate[1][3].clicked.connect(
            lambda: self.clickedButton(self.plate[1][3]))
        self.plate[1][4].clicked.connect(
            lambda: self.clickedButton(self.plate[1][4]))
        self.plate[1][5].clicked.connect(
            lambda: self.clickedButton(self.plate[1][5]))
        self.plate[1][6].clicked.connect(
            lambda: self.clickedButton(self.plate[1][6]))
        self.plate[1][7].clicked.connect(
            lambda: self.clickedButton(self.plate[1][7]))
        self.plate[2][0].clicked.connect(
            lambda: self.clickedButton(self.plate[2][0]))
        self.plate[2][1].clicked.connect(
            lambda: self.clickedButton(self.plate[2][1]))
        self.plate[2][2].clicked.connect(
            lambda: self.clickedButton(self.plate[2][2]))
        self.plate[2][3].clicked.connect(
            lambda: self.clickedButton(self.plate[2][3]))
        self.plate[2][4].clicked.connect(
            lambda: self.clickedButton(self.plate[2][4]))
        self.plate[2][5].clicked.connect(
            lambda: self.clickedButton(self.plate[2][5]))
        self.plate[2][6].clicked.connect(
            lambda: self.clickedButton(self.plate[2][6]))
        self.plate[2][7].clicked.connect(
            lambda: self.clickedButton(self.plate[2][7]))
        self.plate[3][0].clicked.connect(
            lambda: self.clickedButton(self.plate[3][0]))
        self.plate[3][1].clicked.connect(
            lambda: self.clickedButton(self.plate[3][1]))
        self.plate[3][2].clicked.connect(
            lambda: self.clickedButton(self.plate[3][2]))
        self.plate[3][3].clicked.connect(
            lambda: self.clickedButton(self.plate[3][3]))
        self.plate[3][4].clicked.connect(
            lambda: self.clickedButton(self.plate[3][4]))
        self.plate[3][5].clicked.connect(
            lambda: self.clickedButton(self.plate[3][5]))
        self.plate[3][6].clicked.connect(
            lambda: self.clickedButton(self.plate[3][6]))
        self.plate[3][7].clicked.connect(
            lambda: self.clickedButton(self.plate[3][7]))
        self.plate[4][0].clicked.connect(
            lambda: self.clickedButton(self.plate[4][0]))
        self.plate[4][1].clicked.connect(
            lambda: self.clickedButton(self.plate[4][1]))
        self.plate[4][2].clicked.connect(
            lambda: self.clickedButton(self.plate[4][2]))
        self.plate[4][3].clicked.connect(
            lambda: self.clickedButton(self.plate[4][3]))
        self.plate[4][4].clicked.connect(
            lambda: self.clickedButton(self.plate[4][4]))
        self.plate[4][5].clicked.connect(
            lambda: self.clickedButton(self.plate[4][5]))
        self.plate[4][6].clicked.connect(
            lambda: self.clickedButton(self.plate[4][6]))
        self.plate[4][7].clicked.connect(
            lambda: self.clickedButton(self.plate[4][7]))
        self.plate[5][0].clicked.connect(
            lambda: self.clickedButton(self.plate[5][0]))
        self.plate[5][1].clicked.connect(
            lambda: self.clickedButton(self.plate[5][1]))
        self.plate[5][2].clicked.connect(
            lambda: self.clickedButton(self.plate[5][2]))
        self.plate[5][3].clicked.connect(
            lambda: self.clickedButton(self.plate[5][3]))
        self.plate[5][4].clicked.connect(
            lambda: self.clickedButton(self.plate[5][4]))
        self.plate[5][5].clicked.connect(
            lambda: self.clickedButton(self.plate[5][5]))
        self.plate[5][6].clicked.connect(
            lambda: self.clickedButton(self.plate[5][6]))
        self.plate[5][7].clicked.connect(
            lambda: self.clickedButton(self.plate[5][7]))
        self.plate[6][0].clicked.connect(
            lambda: self.clickedButton(self.plate[6][0]))
        self.plate[6][1].clicked.connect(
            lambda: self.clickedButton(self.plate[6][1]))
        self.plate[6][2].clicked.connect(
            lambda: self.clickedButton(self.plate[6][2]))
        self.plate[6][3].clicked.connect(
            lambda: self.clickedButton(self.plate[6][3]))
        self.plate[6][4].clicked.connect(
            lambda: self.clickedButton(self.plate[6][4]))
        self.plate[6][5].clicked.connect(
            lambda: self.clickedButton(self.plate[6][5]))
        self.plate[6][6].clicked.connect(
            lambda: self.clickedButton(self.plate[6][6]))
        self.plate[6][7].clicked.connect(
            lambda: self.clickedButton(self.plate[6][7]))
        self.plate[7][0].clicked.connect(
            lambda: self.clickedButton(self.plate[7][0]))
        self.plate[7][1].clicked.connect(
            lambda: self.clickedButton(self.plate[7][1]))
        self.plate[7][2].clicked.connect(
            lambda: self.clickedButton(self.plate[7][2]))
        self.plate[7][3].clicked.connect(
            lambda: self.clickedButton(self.plate[7][3]))
        self.plate[7][4].clicked.connect(
            lambda: self.clickedButton(self.plate[7][4]))
        self.plate[7][5].clicked.connect(
            lambda: self.clickedButton(self.plate[7][5]))
        self.plate[7][6].clicked.connect(
            lambda: self.clickedButton(self.plate[7][6]))
        self.plate[7][7].clicked.connect(
            lambda: self.clickedButton(self.plate[7][7]))

    def cell_count(self):
        self.remainTime = 15

        white = 0
        black = 0

        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.WHITE_CELL:
                    white += 1
                elif self.plateStatus[i][j] == self.BLACK_CELL:
                    black += 1

        self.lcdNumber_2.display(black)
        self.lcdNumber_3.display(white)

        return black, white

    # TO-DO, Give a clear range of conditions
    def findavailable(self):
        self.availableLocation = []

        self.TURN += 1
        print(f'check turn num : {self.TURN}')

        if self.TURN is 3:
            print('!! Game Over !!')
            self.gameOver()
            os._exit(1)

        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                if self.plateStatus[i][j] == self.MY_CELL:
                    for k in range(8):
                        x, y = i, j
                        cur_x = x+self.dx[k]
                        cur_y = y+self.dy[k]
                        # If the edge meets, cur_x or cur_y is negative.
                        if self.BOARD_LEN > cur_x >= 0 and self.BOARD_LEN > cur_y >= 0:
                            # (i, j)를 기준으로 상하좌우 대각선을 dx, dy로 점검
                            while(self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.OP_CELL):
                                x = x + self.dx[k]
                                y = y + self.dy[k]
                                if self.BOARD_LEN > x+self.dx[k] >= 0 and self.BOARD_LEN > y+self.dy[k] >= 0:
                                    continue
                                else:
                                    break

                            # 2줄 밑 경계값 검사
                            if not (self.BOARD_LEN > x+self.dx[k] >= 0 and self.BOARD_LEN > y+self.dy[k] >= 0):
                                break

                            if self.BOARD_LEN > cur_x >= 0 and self.BOARD_LEN > cur_y >= 0:
                                if x == i and y == j:
                                    continue
                                elif self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.MY_CELL:
                                    continue
                                elif self.plateStatus[x+self.dx[k]][y+self.dy[k]] == self.EMPTY_CELL:
                                    cur_x = x+self.dx[k]
                                    cur_y = y+self.dy[k]
                                    # If the edge meets, cur_x or cur_y is negative.
                                    if self.BOARD_LEN > cur_x >= 0 and self.BOARD_LEN > cur_y >= 0:
                                        self.availableLocation.append(
                                            [cur_x, cur_y])

        # When no point is available, turn the turn or end the game.
        if len(self.availableLocation) is 0:
            self.TURN += 1  # print(f'check turn num : {self.TURN}')
            if self.TURN is 3:
                print('No point is available')
                self.gameOver()
                self.close()

            black, white = self.cell_count()
            total = black + white

            if total is 64:
                print('game end')
                self.gameOver()
                self.close()
            else:
                print('pass turn')
                return 1

        return 0

    def clearAvailableLoc(self):
        print('removing...')
        for i in range(len(self.availableLocation)):
            x = self.availableLocation[i][0]
            y = self.availableLocation[i][1]
            print(x, y)
            self.plate[x][y].setIcon(QIcon())

    def clickedByComputer(self):
        self.TURN -= 1
        print(f'check turn num : {self.TURN}')
        minimax = Minimax()
        getCell = minimax.calc(self.availableLocation)

        x = int(getCell[0])
        y = int(getCell[1])

        self.plate[x][y].setEnabled(False)

        for i in range(8):
            self.plateStatus[x][y] = self.OP_CELL
            self.updateBoard(x, y, i)

        self.plateStatus[x][y] = self.MY_CELL
        # For Debug
        # print(self.plateStatus)
        # self.printBoard()

        self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL  # turn swap
        print(f'현재 차례 {self.MY_CELL}, 상대방 :{self.OP_CELL}')
        checkTurn = self.findavailable()  # using play alone

        self.showMarker()

        if checkTurn is 1:  # print('client nothing to do')
            self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL
            self.findavailable()
            self.showMarker()

    def clickedByAI(self):
        minimax = Minimax()
        getCell = minimax.calc(self.availableLocation)

        x = int(getCell[0])
        y = int(getCell[1])

        self.plate[x][y].setEnabled(False)

        setMove = convert_ij_to_1A(x, y)
        self.othelloLib.move(setMove)

        th = threading.Thread(target=self.showMarker)   # self.showMarker()
        th.start()

    def clickedButton(self, btn):
        self.clearAvailableLoc()  # Delete Image
        position = btn.objectName()  # type(position) => <class 'str'>
        print(f'position : {position}')
        x = int(position[0])
        y = int(position[1])

        if self.gameType is 'Alone':
            self.plate[x][y].setEnabled(False)

            for i in range(8):
                self.plateStatus[x][y] = self.OP_CELL
                self.updateBoard(x, y, i)

            self.plateStatus[x][y] = self.MY_CELL
            self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL  # turn swap

            checkTurn = self.findavailable()

            if checkTurn is 1:
                print('computer nothing to do')
                self.MY_CELL, self.OP_CELL = self.OP_CELL, self.MY_CELL  # turn swap
                self.TURN -= 1
                print(f'check turn num : {self.TURN}')
            else:
                self.TURN -= 1
                print(f'check turn num : {self.TURN}')
                if self.playStrategy:
                    self.clickedByComputer()

            self.showMarker()

        elif self.gameType is 'Together':
            setMove = convert_ij_to_1A(x, y)
            print(setMove)
            self.othelloLib.move(setMove)

    def updateBoard(self, x, y, direction):
        if self.plateStatus[x][y] == self.MY_CELL:
            print(self.MY_CELL, self.OP_CELL)
            # print(f'{self.MY_CELL} found! x : {x} y : {y} and direction is {direction}') # For Debug
            return 1
        elif self.plateStatus[x][y] == self.EMPTY_CELL:
            return 0

        cur_x = x
        cur_y = y
        cur_x = cur_x + self.dx[direction]
        cur_y = cur_y + self.dy[direction]

        if self.BOARD_LEN > cur_x >= 0 and self.BOARD_LEN > cur_y >= 0:
            tmp = self.updateBoard(cur_x, cur_y, direction)
            #print(f'check2@ cur_x : {cur_x} cur_y : {cur_y} direction : {direction}')
            if tmp:
                self.plateStatus[x][y] = self.MY_CELL
                print(self.plateStatus)
                return 1

        return 0

    def showMarker(self):
        print('enter in the showMarker')
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

        print(self.availableLocation)
        for i in range(len(self.availableLocation)):
            x = self.availableLocation[i][0]
            y = self.availableLocation[i][1]
            self.plate[x][y].setIcon(QIcon("./image/Othello icon.png"))
            self.plate[x][y].setIconSize(QSize(20, 20))
            # available Button Activate
            if self.playStrategy is 0:
                self.plate[x][y].setEnabled(True)

        self.cell_count()

    def initUI(self):
        self.setWindowTitle('Reverse Othello')
        self.setWindowIcon(QIcon('./image/Othello icon.png'))
        self.center()

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
                self.plate[i][j].setEnabled(False)
                self.plate[i][j].setStyleSheet("background-color: teal")

    # For Debug Function
    # def printBoard(self):
    #     for i in range(self.BOARD_LEN):
    #         for j in range(self.BOARD_LEN):
    #             print(self.plateStatus[j][i], end='')
    #         print()


class ServerConnectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.ip = None
        self.port = None

    def setupUI(self):
        self.setWindowTitle("Server Connect ...")

        label1 = QLabel("IP Address ")
        label2 = QLabel("Port ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1 = QPushButton("Connect")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.ip = self.lineEdit1.text()
        self.port = self.lineEdit2.text()
        self.close()


if __name__ == '__main__':
    # QApplication : program start class
    app = QApplication(sys.argv)
    myWindow = CreateGame()  # Create Reverse_Othello instance
    myWindow.show()
    # Enters the program into the event loop (running the program)
    app.exec_()
