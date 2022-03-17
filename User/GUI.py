import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set Application Title
        self.setWindowTitle('Rocket Stocks')

        #Create Default Window Size
        self.setMinimumSize(500,500)

        #create Window Widgets
        self.createWidgets()

    def createWidgets(self):
        pass


    def clickSettings(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
