from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainApp(QMainWindow):
	"""docstring for MainApp"""
	def __init__(self, parent=None,*args):
		super(MainApp, self).__init__(parent=parent)
		
		self.setMinimumSize(640,480)
		self.setMaximumSize(1920,1080)

		self.setWindowTitle("ESTA ES MI APP")

		label = QLabel("Que mierda es un Label",self)
		#label.setGeometry(0,0,self.frameGeometry().width(),self.frameGeometry().height()//2)
		label.setStyleSheet("background:#424242; color:#fff")

		self.setCentralWidget(label)
		# setMiniumSize()
		# setMaximunSize()
		#setFixedSize













if __name__ == '__main__':

	app = QApplication([])  #Obligatorio solo llamarse una vez en el programa
	window = MainApp()
	window.show()
	app.exec_() #Para mantener un while





