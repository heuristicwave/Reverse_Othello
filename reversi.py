from PyQt5.QtGui import QColor, QFont
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QAction, QWidget, QDesktopWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox, QHBoxLayout, QLabel, QPushButton, QColorDialog, qApp, QTextBrowser

square = [0, 60, 120, 180, 240, 300, 36, 42]


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
        self.setFixedSize(800, 600)
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
        plates = QColor(10, 138, 65)

        positionInRow = QHBoxLayout()

        self.gameBoard = QLabel()
        self.gameInfo = QLabel()
        positionInRow.addWidget(self.gameBoard)
        positionInRow.addWidget(self.gameInfo)

        self.gameBoard.resize(500, 500)
        self.gameBoard.setMinimumWidth(400)
        self.gameInfo.setMinimumWidth(200)

        self.setLayout(positionInRow)

        self.board()

    def board(self):
        self.plates = [[] for i in range(8)]
        self.buttons = [[] for i in range(8)]

        # m = 0
        # n = 0
        # for i in square:
        #     for j in square:
        #         self.buttons[m][n] = QPushButton(self.labelBoard)
        #         self.buttons[m][n].resize(60, 60)
        #         self.buttons[m][n].move(*(j, i))
        #         self.buttons[m][n].setStyleSheet("""border-style: outset;
        #                                       border-width: 5px;
        #                                       border-radius: 4px;
        #                                       border-color: gray
        #                                       """)
        #         if (m, n) == (3, 4) or (m, n) == (4, 3):
        #             self.buttons[m][n].setIcon(QIcon("black.png"))
        #             self.buttons[m][n].setIconSize(QSize(48, 48))
        #         elif (m, n) == (3, 3) or (m, n) == (4, 4):
        #             self.buttons[m][n].setIcon(QIcon("white.png"))
        #             self.buttons[m][n].setIconSize(QSize(48, 48))
        #         else:
        #             self.zeroColTab.append((j, i))
        #         tableCoords.append((j, i))
        #         self.buttons[m][n].clicked.connect(self.reverse)
        #         if n == 7:
        #             m += 1
        #             n = -1
        #         n += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gm = MainWindow()
    sys.exit(app.exec_())
