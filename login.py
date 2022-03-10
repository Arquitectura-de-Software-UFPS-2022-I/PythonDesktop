from login_ui import *
from register import RegisterWindow
from dashboard import DashboardWindow
from signaturelib import services

class LoginWindow(QtWidgets.QMainWindow, LoginMainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.commandLinkButton.clicked.connect(self.register_view)
        self.pushButton.clicked.connect(self.login)

    def register_view(self):
        self.hide()
        self.register = RegisterWindow(self)
        self.register.show()
        
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        user = services.get_user_login(username, password)
        if user:
            self.dashboard = DashboardWindow(self)
            self.dashboard.user = user
            self.dashboard.show()
            self.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()