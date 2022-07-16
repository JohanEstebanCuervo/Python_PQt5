
################################
# librerias para algoritmos de reproducción
################################

from API.Flea3Cam_API import *
from API.ColorReproduction_API import *
from API.Core_App import *

from Body.Barra_Principal import *
from Body.Menu import *
from Body.Stacked_Pages import *

################################
# Librerias PyQt
################################

from PyQt5 import QtCore, QtWidgets, uic

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QDir, QTimer

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QStatusBar
class AMILI_App(QtWidgets.QMainWindow):

    """docstring for Multiespectral_App"""

    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(1000, 721)
        self.setStyleSheet(u"QPushButton{\n"
                           "border:0px\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QLabel{\n"
                           "font: 9pt \"Microsoft Sans Serif\";\n"
                           "}\n"
                           "\n"
                           "QMainWindow{\n"
                           "background-color: rgb(161, 187, 215);\n"
                           "}")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(161, 187, 215);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Core_App = Core_App(self)
        self.Stacked_Pages = Stacked_Pages(self)
        self.Menu = Menu(self)
        self.Barra_Principal = Barra_Principal(self)

        self.verticalLayout.addWidget(self.Barra_Principal)


        self.Ventana_Principal = QFrame(self.centralwidget)
        self.Ventana_Principal.setObjectName(u"Ventana_Principal")
        self.Ventana_Principal.setStyleSheet(u"QFrame{\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "}")

        self.Ventana_Principal.setFrameShape(QFrame.StyledPanel)
        self.Ventana_Principal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Ventana_Principal)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.Menu)

        self.lb_desplegar_menu = QLabel(self.Ventana_Principal)
        self.lb_desplegar_menu.setObjectName(u"lb_desplegar_menu")
        self.lb_desplegar_menu.setMinimumSize(QSize(10, 0))
        self.lb_desplegar_menu.setMaximumSize(QSize(10, 16777215))
        self.lb_desplegar_menu.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";\n"
                                             "background-color: rgb(255, 255, 255);\n"
                                             "")
        self.lb_desplegar_menu.setScaledContents(True)
        self.lb_desplegar_menu.setText('<')
        self.lb_desplegar_menu.mousePressEvent = self.desplegar_menu

        self.horizontalLayout_2.addWidget(self.lb_desplegar_menu)

        self.horizontalLayout_2.addWidget(self.Stacked_Pages)


        self.verticalLayout.addWidget(self.Ventana_Principal)

        self.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(self)
        self.statusBar.setObjectName(u"statusBar")
        self.setStatusBar(self.statusBar)


    def desplegar_menu(self, event):

        if self.lb_desplegar_menu.text() == '<':
            self.Menu.hide()
            self.lb_desplegar_menu.setText('>')

        else:
            self.Menu.show()
            self.lb_desplegar_menu.setText('<')


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    mi_app = AMILI_App()
    mi_app.show()
    app.exit(app.exec_())
