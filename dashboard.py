import imp
from dashboard_ui import *
from Profile import ProfileWindow

class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.commandLinkButton_2.clicked.connect(self.profile_view)

    
    def profile_view(self):
        # self.hide()
        print(self.user)
        self.profile = ProfileWindow(self)
        self.profile.user = self.user
        self.profile.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DashboardWindow() 
    window.show()
    app.exec_()