from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Barra_Principal(QFrame):

    """docstring for Barra_Principal"""

    def __init__(self, App):
        super(Barra_Principal, self).__init__(App)
        self.App = App

        self.Structe_Barra()
        self.Names_Barra()

        # mover ventana
        self.mouseMoveEvent = self.mover_ventana

        self.Control_Buttons()

    def Structe_Barra(self):
        self.setObjectName(u"Barra_Principal")
        self.setMinimumSize(QSize(0, 30))
        self.setMaximumSize(QSize(16777215, 30))
        self.setStyleSheet(u"QFrame{\n"
                            "background-color: rgb(161, 187, 215);\n"
                            "}\n"
                            "\n"
                            "\n"
                            "QPushButton{\n"
                            "background-color: rgb(161, 187, 215);\n"
                            "   \n"
                            "}\n"
                            "\n"
                            "QPushButton:hover{\n"
                            "background-color:  rgb(204, 204, 204);\n"
                            "}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.LayoutH_principal = QHBoxLayout(self)
        self.LayoutH_principal.setSpacing(5)
        self.LayoutH_principal.setObjectName(u"LayoutH_principal")
        self.LayoutH_principal.setContentsMargins(0, 0, 0, 0)
        self.lb_name_window = QLabel(self)
        self.lb_name_window.setObjectName(u"lb_name_window")
        self.lb_name_window.setMinimumSize(QSize(0, 30))
        self.lb_name_window.setMaximumSize(QSize(16777215, 30))
        self.lb_name_window.setAlignment(Qt.AlignCenter)

        self.LayoutH_principal.addWidget(self.lb_name_window)

        self.pb_error_conection_corona = QPushButton(self)
        self.pb_error_conection_corona.setObjectName(u"pb_error_conection_corona")
        self.pb_error_conection_corona.setMinimumSize(QSize(20, 20))
        self.pb_error_conection_corona.setMaximumSize(QSize(20, 20))
        self.pb_error_conection_corona.setStyleSheet(u"border-radius: 10px;\n"
                                                      "background-color: rgb(255, 0, 0);")
        self.pb_error_conection_corona.setIconSize(QSize(30, 30))

        self.LayoutH_principal.addWidget(self.pb_error_conection_corona)

        self.lb_error_conection_corona = QLabel(self)
        self.lb_error_conection_corona.setObjectName(u"lb_error_conection_corona")
        self.lb_error_conection_corona.setMinimumSize(QSize(0, 30))
        self.lb_error_conection_corona.setMaximumSize(QSize(16777215, 30))

        self.LayoutH_principal.addWidget(self.lb_error_conection_corona)

        self.pb_error_conection_camera = QPushButton(self)
        self.pb_error_conection_camera.setObjectName(u"pb_error_conection_camera")
        self.pb_error_conection_camera.setMinimumSize(QSize(20, 20))
        self.pb_error_conection_camera.setMaximumSize(QSize(20, 20))
        self.pb_error_conection_camera.setStyleSheet(u"border-radius: 10px;\n"
                                                      "background-color: rgb(255, 0, 0);")
        self.pb_error_conection_camera.setIconSize(QSize(30, 30))

        self.LayoutH_principal.addWidget(self.pb_error_conection_camera)

        self.lb_error_conection_camera = QLabel(self)
        self.lb_error_conection_camera.setObjectName(u"lb_error_conection_camera")
        self.lb_error_conection_camera.setMinimumSize(QSize(0, 30))
        self.lb_error_conection_camera.setMaximumSize(QSize(16777215, 30))

        self.LayoutH_principal.addWidget(self.lb_error_conection_camera)

        self.spacer_bar = QSpacerItem(784, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayoutH_principal.addItem(self.spacer_bar)

        self.pb_minimum = QPushButton(self)
        self.pb_minimum.setObjectName(u"pb_minimum")
        self.pb_minimum.setMinimumSize(QSize(30, 30))
        self.pb_minimum.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"iconos/minimium.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_minimum.setIcon(icon)
        self.pb_minimum.setIconSize(QSize(25, 25))

        self.LayoutH_principal.addWidget(self.pb_minimum)

        self.pb_normal = QPushButton(self)
        self.pb_normal.setObjectName(u"pb_normal")
        self.pb_normal.setMinimumSize(QSize(30, 30))
        self.pb_normal.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"iconos/minimum2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_normal.setIcon(icon1)
        self.pb_normal.setIconSize(QSize(25, 25))

        self.LayoutH_principal.addWidget(self.pb_normal)

        self.pb_maximum = QPushButton(self)
        self.pb_maximum.setObjectName(u"pb_maximum")
        self.pb_maximum.setMinimumSize(QSize(30, 30))
        self.pb_maximum.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"iconos/maximum.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_maximum.setIcon(icon2)
        self.pb_maximum.setIconSize(QSize(25, 25))

        self.LayoutH_principal.addWidget(self.pb_maximum)

        self.pb_exit = QPushButton(self)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setMinimumSize(QSize(30, 30))
        self.pb_exit.setMaximumSize(QSize(30, 30))
        self.pb_exit.setStyleSheet(u"QPushButton:hover{\n"
                                    "background-color: red;\n"
                                    "\n"
                                    "}")
        icon3 = QIcon()
        icon3.addFile(u"iconos/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_exit.setIcon(icon3)
        self.pb_exit.setIconSize(QSize(25, 25))

        self.LayoutH_principal.addWidget(self.pb_exit)

    def Names_Barra(self):

        self.lb_name_window.setText('AMILI')

    def Control_Buttons(self):

        self.pb_minimum.clicked.connect(self.control_pb_minimum)
        self.pb_normal.clicked.connect(self.control_pb_normal)
        self.pb_maximum.clicked.connect(self.control_pb_maximum)
        self.pb_exit.clicked.connect(self.exit_app)
        self.pb_normal.hide()

    def mousePressEvent(self, event):

        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.App.isMaximized() is False:
            if event.buttons() == Qt.LeftButton:
                self.App.move(self.App.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <= 20:
            self.App.showMaximized()
            self.pb_maximum.hide()
            self.pb_normal.show()
        else:
            self.App.showNormal()
            self.pb_normal.hide()
            self.pb_maximum.show()

    def control_pb_minimum(self):

        self.App.showMinimized()

    def control_pb_normal(self):
        self.App.showNormal()
        self.pb_normal.hide()
        self.pb_maximum.show()

    def control_pb_maximum(self):
        self.App.showMaximized()
        self.pb_maximum.hide()
        self.pb_normal.show()

    def exit_app(self):

        #if self.camera_init:

        #    del self.camera

        #if self.corona_init:

        #    del self.corona

        self.App.close()
