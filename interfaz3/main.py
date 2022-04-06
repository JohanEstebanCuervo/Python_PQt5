################################
# librerias para algoritmos de reproducción
################################

import subprocess
from clases_VM import *
import Funciones_Adquisicion as Fun_Ad
################################
# Librerias PyQt
################################

from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect,
                          QAbstractAnimation, QTranslator, QLocale, QLibraryInfo,QTimer)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox,
                             QFrame, QLabel, QFileDialog)


class Multiespectral_App(QtWidgets.QMainWindow):
	
	"""docstring for Multiespectral_App"""
	def __init__(self):
		super().__init__()

		uic.loadUi("Interfaz_grafica.ui",self)

		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)


	##########################################
	# timer para actualizacion del boton
	##########################################

		self.timer =QTimer()
		self.timer.timeout.connect(self.check_connection)
		self.timer.start(4000)


	##########################################
	# Configuracion de botones y funciones de ventana
	##########################################

		# mover ventana
		self.fm_barra.mouseMoveEvent = self.mover_ventana

		#control barra de titulos
		self.pb_minimum.clicked.connect(self.control_pb_minimum)		
		self.pb_normal.clicked.connect(self.control_pb_normal)
		self.pb_maximum.clicked.connect(self.control_pb_maximum)
		self.pb_exit.clicked.connect(lambda: self.close())
		self.pb_normal.hide()

		#desplegar menu
		self.lb_desplegar_menu.mousePressEvent = self.desplegar_menu


		#botones de menu
		self.pb_menu_capture.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_capture))
		self.pb_menu_camera.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_camera))
		self.pb_menu_corona.clicked.connect(self.control_pb_menu_corona)
		self.pb_menu_colorReproduction.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_colorReproduction))
		self.pb_menu_settings.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_settings))


		#botones settings corona

		self.pb_init_corona.clicked.connect(self.control_pb_init_corona)
		self.pb_sc_leds.clicked.connect(self.control_pb_sc_leds)
		self.pb_sc_PWMleds.clicked.connect(self.control_pb_sc_PWMleds)

	##########################################
	# Ocultar ventanas que no se van a mostrar en el inicio
	##########################################

		self.fm_leds.hide()
		self.fm_PWM.hide()


	#########################################
	# Variables Propias de App para control
	#########################################

		self.corona_init = False

	#########################################
	# Funciones de ventanas 
	#########################################

	def check_connection(self):

		if self.corona_init:
			self.pb_error_conection.setStyleSheet("background-color : green; border-radius: 10px")
			self.lb_error_conection.setText("")
			ports = Fun_Ad.Serial_Port_Select(terminal=False)
			bandera=0
			if ports != 1:
				for port in ports:
					if(port== self.lb_sc_port.text()):
						bandera=1
						break

			if bandera==0:
				self.corona_init=False
				self.pb_error_conection.setStyleSheet("background-color : red; border-radius: 10px")
				self.lb_error_conection.setText("Corona desconectada")
				self.fm_init_corona.show()
				self.fm_settings_corona.hide()


	def mousePressEvent(self, event):

		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()

	def control_pb_minimum(self):

		self.showMinimized()		

	def  control_pb_normal(self): 
		self.showNormal()		
		self.pb_normal.hide()
		self.pb_maximum.show()

	def  control_pb_maximum(self): 
		self.showMaximized()
		self.pb_maximum.hide()
		self.pb_normal.show()

	def desplegar_menu(self,event):

		if self.lb_desplegar_menu.text()=='<':
			self.fm_menu.hide()
			self.lb_desplegar_menu.setText('>')

		else:
			self.fm_menu.show()
			self.lb_desplegar_menu.setText('<')

	def control_pb_menu_corona(self):
		if self.corona_init:

			self.fm_settings_corona.show()
			self.fm_init_corona.hide()


		else:
			self.fm_settings_corona.hide()
			self.fm_init_corona.show()

			self.cb_listPort.clear()
			list_ports = Fun_Ad.Serial_Port_Select(terminal=False)
			if list_ports!=1:
				self.cb_listPort.addItems(list_ports)


		self.stackedWidget.setCurrentWidget(self.page_corona)

	#################################
	# Control buttons settings corona
	#################################

	def control_pb_init_corona(self):

		puerto = self.cb_listPort.currentText()
		try:
			self.corona = Corona_Multiespectral(puerto,time_sleep_c=1e-2)
			if self.corona.get_comunication_state():
				

				self.cb_buttons_checked("U")

				self.le_PWM_led_checked("U")
				self.lb_sc_port.setText(puerto)

				self.le_timeSleepc.setText(str(self.corona.get_time_sleepc()))

				self.le_shotMessage.setText(str(self.corona.get_shot_message()))

				self.le_timeTrigger.setText(str(self.corona.get_shot_time_trigger()))

				self.le_timeOut.setText(str(self.corona.get_shot_time_out()))

				self.le_shotMode.setText(str(self.corona.get_shot_mode()))

				self.le_timeFlash.setText(str(self.corona.get_shot_time_flash()))

