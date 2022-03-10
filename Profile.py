from Profile_ui import *

class ProfileWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.textEdit_4.setText(self.user.full_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ProfileWindow()
    window.show()
    app.exec_()