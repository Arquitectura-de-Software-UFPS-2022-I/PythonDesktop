from PyQt5 import QtWidgets,uic
#iniciar la aplicacion
app= QtWidgets.QApplication([])

#Caragar Los archivos .uic
login= uic.loadUi("ViewLogin.ui")

#ejecutable
login.show()
app.exec_()
