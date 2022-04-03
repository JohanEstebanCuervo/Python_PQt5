from PyQt5 import QtWidgets , uic

class Miapp:
	"""docstring for Miapp"""
	def __init__(self):

		self.__inicio = uic.loadUi("Ventana_inicio.ui")
		self.__acceso = uic.loadUi("Ventana_acceso.ui")


		##################
		# botton connect
		##################
		self.__inicio.pushButton_ingresar.clicked.connect(self.gui_login)
		self.__inicio.pushButton_SALIR.clicked.connect(self.gui_exit)
		self.__inicio.pushButton_limpiar.clicked.connect(self.gui_clean)
		self.__inicio.Lineedit_Password.returnPressed.connect(self.gui_login)

		self.config_specials()

		self.__inicio.pushButton_limpiar.hide()
		self.__inicio.Lineedit_Password.cursorPosition()
		self.__inicio.show()

	def gui_login(self):

		name = self.__inicio.Lineedit_User.text()

		Password = self.__inicio.Lineedit_Password.text()

		if len(name)==0 or len(Password)==0:
			self.__inicio.label_error.setText("Ingresar datos completos")
			self.__inicio.pushButton_limpiar.show()

		elif name=='Johan' and Password =='2906':

			self.gui_entrar()

		else:
			self.__inicio.label_error.setText(".I. Chupela")

	def gui_entrar(self):

		self.__inicio.hide()
		self.__acceso.show()

	def gui_exit(self):
		self.__inicio.close()

	def gui_clean(self):
		self.__inicio.Lineedit_User.setText("")
		self.__inicio.Lineedit_Password.setText("")
		self.__inicio.label_error.setText("")


	def config_specials(self):

		self.__inicio.Lineedit_User.setClearButtonEnabled(True)
		self.__inicio.Lineedit_Password.setClearButtonEnabled(True)


if __name__=='__main__':
	app = QtWidgets.QApplication([])
	Miapp_1 = Miapp()

	app.exec_()
