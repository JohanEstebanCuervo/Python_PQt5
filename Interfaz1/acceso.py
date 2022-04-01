from PyQt5 import QtWidgets , uic

app = QtWidgets.QApplication([])

inicio = uic.loadUi("Ventana_inicio.ui")

acceso = uic.loadUi("Ventana_acceso.ui")

def gui_login():

	name = inicio.Lineedit_User.text()

	Password = inicio.Lineedit_Password.text()

	if len(name)==0 or len(Password)==0:
		inicio.label_error.setText("Ingresar datos completos")

	elif name=='Johan' and Password =='2906':

		gui_entrar()

	else:
		inicio.label_error.setText(".I. Chupela")

def gui_entrar():

	inicio.hide()
	acceso.show()

def gui_exit():
	app.exit()

def gui_clean():
	inicio.Lineedit_User.setText("")
	inicio.Lineedit_Password.setText("")
	inicio.label_error.setText("")

#bottom

inicio.pushButton_ingresar.clicked.connect(gui_login)
inicio.pushButton_SALIR.clicked.connect(gui_exit)
inicio.pushButton_limpiar.clicked.connect(gui_clean)

inicio.show()
app.exec_()
