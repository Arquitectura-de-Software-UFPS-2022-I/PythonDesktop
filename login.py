from login_ui import *
from register import RegisterWindow

class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.commandLinkButton.clicked.connect(self.register_view)

    def register_view(self):
        self.register = RegisterWindow()
        self.register.show()
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()