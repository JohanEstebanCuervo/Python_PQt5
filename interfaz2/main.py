# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
#from menu import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect,
                          QAbstractAnimation, QTranslator, QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox,
                             QFrame, QLabel, QFileDialog)

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		#self.ui = Ui_MainWindow() 
		#self.ui.setupUi(self)

		uic.loadUi("menu.ui",self)
		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		self.parent = None

		self.bt_anterior.setObjectName("Siguiente")
		self.bt_siguiente.setObjectName("Anterior")
		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana

		#acceder a las paginas
		#self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio)
		self.bt_cargar.clicked.connect(self.Cargar)			
		self.bt_eliminar.clicked.connect(self.Eliminar)
		self.bt_siguiente.clicked.connect(self.anteriorSiguiente)	
		self.bt_anterior.clicked.connect(self.anteriorSiguiente)
		self.bt_configurar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_configuracion))			
		self.bt_cinco.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_configuracion))	

		#control barra de titulos
		self.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
		self.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.bt_cerrar.clicked.connect(lambda: self.close())

		self.bt_restaurar.hide()

		#menu lateral
		self.bt_menu.clicked.connect(self.mover_menu)

		#self.label_Imagen.setScaledContents(True)

		framePrincipal = QFrame(self)
		framePrincipal.setFrameShape(QFrame.Box)
		framePrincipal.setFrameShadow(QFrame.Sunken)
		framePrincipal.setAutoFillBackground(True)
		framePrincipal.setBackgroundRole(QPalette.Light)
		framePrincipal.setMinimumSize(662, 503)
		framePrincipal.move(10, 10)
		framePrincipal.hide()
		frame = QFrame(framePrincipal)
		frame.setMinimumSize(640, 480)
		frame.move(10, 10)

		#self.labelImagen = QLabel(frame)
		#self.labelImagen.setAlignment(Qt.AlignCenter)
		#self.labelImagen.setGeometry(0, 0, 640, 480)
		#self.labelImagen.setScaledContents(True)

		self.labelImagenUno = QLabel(frame)
		self.labelImagenUno.setAlignment(Qt.AlignCenter)
		self.labelImagenUno.setGeometry(-650, 0, 640, 480)
		self.labelImagenUno.hide()

	###############################################
	# Funciones para botones de la ventana
	###############################################

	def control_bt_minimizar(self):

		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.bt_restaurar.hide()
		self.bt_maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.bt_maximizar.hide()
		self.bt_restaurar.show()

	def mover_menu(self):
		if True:			
			width = self.frame_lateral.width()
			if width==0:
				extender = 200
			else:
				extender = 0
			self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
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


	###############################################
	# Funciones para cargar imagenes 
	###############################################

	def bloquearBotones(self, bool):
	   self.bt_cargar.setEnabled(bool)
	   self.bt_eliminar.setEnabled(bool)
	   self.bt_restaurar.setEnabled(bool)
	   self.bt_maximizar.setEnabled(bool)
	   self.bt_menu.setEnabled(bool)
	   self.bt_anterior.setEnabled(bool)
	   self.bt_siguiente.setEnabled(bool)


	def Mostrar (self, label, imagen, nombre, posicionX=650):
	   imagen = QPixmap.fromImage(imagen)

	   # Escalar imagen a 640x480 si el ancho es mayor a 640 o el alto mayor a 480
	   if imagen.width() > label.width() or imagen.height() > label.height():
	       imagen = imagen.scaled(label.width(),label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

	   # Mostrar imagen
	   label.setPixmap(imagen)
	   label.setAlignment(QtCore.Qt.AlignCenter)
	   # Animación (al finalizar la animación se muestra en la barra de estado el nombre y la extensión de la imagen
	   # y se desbloquean los botones).       
	   self.animacionMostar = QPropertyAnimation(label, b"geometry")
	   #self.animacionMostar.finished.connect(lambda: (self.parent.statusBar.showMessage(nombre),
	   #                                               self.bloquearBotones(True)))
	   self.bloquearBotones(True)
	   self.animacionMostar.setDuration(200)
	   self.animacionMostar.setStartValue(QRect(posicionX, 0, 640, 480))
	   self.animacionMostar.setEndValue(QRect(0, 0, 640, 480))
	   self.animacionMostar.start(QAbstractAnimation.DeleteWhenStopped)

	def Limpiar(self, labelConImagen, labelMostrarImagen, imagen, nombre,
	           posicionInternaX, posicionX=None):

	   def Continuar(estado):
	       if estado:
	           if posicionX:
	               self.Mostrar(labelMostrarImagen, imagen, nombre, posicionX)
	           else:
	               self.Mostrar(labelMostrarImagen, imagen, nombre)
	       
	   self.animacionLimpiar = QPropertyAnimation(labelConImagen, b"geometry")
	   self.animacionLimpiar.finished.connect(lambda: labelConImagen.clear())
	   self.animacionLimpiar.setDuration(200)
	   # self.animacionLimpiar.valueChanged.connect(lambda x: print(x))
	   self.animacionLimpiar.stateChanged.connect(Continuar)
	   self.animacionLimpiar.setStartValue(QRect(0, 0, 640, 480))
	   self.animacionLimpiar.setEndValue(QRect(posicionInternaX, 0, 640, 480))
	   self.animacionLimpiar.start(QAbstractAnimation.DeleteWhenStopped)

	def Cargar(self):

		self.stackedWidget.setCurrentWidget(self.page_inicio)
		   
		nombreImagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen",
		                                       QDir.currentPath(),
		                                       "Archivos de imagen (*.jpg *.png *.ico *.bmp)")

		if nombreImagen:
		# Verificar que QLabel tiene imagen
			labelConImagen = ""
		if self.label_Imagen.pixmap():
			labelConImagen = self.label_Imagen
		elif self.labelImagenUno.pixmap():
			labelConImagen = self.labelImagenUno
		 
		imagen = QImage(nombreImagen)
		if imagen.isNull():
			if labelConImagen:
				self.Eliminar()

			QMessageBox.information(self, "Visor de imágenes",
			                    "No se puede cargar %s." % nombreImagen)
			return

		# Obtener ruta de la carpeta que contiene la imagen seleccionada
		self.carpetaActual = QDir(QFileInfo(nombreImagen).absoluteDir().path())

		# Obtener la ruta y el nombre de las imagenes que se encuentren en la carpeta de
		# la imagen seleccionada
		imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
		                                         QDir.Files, QDir.Name)
		self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

		self.posicion = self.imagenesCarpeta.index(nombreImagen)
		self.estadoAnterior = True if self.posicion == 0 else False
		self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False

		# Función encargada de bloquear o desbloquear los botones
		self.bloquearBotones(False)

		# Nombre y extensión de la imagen
		nombre = QFileInfo(nombreImagen).fileName()

		if labelConImagen:
		 posicionInternaX = -650
		 labelMostrarImagen = self.label_Imagen if self.labelImagenUno.pixmap() else self.labelImagenUno
		 self.Limpiar(labelConImagen, labelMostrarImagen, imagen, nombre, posicionInternaX)
		else:
		 self.Mostrar(self.label_Imagen, imagen, nombre)




	def Eliminar(self):
	   def establecerValores():
	       labelConImagen.clear()
	       labelConImagen.move(0, 0)

	       # Limpiar la barra de estado
	       #self.parent.statusBar.clearMessage()

	       # Establecer los valores predeterminados
	       self.posicion = int
	       self.estadoAnterior, self.estadoSiguiente = False, False
	       self.carpetaActual = QDir()
	       self.imagenesCarpeta.clear()

	       self.bloquearBotones(True)
	       
	   # Verificar que QLabel tiene imagen
	   labelConImagen = ""
	   if self.label_Imagen.pixmap():
	       labelConImagen = self.label_Imagen
	   elif self.labelImagenUno.pixmap():
	       labelConImagen = self.labelImagenUno
	           
	   if labelConImagen:
	       self.bloquearBotones(False)
	       
	       self.animacionEliminar = QPropertyAnimation(labelConImagen, b"geometry")
	       self.animacionEliminar.finished.connect(establecerValores)
	       self.animacionEliminar.setDuration(200)
	       self.animacionEliminar.setStartValue(QRect(0, 0, 640, 480))
	       self.animacionEliminar.setEndValue(QRect(-650, 0, 640, 480))
	       self.animacionEliminar.start(QAbstractAnimation.DeleteWhenStopped)

	def anteriorSiguiente(self):
	   if self.imagenesCarpeta:

	       widget = self.sender().objectName()
	       
	       if widget == "Anterior":
	           self.estadoAnterior = True if self.posicion == 0 else False
	           self.estadoSiguiente = False
	               
	           self.posicion -= 1 if self.posicion > 0 else 0
	           posicionInternaX, posicionX = 650, -650 
	       else:
	           self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False
	           self.estadoAnterior = False
	               
	           self.posicion += 1 if self.posicion < len(self.imagenesCarpeta)-1 else 0
	           posicionInternaX, posicionX = -650, 650 

	       if self.estadoAnterior or self.estadoSiguiente:
	           return
	       else:
	           imagen = self.imagenesCarpeta[self.posicion]

	           # Verificar que la carpeta que contiene la imagene exista
	           if not QDir(self.carpetaActual).exists():
	               self.Eliminar()
	               return
	           elif not QFile.exists(imagen):
	               # Obtener la ruta y el nombre de las imagenes que se encuentren en la
	               # carpeta de la imagen seleccionada
	               imagenes = self.carpetaActual.entryInfoList(["*.jpg", "*.png", "*.ico", "*.bmp"],
	                                                           QDir.Files, QDir.Name)

	               if not imagenes:
	                   self.Eliminar()
	                   return
	               
	               self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in imagenes]

	               self.posicion = randint(0, len(self.imagenesCarpeta)-1)
	               self.estadoAnterior = True if self.posicion == 0 else False
	               self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False
	           elif QImage(imagen).isNull():
	               del self.imagenesCarpeta[self.posicion]

	               if not self.imagenesCarpeta:
	                   self.Eliminar()
	                   return

	               self.posicion = randint(0, len(self.imagenesCarpeta)-1)
	               self.estadoAnterior = True if self.posicion == 0 else False
	               self.estadoSiguiente = True if self.posicion == len(self.imagenesCarpeta)-1 else False

	           imagen = self.imagenesCarpeta[self.posicion]

	           if self.label_Imagen.pixmap():
	               labelConImagen = self.label_Imagen
	           elif self.labelImagenUno.pixmap():
	               labelConImagen = self.labelImagenUno

	           # Función encargada de bloquear o desbloquear los botones
	           self.bloquearBotones(False)

	           # Nombre y extensión de la imagen
	           nombre = QFileInfo(imagen).fileName()

	           # Label en el que se va a mostrar la imagen
	           labelMostrarImagen = self.label_Imagen if self.labelImagenUno.pixmap() else self.labelImagenUno

	           # Quitar la imagen actual y mostrar la siguiente
	           self.Limpiar(labelConImagen, labelMostrarImagen, QImage(imagen),
	                        nombre, posicionInternaX, posicionX)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	


