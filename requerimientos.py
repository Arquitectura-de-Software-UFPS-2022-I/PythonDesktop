from PyQt5 import QtWidgets,uic
#iniciar la aplicacion
app= QtWidgets.QApplication([])

#Cargar Los archivos .uic
login= uic.loadUi("ViewLogin.ui")

#desativar boton activar
login.btnIniciarSesion.setEnabled(False)

#test
#ejecutable
login.show()
app.exec_()
