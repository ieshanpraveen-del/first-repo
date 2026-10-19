import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import re


class Ui_RegisterScreen(object):
    
    def existing_user_error(self):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Username already exists.')
        error_dialog.exec_()

    def register_success(self):
                sucess_dialog = QtWidgets.QMessageBox()
                sucess_dialog.setText('Register Successful!')
                sucess_dialog.exec_()

    def register_database(self):
            conn = sqlite3.connect("login.db") # accesses the database
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS login (username TEXT PRIMARY KEY, password TEXT)")
            
            try:
                 def username_validation():
                     username = self.UsernameEntry.text()
                     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-+]).{5,20}$"

                     if not re.match(pattern, username):
                         username_error = QtWidgets.QErrorMessage()
                         username_error.showMessage('Username must be 5-20 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*()-+).  ')
                         username_error.exec_()

                         return False
                     else:
                         return True

                 def password_validation():
                     password = self.PasswordEntry.text()
                     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-+]).{5,20}$"

                     if not re.match(pattern, password):
                         password_error = QtWidgets.QErrorMessage()
                         password_error.showMessage('Password must be 5-20 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*()-+).')
                         password_error.exec_()

                         return False
                     else:
                         return True

                 if not username_validation() or not password_validation():
                     return

                 username_validation()
                 password_validation()

                 password_hash = hashlib.sha256(self.PasswordEntry.text().encode()).hexdigest()
                 cur.execute("INSERT INTO login (username, password) VALUES (?, ?)", (self.UsernameEntry.text(), password_hash)) #inserts the username and password entered
                 conn.commit()
                 self.register_success()

            except sqlite3.IntegrityError:
                self.existing_user_error()

    def setupUi(self, RegisterScreen):
        RegisterScreen.setObjectName("RegisterScreen")
        RegisterScreen.resize(577, 600)
        RegisterScreen.setStyleSheet("background-color: rgb(81, 81, 81)")
        self.centralwidget = QtWidgets.QWidget(RegisterScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 181, 81))
        self.label.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(50, 170, 91, 31))
        self.UsernameLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.UsernameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.UsernameEntry.setGeometry(QtCore.QRect(160, 170, 291, 41))
        self.UsernameEntry.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.UsernameEntry.setText("")
        self.UsernameEntry.setObjectName("UsernameEntry")
        self.PasswordEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEntry.setGeometry(QtCore.QRect(160, 250, 291, 41))
        self.PasswordEntry.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.PasswordEntry.setText("")
        self.PasswordEntry.setObjectName("PasswordEntry")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(50, 250, 80, 31))
        self.PasswordLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.ResigterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.register_database())
        self.ResigterButton.setGeometry(QtCore.QRect(300, 330, 151, 41))
        self.ResigterButton.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.ResigterButton.setObjectName("ResigterButton")
        RegisterScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 26))
        self.menubar.setObjectName("menubar")
        RegisterScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterScreen)
        self.statusbar.setObjectName("statusbar")
        RegisterScreen.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterScreen)
        QtCore.QMetaObject.connectSlotsByName(RegisterScreen)

    def retranslateUi(self, RegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        RegisterScreen.setWindowTitle(_translate("RegisterScreen", "MainWindow"))
        self.label.setText(_translate("RegisterScreen", "Register"))
        self.UsernameLabel.setText(_translate("RegisterScreen", "Username"))
        self.PasswordLabel.setText(_translate("RegisterScreen", "Password"))
        self.ResigterButton.setText(_translate("RegisterScreen", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterScreen = QtWidgets.QMainWindow()
    ui = Ui_RegisterScreen()
    ui.setupUi(RegisterScreen)
    RegisterScreen.show()
    sys.exit(app.exec_())
