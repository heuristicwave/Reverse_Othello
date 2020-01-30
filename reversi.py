import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QAction, QWidget, QDesktopWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox, QHBoxLayout, QLabel, QPushButton, QColorDialog, qApp, QTextBrowser

square = []


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Using Reversi Class
        self.content = Reversi()
        self.setCentralWidget(self.content)

        self.initMW()

    def initMW(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("background-color: lightgray;"
                              "color: black")
        filemenu1 = menubar.addMenu("Setting")
        filemenu2 = menubar.addMenu("About")

        setting = QAction("Setting", self)
        setting.setStatusTip("Game Option Setting")
        filemenu1.addAction(setting)

        github = QAction("Github", self)
        github.triggered.connect(self.openUrl)
        github.setStatusTip("Click To Connect Github")
        filemenu2.addAction(github)

        exitAct = QAction("Quit", self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Click to quit")
        exitAct.triggered.connect(qApp.quit)
        filemenu2.addAction(exitAct)

        self.statusBar()
        self.setStyleSheet("background-color: lightgray")
        self.center()
        self.setFixedSize(900, 600)
        self.setWindowTitle('Reverse Othello')
        self.setWindowIcon(QIcon('./image/Othello icon.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openUrl(self):
        url = QUrl("https://github.com/heuristicwave/Reverse_Othello")
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Url Open Error')


class Reversi(QWidget):

    def __init__(self):
        super().__init__()

        self.initGrapic()

    def initGrapic(self):
        #plates = QColor(10, 138, 65)

        positionInRow = QHBoxLayout()

        self.gameBoard = QLabel()
        self.gameInfo = QLabel()
        positionInRow.addWidget(self.gameBoard)
        positionInRow.addWidget(self.gameInfo)

        self.gameBoard.resize(500, 500)
        self.gameBoard.setMinimumWidth(500)
        self.gameInfo.setMinimumWidth(200)

        self.setLayout(positionInRow)

        self.gameBoard.setStyleSheet("background-color: seagreen")
        self.gameInfo.setStyleSheet("background-color: yellowgreen")

        self.board()

    def board(self):
        self.plates = [[] for i in range(8)]

        for i in square:
            for j in square:
                self.plates[i][j] = QPushButton(self.gameBoard)
                self.plates[i][j].resize(60, 60)
                self.plates[i][j].setStyleSheet("border-color: gray")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gm = MainWindow()
    sys.exit(app.exec_())
