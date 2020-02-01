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

        self.BOARD_LEN = 8
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.plate = [[self.EMPTY_CELL for x in range(self.BOARD_LEN)]
                      for y in range(self.BOARD_LEN)]
        # self.initGame()

        self.createBoard()

    def initGame(self):

        self.plates[3][3] = self.WHITE_CELL
        self.plates[4][4] = self.WHITE_CELL
        self.plates[3][4] = self.BLACK_CELL
        self.plates[4][3] = self.BLACK_CELL

    def initUI(self):

        self.setWindowTitle('Reverse Othello')
        self.setWindowIcon(QIcon('./image/Othello icon.png'))
        self.center()
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createBoard(self):
        for i in range(self.BOARD_LEN):
            for j in range(self.BOARD_LEN):
                self.plate[i][j] = QPushButton("", self)
                self.plate[i][j].move(60, 60)
                self.plate[i][j].resize(60, 60)


# class Reversi(CreateGame):

#     def __init__(self):
#         super().__init__()
#         self.showMarker()

#     def showMarker(self):

#         if self.plates[3][4] is self.BLACK_CELL:
#             self.plateq_34.setIcon(QIcon("./image/black.png"))
#             self.plate_34.setIconSize(QSize(50, 50))


if __name__ == '__main__':
    # QApplication : program start class
    app = QApplication(sys.argv)
    myWindow = CreateGame()  # create ReverseOthello instance
    myWindow.show()
    # myWindow2 = Reversi()  # create Reversi instance
    # myWindow2.show()
    # Enters the program into the event loop (running the program)
    app.exec_()
