from PyQt5 import QtCore, QtGui, QtWidgets
from Player_table import PlayerTable
from Optimiser import Ui_OptimiserScreen


class Ui_MainScreen(object):
    
    def OpenPlayerTable(self):
        self.window = PlayerTable()
        self.window.show()

    def OpenOptimiser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OptimiserScreen()
        self.ui.setupUi(self.window)
        self.window.show()
               
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(800, 600)
        MainScreen.setStyleSheet("background-color: rgb(81, 81, 81)")
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 661, 71))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.OpenPlayerTable()) #Button to open the player table
        self.pushButton.setGeometry(QtCore.QRect(270, 220, 211, 51))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.OpenOptimiser()) #Button to open the optimiser screen
        self.pushButton_2.setGeometry(QtCore.QRect(270, 340, 211, 51))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        MainScreen.setStatusBar(self.statusbar)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "MainWindow"))
        self.label.setText(_translate("MainScreen", "Welcome to the NBA Draft Optimiser"))
        self.pushButton.setText(_translate("MainScreen", "Player List"))
        self.pushButton_2.setText(_translate("MainScreen", "Optimiser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())