#Adquisition Multispectral Interfaz Leds Ilumination

				self.fm_init_corona.hide()
				self.fm_settings_corona.show()
				self.corona_init = True
				self.lb_init_c_error.setText("")

		except:
				self.lb_init_c_error.setText("No se ha podido iniciar la corona")



	def cb_buttons_checked(self,action):

		if action == 'U':
			for led in self.corona.get_leds():

				if led[2] == '1':
					self.cb_led_1.setChecked(True)


				elif led[2] == '2':
					self.cb_led_2.setChecked(True)

				elif led[2] == '3':
					self.cb_led_3.setChecked(True)

				elif led[2] == '4':
					self.cb_led_4.setChecked(True)

				elif led[2] == '5':
					self.cb_led_5.setChecked(True)

				if led[2] == '6':
					self.cb_led_6.setChecked(True)

				if led[2] == '7':
					self.cb_led_7.setChecked(True)

				if led[2] == '8':
					self.cb_led_8.setChecked(True)

				if led[2] == '9':
					self.cb_led_9.setChecked(True)

				if led[2] == 'A':
					self.cb_led_10.setChecked(True)

				if led[2] == 'B':
					self.cb_led_11.setChecked(True)

				if led[2] == 'C':
					self.cb_led_12.setChecked(True)

				if led[2] == 'D':
					self.cb_led_13.setChecked(True)

				if led[2] == 'E':
					self.cb_led_14.setChecked(True)

				if led[2] == 'F':
					self.cb_led_15.setChecked(True)



		if action == 'G':

			lista_leds = []

			if self.cb_led_1.isChecked():

				lista_leds.append('M01N')

			if self.cb_led_2.isChecked():

				lista_leds.append('M02N')

			if self.cb_led_3.isChecked():

				lista_leds.append('M03N')

			if self.cb_led_4.isChecked():

				lista_leds.append('M04N')

			if self.cb_led_5.isChecked():

				lista_leds.append('M05N')

			if self.cb_led_6.isChecked():

				lista_leds.append('M06N')

			if self.cb_led_7.isChecked():

				lista_leds.append('M07N')

			if self.cb_led_8.isChecked():

				lista_leds.append('M08N')

			if self.cb_led_9.isChecked():

				lista_leds.append('M09N')

			if self.cb_led_10.isChecked():

				lista_leds.append('M0AN')

			if self.cb_led_11.isChecked():

				lista_leds.append('M0BN')

			if self.cb_led_12.isChecked():

				lista_leds.append('M0CN')

			if self.cb_led_13.isChecked():

				lista_leds.append('M0DN')

			if self.cb_led_14.isChecked():

				lista_leds.append('M0EN')

			if self.cb_led_15.isChecked():

				lista_leds.append('M0FN')

			return lista_leds


	def le_PWM_led_checked(self,action):

		if action == 'U':
			for led in self.corona.get_PWM_leds():

				if led[1] == '1':
					self.le_PWM_led_1.setText(led[2:5])


				elif led[1] == '2':
					self.le_PWM_led_2.setText(led[2:5])

				elif led[1] == '3':
					self.le_PWM_led_3.setText(led[2:5])

				elif led[1] == '4':
					self.le_PWM_led_4.setText(led[2:5])

				elif led[1] == '5':
					self.le_PWM_led_5.setText(led[2:5])

				elif led[1] == '6':
					self.le_PWM_led_6.setText(led[2:5])

				elif led[1] == '7':
					self.le_PWM_led_7.setText(led[2:5])

				elif led[1] == '8':
					self.le_PWM_led_8.setText(led[2:5])

				elif led[1] == '9':
					self.le_PWM_led_9.setText(led[2:5])

				elif led[1] == 'A':
					self.le_PWM_led_10.setText(led[2:5])

				elif led[1] == 'B':
					self.le_PWM_led_11.setText(led[2:5])

				elif led[1] == 'C':
					self.le_PWM_led_12.setText(led[2:5])

				elif led[1] == 'D':
					self.le_PWM_led_13.setText(led[2:5])

				elif led[1] == 'E':
					self.le_PWM_led_14.setText(led[2:5])

				elif led[1] == 'F':
					self.le_PWM_led_15.setText(led[2:5])



		if action == 'G':

			lista_PWM_leds = []

			if self.cb_led_1.isChecked():

				lista_PWM_leds.append('J1'+self.le_PWM_led_1+'K')

			if self.cb_led_2.isChecked():

				lista_PWM_leds.append('J2'+self.le_PWM_led_2+'K')

			if self.cb_led_3.isChecked():

				lista_PWM_leds.append('J3'+self.le_PWM_led_3+'K')

			if self.cb_led_4.isChecked():

				lista_PWM_leds.append('J4'+self.le_PWM_led_4+'K')

			if self.cb_led_5.isChecked():

				lista_PWM_leds.append('J5'+self.le_PWM_led_5+'K')

			if self.cb_led_6.isChecked():

				lista_PWM_leds.append('J6'+self.le_PWM_led_6+'K')

			if self.cb_led_7.isChecked():

				lista_PWM_leds.append('J7'+self.le_PWM_led_7+'K')

			if self.cb_led_8.isChecked():

				lista_PWM_leds.append('J8'+self.le_PWM_led_8+'K')

			if self.cb_led_9.isChecked():

				lista_PWM_leds.append('J9'+self.le_PWM_led_9+'K')

			if self.cb_led_10.isChecked():

				lista_PWM_leds.append('JA'+self.le_PWM_led_A+'K')

			if self.cb_led_11.isChecked():

				lista_PWM_leds.append('JB'+self.le_PWM_led_B+'K')

			if self.cb_led_12.isChecked():

				lista_PWM_leds.append('JC'+self.le_PWM_led_C+'K')

			if self.cb_led_13.isChecked():

				lista_PWM_leds.append('JD'+self.le_PWM_led_D+'K')

			if self.cb_led_14.isChecked():

				lista_PWM_leds.append('JE'+self.le_PWM_led_E+'K')

			if self.cb_led_15.isChecked():

				lista_PWM_leds.append('JF'+self.le_PWM_led_F+'K')

			return lista_PWM_leds

	def control_pb_sc_leds(self):

		self.fm_leds.show()
		self.fm_PWM.hide()

	def control_pb_sc_PWMleds(self):

		self.fm_leds.hide()
		self.fm_PWM.show()

		self.fm_PWM_led_hs()

	def fm_PWM_led_hs(self):

		if self.cb_led_1.isChecked():
			self.fm_PWM_led_1.show()
		else:
			self.fm_PWM_led_1.hide()

		if self.cb_led_2.isChecked():
			self.fm_PWM_led_2.show()
		else:
			self.fm_PWM_led_2.hide()

		if self.cb_led_3.isChecked():
			self.fm_PWM_led_3.show()
		else:
			self.fm_PWM_led_3.hide()

		if self.cb_led_4.isChecked():
			self.fm_PWM_led_4.show()
		else:
			self.fm_PWM_led_4.hide()

		if self.cb_led_5.isChecked():
			self.fm_PWM_led_5.show()
		else:
			self.fm_PWM_led_5.hide()

		if self.cb_led_6.isChecked():
			self.fm_PWM_led_6.show()
		else:
			self.fm_PWM_led_6.hide()

		if self.cb_led_7.isChecked():
			self.fm_PWM_led_7.show()
		else:
			self.fm_PWM_led_7.hide()

		if self.cb_led_8.isChecked():
			self.fm_PWM_led_8.show()
		else:
			self.fm_PWM_led_8.hide()

		if self.cb_led_9.isChecked():
			self.fm_PWM_led_9.show()
		else:
			self.fm_PWM_led_9.hide()

		if self.cb_led_10.isChecked():
			self.fm_PWM_led_10.show()
		else:
			self.fm_PWM_led_10.hide()

		if self.cb_led_12.isChecked():
			self.fm_PWM_led_12.show()
		else:
			self.fm_PWM_led_12.hide()

		if self.cb_led_13.isChecked():
			self.fm_PWM_led_13.show()
		else:
			self.fm_PWM_led_13.hide()

		if self.cb_led_14.isChecked():
			self.fm_PWM_led_14.show()
		else:
			self.fm_PWM_led_14.hide()

		if self.cb_led_15.isChecked():
			self.fm_PWM_led_15.show()
		else:
			self.fm_PWM_led_15.hide()



if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	mi_app = Multiespectral_App()
	mi_app.show()
	app.exit(app.exec_())	
