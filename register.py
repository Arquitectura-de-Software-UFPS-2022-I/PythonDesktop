from register_ui import *

class RegisterWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    
        self.pushButton_2.clicked.connect(self.login_view)

    def login_view(self):
        self.parent().show()
        self.close()
       # self.login.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = RegisterWindow()
    window.show()
    app.exec_()