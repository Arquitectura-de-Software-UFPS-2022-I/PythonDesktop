import imp
from dashboard_ui import *

class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DashboardWindow() 
    window.show()
    app.exec_()