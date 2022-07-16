# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz_graficaHonIUM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 721)
        MainWindow.setStyleSheet(u"QPushButton{\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(161, 187, 215);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fm_barra = QFrame(self.centralwidget)
        self.fm_barra.setObjectName(u"fm_barra")
        self.fm_barra.setMinimumSize(QSize(0, 30))
        self.fm_barra.setMaximumSize(QSize(16777215, 30))
        self.fm_barra.setStyleSheet(u"QFrame{\n"
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
        self.fm_barra.setFrameShape(QFrame.StyledPanel)
        self.fm_barra.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fm_barra)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_name_window = QLabel(self.fm_barra)
        self.lb_name_window.setObjectName(u"lb_name_window")
        self.lb_name_window.setMinimumSize(QSize(0, 30))
        self.lb_name_window.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.lb_name_window)

        self.pb_error_conection_corona = QPushButton(self.fm_barra)
        self.pb_error_conection_corona.setObjectName(u"pb_error_conection_corona")
        self.pb_error_conection_corona.setMinimumSize(QSize(20, 20))
        self.pb_error_conection_corona.setMaximumSize(QSize(20, 20))
        self.pb_error_conection_corona.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.pb_error_conection_corona.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pb_error_conection_corona)

        self.lb_error_conection_corona = QLabel(self.fm_barra)
        self.lb_error_conection_corona.setObjectName(u"lb_error_conection_corona")
        self.lb_error_conection_corona.setMinimumSize(QSize(0, 30))
        self.lb_error_conection_corona.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.lb_error_conection_corona)

        self.pb_error_conection_camera = QPushButton(self.fm_barra)
        self.pb_error_conection_camera.setObjectName(u"pb_error_conection_camera")
        self.pb_error_conection_camera.setMinimumSize(QSize(20, 20))
        self.pb_error_conection_camera.setMaximumSize(QSize(20, 20))
        self.pb_error_conection_camera.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);")
        self.pb_error_conection_camera.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pb_error_conection_camera)

        self.lb_error_conection_camera = QLabel(self.fm_barra)
        self.lb_error_conection_camera.setObjectName(u"lb_error_conection_camera")
        self.lb_error_conection_camera.setMinimumSize(QSize(0, 30))
        self.lb_error_conection_camera.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.lb_error_conection_camera)

        self.spacer_bar = QSpacerItem(784, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacer_bar)

        self.pb_minimum = QPushButton(self.fm_barra)
        self.pb_minimum.setObjectName(u"pb_minimum")
        self.pb_minimum.setMinimumSize(QSize(30, 30))
        self.pb_minimum.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"iconos/minimium.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_minimum.setIcon(icon)
        self.pb_minimum.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pb_minimum)

        self.pb_normal = QPushButton(self.fm_barra)
        self.pb_normal.setObjectName(u"pb_normal")
        self.pb_normal.setMinimumSize(QSize(30, 30))
        self.pb_normal.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"iconos/minimum2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_normal.setIcon(icon1)
        self.pb_normal.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pb_normal)

        self.pb_maximum = QPushButton(self.fm_barra)
        self.pb_maximum.setObjectName(u"pb_maximum")
        self.pb_maximum.setMinimumSize(QSize(30, 30))
        self.pb_maximum.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"iconos/maximum.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_maximum.setIcon(icon2)
        self.pb_maximum.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pb_maximum)

        self.pb_exit = QPushButton(self.fm_barra)
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

        self.horizontalLayout.addWidget(self.pb_exit)


        self.verticalLayout.addWidget(self.fm_barra)

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
        self.fm_menu = QFrame(self.Ventana_Principal)
        self.fm_menu.setObjectName(u"fm_menu")
        self.fm_menu.setMinimumSize(QSize(300, 0))
        self.fm_menu.setMaximumSize(QSize(300, 16777215))
        self.fm_menu.setStyleSheet(u"QFrame{\n"
"background-color: rgb(161, 187, 215);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"border:1px solid #000000;\n"
"background-color: rgb(161, 187, 215);\n"
"font: 75 12pt \"Arial Narrow\";\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"\n"
"}")
        self.fm_menu.setFrameShape(QFrame.StyledPanel)
        self.fm_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fm_menu)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_menu_capture = QPushButton(self.fm_menu)
        self.pb_menu_capture.setObjectName(u"pb_menu_capture")
        self.pb_menu_capture.setMinimumSize(QSize(0, 30))
        self.pb_menu_capture.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.pb_menu_capture)

        self.pb_menu_camera = QPushButton(self.fm_menu)
        self.pb_menu_camera.setObjectName(u"pb_menu_camera")
        self.pb_menu_camera.setMinimumSize(QSize(0, 30))
        self.pb_menu_camera.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.pb_menu_camera)

        self.pb_menu_corona = QPushButton(self.fm_menu)
        self.pb_menu_corona.setObjectName(u"pb_menu_corona")
        self.pb_menu_corona.setMinimumSize(QSize(0, 30))
        self.pb_menu_corona.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.pb_menu_corona)

        self.pb_menu_colorReproduction = QPushButton(self.fm_menu)
        self.pb_menu_colorReproduction.setObjectName(u"pb_menu_colorReproduction")
        self.pb_menu_colorReproduction.setMinimumSize(QSize(0, 30))
        self.pb_menu_colorReproduction.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.pb_menu_colorReproduction)

        self.pb_menu_settings = QPushButton(self.fm_menu)
        self.pb_menu_settings.setObjectName(u"pb_menu_settings")
        self.pb_menu_settings.setMinimumSize(QSize(0, 30))
        self.pb_menu_settings.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.pb_menu_settings)

        self.spacer_menu = QSpacerItem(20, 503, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_menu)


        self.horizontalLayout_2.addWidget(self.fm_menu)

        self.lb_desplegar_menu = QLabel(self.Ventana_Principal)
        self.lb_desplegar_menu.setObjectName(u"lb_desplegar_menu")
        self.lb_desplegar_menu.setMinimumSize(QSize(10, 0))
        self.lb_desplegar_menu.setMaximumSize(QSize(10, 16777215))
        self.lb_desplegar_menu.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";\n"
"background-color: rgb(232, 232, 232);\n"
"")
        self.lb_desplegar_menu.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.lb_desplegar_menu)

        self.stackedWidget = QStackedWidget(self.Ventana_Principal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_capture = QWidget()
        self.page_capture.setObjectName(u"page_capture")
        self.page_capture.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame{\n"
"background-color: rgb(161, 187, 215);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.page_capture)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fm_control_capture = QFrame(self.page_capture)
        self.fm_control_capture.setObjectName(u"fm_control_capture")
        self.fm_control_capture.setMinimumSize(QSize(0, 30))
        self.fm_control_capture.setMaximumSize(QSize(16777215, 30))
        self.fm_control_capture.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color: white;\n"
"   \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(204, 204, 204);\n"
"}")
        self.fm_control_capture.setFrameShape(QFrame.StyledPanel)
        self.fm_control_capture.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fm_control_capture)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pb_capture = QPushButton(self.fm_control_capture)
        self.pb_capture.setObjectName(u"pb_capture")
        self.pb_capture.setMinimumSize(QSize(30, 30))
        self.pb_capture.setMaximumSize(QSize(30, 30))
        self.pb_capture.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(0, 170, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"iconos/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_capture.setIcon(icon4)
        self.pb_capture.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_capture)

        self.pb_next_capture = QPushButton(self.fm_control_capture)
        self.pb_next_capture.setObjectName(u"pb_next_capture")
        self.pb_next_capture.setMinimumSize(QSize(30, 30))
        self.pb_next_capture.setMaximumSize(QSize(30, 30))
        self.pb_next_capture.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 255, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"iconos/after.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_next_capture.setIcon(icon5)
        self.pb_next_capture.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_next_capture)

        self.pb_after_capture = QPushButton(self.fm_control_capture)
        self.pb_after_capture.setObjectName(u"pb_after_capture")
        self.pb_after_capture.setMinimumSize(QSize(30, 30))
        self.pb_after_capture.setMaximumSize(QSize(30, 30))
        self.pb_after_capture.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(255, 255, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"iconos/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_after_capture.setIcon(icon6)
        self.pb_after_capture.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_after_capture)

        self.pb_save_capture = QPushButton(self.fm_control_capture)
        self.pb_save_capture.setObjectName(u"pb_save_capture")
        self.pb_save_capture.setMinimumSize(QSize(30, 30))
        self.pb_save_capture.setMaximumSize(QSize(30, 30))
        self.pb_save_capture.setStyleSheet(u"QPushButton:hover{\n"
"background-color:  rgb(170, 0, 127);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"iconos/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_capture.setIcon(icon7)
        self.pb_save_capture.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_save_capture)

        self.pb_clean_capture = QPushButton(self.fm_control_capture)
        self.pb_clean_capture.setObjectName(u"pb_clean_capture")
        self.pb_clean_capture.setMinimumSize(QSize(30, 30))
        self.pb_clean_capture.setMaximumSize(QSize(30, 30))
        self.pb_clean_capture.setStyleSheet(u"QPushButton:hover{\n"
"background-color:  rgb(255, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"iconos/stop2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_clean_capture.setIcon(icon8)
        self.pb_clean_capture.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pb_clean_capture)

        self.lb_wavelenth_capture = QLabel(self.fm_control_capture)
        self.lb_wavelenth_capture.setObjectName(u"lb_wavelenth_capture")

        self.horizontalLayout_4.addWidget(self.lb_wavelenth_capture)


        self.verticalLayout_3.addWidget(self.fm_control_capture)

        self.gv_Principal_imag = QGraphicsView(self.page_capture)
        self.gv_Principal_imag.setObjectName(u"gv_Principal_imag")
        self.gv_Principal_imag.setLayoutDirection(Qt.LeftToRight)
        self.gv_Principal_imag.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.gv_Principal_imag.setDragMode(QGraphicsView.ScrollHandDrag)

        self.verticalLayout_3.addWidget(self.gv_Principal_imag)

        self.fm_list_imag = QFrame(self.page_capture)
        self.fm_list_imag.setObjectName(u"fm_list_imag")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.fm_list_imag.sizePolicy().hasHeightForWidth())
        self.fm_list_imag.setSizePolicy(sizePolicy)
        self.fm_list_imag.setMaximumSize(QSize(16777215, 100))
        self.fm_list_imag.setFrameShape(QFrame.StyledPanel)
        self.fm_list_imag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fm_list_imag)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.lb_list_imag_1 = QLabel(self.fm_list_imag)
        self.lb_list_imag_1.setObjectName(u"lb_list_imag_1")
        self.lb_list_imag_1.setScaledContents(True)
        self.lb_list_imag_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_1)

        self.lb_list_imag_2 = QLabel(self.fm_list_imag)
        self.lb_list_imag_2.setObjectName(u"lb_list_imag_2")
        self.lb_list_imag_2.setScaledContents(True)
        self.lb_list_imag_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_2)

        self.lb_list_imag_3 = QLabel(self.fm_list_imag)
        self.lb_list_imag_3.setObjectName(u"lb_list_imag_3")
        self.lb_list_imag_3.setScaledContents(True)
        self.lb_list_imag_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_3)

        self.lb_list_imag_4 = QLabel(self.fm_list_imag)
        self.lb_list_imag_4.setObjectName(u"lb_list_imag_4")
        self.lb_list_imag_4.setScaledContents(True)
        self.lb_list_imag_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_4)

        self.lb_list_imag_5 = QLabel(self.fm_list_imag)
        self.lb_list_imag_5.setObjectName(u"lb_list_imag_5")
        self.lb_list_imag_5.setScaledContents(True)
        self.lb_list_imag_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_5)

        self.lb_list_imag_6 = QLabel(self.fm_list_imag)
        self.lb_list_imag_6.setObjectName(u"lb_list_imag_6")
        self.lb_list_imag_6.setScaledContents(True)
        self.lb_list_imag_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_6)

        self.lb_list_imag_7 = QLabel(self.fm_list_imag)
        self.lb_list_imag_7.setObjectName(u"lb_list_imag_7")
        self.lb_list_imag_7.setScaledContents(True)
        self.lb_list_imag_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_list_imag_7)


        self.verticalLayout_3.addWidget(self.fm_list_imag)

        self.verticalLayout_3.setStretch(2, 20)
        self.stackedWidget.addWidget(self.page_capture)
        self.page_colorReproduction = QWidget()
        self.page_colorReproduction.setObjectName(u"page_colorReproduction")
        self.label_7 = QLabel(self.page_colorReproduction)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 270, 55, 16))
        self.stackedWidget.addWidget(self.page_colorReproduction)
        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.verticalLayout_9 = QVBoxLayout(self.page_camera)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_title_page_sca = QLabel(self.page_camera)
        self.lb_title_page_sca.setObjectName(u"lb_title_page_sca")
        self.lb_title_page_sca.setMinimumSize(QSize(0, 80))
        self.lb_title_page_sca.setMaximumSize(QSize(16777215, 80))
        self.lb_title_page_sca.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")

        self.verticalLayout_9.addWidget(self.lb_title_page_sca)

        self.fm_settings_camera = QFrame(self.page_camera)
        self.fm_settings_camera.setObjectName(u"fm_settings_camera")
        self.fm_settings_camera.setFrameShape(QFrame.StyledPanel)
        self.fm_settings_camera.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.fm_settings_camera)
        self.horizontalLayout_25.setSpacing(3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.fm_buttons_sca = QFrame(self.fm_settings_camera)
        self.fm_buttons_sca.setObjectName(u"fm_buttons_sca")
        self.fm_buttons_sca.setFrameShape(QFrame.StyledPanel)
        self.fm_buttons_sca.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fm_buttons_sca)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_21 = QLabel(self.fm_buttons_sca)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 9, 0, 1, 1)

        self.label_19 = QLabel(self.fm_buttons_sca)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 11, 0, 1, 1)

        self.label_22 = QLabel(self.fm_buttons_sca)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 8, 0, 1, 1)

        self.label_13 = QLabel(self.fm_buttons_sca)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)

        self.label_6 = QLabel(self.fm_buttons_sca)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_3 = QLabel(self.fm_buttons_sca)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.le_gamma = QLineEdit(self.fm_buttons_sca)
        self.le_gamma.setObjectName(u"le_gamma")

        self.gridLayout_3.addWidget(self.le_gamma, 2, 1, 1, 1)

        self.le_blackLevel = QLineEdit(self.fm_buttons_sca)
        self.le_blackLevel.setObjectName(u"le_blackLevel")

        self.gridLayout_3.addWidget(self.le_blackLevel, 1, 1, 1, 1)

        self.label_14 = QLabel(self.fm_buttons_sca)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_16 = QLabel(self.fm_buttons_sca)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)

        self.le_gain = QLineEdit(self.fm_buttons_sca)
        self.le_gain.setObjectName(u"le_gain")

        self.gridLayout_3.addWidget(self.le_gain, 4, 1, 1, 1)

        self.label_15 = QLabel(self.fm_buttons_sca)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)

        self.le_sharpness = QLineEdit(self.fm_buttons_sca)
        self.le_sharpness.setObjectName(u"le_sharpness")

        self.gridLayout_3.addWidget(self.le_sharpness, 6, 1, 1, 1)

        self.label_17 = QLabel(self.fm_buttons_sca)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 5, 0, 1, 1)

        self.lb_sca_camera = QLabel(self.fm_buttons_sca)
        self.lb_sca_camera.setObjectName(u"lb_sca_camera")

        self.gridLayout_3.addWidget(self.lb_sca_camera, 0, 1, 1, 1)

        self.label_18 = QLabel(self.fm_buttons_sca)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 7, 0, 1, 1)

        self.label_20 = QLabel(self.fm_buttons_sca)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 10, 0, 1, 1)

        self.label_23 = QLabel(self.fm_buttons_sca)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 12, 0, 1, 1)

        self.le_exposure = QLineEdit(self.fm_buttons_sca)
        self.le_exposure.setObjectName(u"le_exposure")

        self.gridLayout_3.addWidget(self.le_exposure, 8, 1, 1, 1)

        self.le_bufferMode = QLineEdit(self.fm_buttons_sca)
        self.le_bufferMode.setObjectName(u"le_bufferMode")

        self.gridLayout_3.addWidget(self.le_bufferMode, 10, 1, 1, 1)

        self.le_bufferCount = QLineEdit(self.fm_buttons_sca)
        self.le_bufferCount.setObjectName(u"le_bufferCount")

        self.gridLayout_3.addWidget(self.le_bufferCount, 11, 1, 1, 1)

        self.le_bufferHandlingMode = QLineEdit(self.fm_buttons_sca)
        self.le_bufferHandlingMode.setObjectName(u"le_bufferHandlingMode")

        self.gridLayout_3.addWidget(self.le_bufferHandlingMode, 12, 1, 1, 1)

        self.cb_gainAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_gainAuto.setObjectName(u"cb_gainAuto")

        self.gridLayout_3.addWidget(self.cb_gainAuto, 3, 1, 1, 1)

        self.cb_sharpnessAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_sharpnessAuto.setObjectName(u"cb_sharpnessAuto")

        self.gridLayout_3.addWidget(self.cb_sharpnessAuto, 5, 1, 1, 1)

        self.cb_exposureAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_exposureAuto.setObjectName(u"cb_exposureAuto")

        self.gridLayout_3.addWidget(self.cb_exposureAuto, 7, 1, 1, 1)

        self.cb_triggerMode = QCheckBox(self.fm_buttons_sca)
        self.cb_triggerMode.setObjectName(u"cb_triggerMode")

        self.gridLayout_3.addWidget(self.cb_triggerMode, 9, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.pb_sca_configuration = QPushButton(self.fm_buttons_sca)
        self.pb_sca_configuration.setObjectName(u"pb_sca_configuration")

        self.verticalLayout_8.addWidget(self.pb_sca_configuration)


        self.horizontalLayout_25.addWidget(self.fm_buttons_sca)


        self.verticalLayout_9.addWidget(self.fm_settings_camera)

        self.fm_init_camera = QFrame(self.page_camera)
        self.fm_init_camera.setObjectName(u"fm_init_camera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.fm_init_camera.sizePolicy().hasHeightForWidth())
        self.fm_init_camera.setSizePolicy(sizePolicy1)
        self.fm_init_camera.setFrameShape(QFrame.StyledPanel)
        self.fm_init_camera.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.fm_init_camera)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(337, 12, 171, 45))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_init_camera = QLabel(self.gridLayoutWidget_3)
        self.lb_init_camera.setObjectName(u"lb_init_camera")

        self.gridLayout_4.addWidget(self.lb_init_camera, 0, 0, 1, 1)

        self.cb_listCameras = QComboBox(self.gridLayoutWidget_3)
        self.cb_listCameras.setObjectName(u"cb_listCameras")

        self.gridLayout_4.addWidget(self.cb_listCameras, 0, 1, 1, 1)

        self.lb_init_camera_2 = QLabel(self.fm_init_camera)
        self.lb_init_camera_2.setObjectName(u"lb_init_camera_2")
        self.lb_init_camera_2.setGeometry(QRect(50, 0, 185, 80))
        self.lb_init_camera_2.setMinimumSize(QSize(0, 80))
        self.lb_init_camera_2.setMaximumSize(QSize(16777215, 80))
        self.lb_init_camera_2.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
        self.pb_init_camera = QPushButton(self.fm_init_camera)
        self.pb_init_camera.setObjectName(u"pb_init_camera")
        self.pb_init_camera.setGeometry(QRect(370, 70, 85, 16))
        self.lb_init_camera_error = QLabel(self.fm_init_camera)
        self.lb_init_camera_error.setObjectName(u"lb_init_camera_error")
        self.lb_init_camera_error.setGeometry(QRect(40, 110, 271, 20))
        self.lb_init_camera_error.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"Microsoft Sans Serif\";")

        self.verticalLayout_9.addWidget(self.fm_init_camera)

        self.stackedWidget.addWidget(self.page_camera)
        self.page_corona = QWidget()
        self.page_corona.setObjectName(u"page_corona")
        self.verticalLayout_7 = QVBoxLayout(self.page_corona)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_title_page_sco = QLabel(self.page_corona)
        self.lb_title_page_sco.setObjectName(u"lb_title_page_sco")
        self.lb_title_page_sco.setMinimumSize(QSize(0, 80))
        self.lb_title_page_sco.setMaximumSize(QSize(16777215, 80))
        self.lb_title_page_sco.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")

        self.verticalLayout_7.addWidget(self.lb_title_page_sco)

        self.fm_settings_corona = QFrame(self.page_corona)
        self.fm_settings_corona.setObjectName(u"fm_settings_corona")
        self.fm_settings_corona.setFrameShape(QFrame.StyledPanel)
        self.fm_settings_corona.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.fm_settings_corona)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fm_buttons_sc = QFrame(self.fm_settings_corona)
        self.fm_buttons_sc.setObjectName(u"fm_buttons_sc")
        self.fm_buttons_sc.setFrameShape(QFrame.StyledPanel)
        self.fm_buttons_sc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.fm_buttons_sc)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.fm_buttons_sc)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_5 = QLabel(self.fm_buttons_sc)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_2 = QLabel(self.fm_buttons_sc)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.le_shotMessage = QLineEdit(self.fm_buttons_sc)
        self.le_shotMessage.setObjectName(u"le_shotMessage")

        self.gridLayout.addWidget(self.le_shotMessage, 2, 1, 1, 1)

        self.le_timeSleepc = QLineEdit(self.fm_buttons_sc)
        self.le_timeSleepc.setObjectName(u"le_timeSleepc")

        self.gridLayout.addWidget(self.le_timeSleepc, 1, 1, 1, 1)

        self.label_4 = QLabel(self.fm_buttons_sc)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.fm_buttons_sc)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.fm_buttons_sc)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.le_shotMode = QLineEdit(self.fm_buttons_sc)
        self.le_shotMode.setObjectName(u"le_shotMode")

        self.gridLayout.addWidget(self.le_shotMode, 4, 1, 1, 1)

        self.le_timeTrigger = QLineEdit(self.fm_buttons_sc)
        self.le_timeTrigger.setObjectName(u"le_timeTrigger")

        self.gridLayout.addWidget(self.le_timeTrigger, 3, 1, 1, 1)

        self.le_timeFlash = QLineEdit(self.fm_buttons_sc)
        self.le_timeFlash.setObjectName(u"le_timeFlash")

        self.gridLayout.addWidget(self.le_timeFlash, 5, 1, 1, 1)

        self.le_timeOut = QLineEdit(self.fm_buttons_sc)
        self.le_timeOut.setObjectName(u"le_timeOut")

        self.gridLayout.addWidget(self.le_timeOut, 6, 1, 1, 1)

        self.label_10 = QLabel(self.fm_buttons_sc)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.lb_sc_port = QLabel(self.fm_buttons_sc)
        self.lb_sc_port.setObjectName(u"lb_sc_port")

        self.gridLayout.addWidget(self.lb_sc_port, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.pb_sc_leds = QPushButton(self.fm_buttons_sc)
        self.pb_sc_leds.setObjectName(u"pb_sc_leds")

        self.verticalLayout_5.addWidget(self.pb_sc_leds)

        self.pb_sc_PWMleds = QPushButton(self.fm_buttons_sc)
        self.pb_sc_PWMleds.setObjectName(u"pb_sc_PWMleds")

        self.verticalLayout_5.addWidget(self.pb_sc_PWMleds)

        self.verticalSpacer = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pb_sc_configuration = QPushButton(self.fm_buttons_sc)
        self.pb_sc_configuration.setObjectName(u"pb_sc_configuration")

        self.verticalLayout_5.addWidget(self.pb_sc_configuration)


        self.horizontalLayout_24.addWidget(self.fm_buttons_sc)

        self.fm_leds = QFrame(self.fm_settings_corona)
        self.fm_leds.setObjectName(u"fm_leds")
        self.fm_leds.setStyleSheet(u"QCheckBox{\n"
"font: 10pt \"Microsoft Sans Serif\";\n"
"}")
        self.fm_leds.setFrameShape(QFrame.StyledPanel)
        self.fm_leds.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fm_leds)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cb_led_1 = QCheckBox(self.fm_leds)
        self.cb_led_1.setObjectName(u"cb_led_1")

        self.verticalLayout_4.addWidget(self.cb_led_1)

        self.cb_led_2 = QCheckBox(self.fm_leds)
        self.cb_led_2.setObjectName(u"cb_led_2")

        self.verticalLayout_4.addWidget(self.cb_led_2)

        self.cb_led_3 = QCheckBox(self.fm_leds)
        self.cb_led_3.setObjectName(u"cb_led_3")

        self.verticalLayout_4.addWidget(self.cb_led_3)

        self.cb_led_4 = QCheckBox(self.fm_leds)
        self.cb_led_4.setObjectName(u"cb_led_4")

        self.verticalLayout_4.addWidget(self.cb_led_4)

        self.cb_led_5 = QCheckBox(self.fm_leds)
        self.cb_led_5.setObjectName(u"cb_led_5")
        self.cb_led_5.setEnabled(True)
        self.cb_led_5.setAcceptDrops(False)
        self.cb_led_5.setAutoFillBackground(False)
        self.cb_led_5.setChecked(False)

        self.verticalLayout_4.addWidget(self.cb_led_5)

        self.cb_led_6 = QCheckBox(self.fm_leds)
        self.cb_led_6.setObjectName(u"cb_led_6")

        self.verticalLayout_4.addWidget(self.cb_led_6)

        self.cb_led_7 = QCheckBox(self.fm_leds)
        self.cb_led_7.setObjectName(u"cb_led_7")

        self.verticalLayout_4.addWidget(self.cb_led_7)

        self.cb_led_8 = QCheckBox(self.fm_leds)
        self.cb_led_8.setObjectName(u"cb_led_8")

        self.verticalLayout_4.addWidget(self.cb_led_8)

        self.cb_led_9 = QCheckBox(self.fm_leds)
        self.cb_led_9.setObjectName(u"cb_led_9")

        self.verticalLayout_4.addWidget(self.cb_led_9)

        self.cb_led_10 = QCheckBox(self.fm_leds)
        self.cb_led_10.setObjectName(u"cb_led_10")

        self.verticalLayout_4.addWidget(self.cb_led_10)

        self.cb_led_11 = QCheckBox(self.fm_leds)
        self.cb_led_11.setObjectName(u"cb_led_11")

        self.verticalLayout_4.addWidget(self.cb_led_11)

        self.cb_led_12 = QCheckBox(self.fm_leds)
        self.cb_led_12.setObjectName(u"cb_led_12")

        self.verticalLayout_4.addWidget(self.cb_led_12)

        self.cb_led_13 = QCheckBox(self.fm_leds)
        self.cb_led_13.setObjectName(u"cb_led_13")

        self.verticalLayout_4.addWidget(self.cb_led_13)

        self.cb_led_14 = QCheckBox(self.fm_leds)
        self.cb_led_14.setObjectName(u"cb_led_14")

        self.verticalLayout_4.addWidget(self.cb_led_14)

        self.cb_led_15 = QCheckBox(self.fm_leds)
        self.cb_led_15.setObjectName(u"cb_led_15")

        self.verticalLayout_4.addWidget(self.cb_led_15)

        self.space_leds = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.space_leds)


        self.horizontalLayout_24.addWidget(self.fm_leds)

        self.fm_PWM = QFrame(self.fm_settings_corona)
        self.fm_PWM.setObjectName(u"fm_PWM")
        self.fm_PWM.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fm_PWM)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.fm_PWM_led_1 = QFrame(self.fm_PWM)
        self.fm_PWM_led_1.setObjectName(u"fm_PWM_led_1")
        self.fm_PWM_led_1.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fm_PWM_led_1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_1 = QLabel(self.fm_PWM_led_1)
        self.lb_PWM_led_1.setObjectName(u"lb_PWM_led_1")

        self.horizontalLayout_5.addWidget(self.lb_PWM_led_1)

        self.le_PWM_led_1 = QLineEdit(self.fm_PWM_led_1)
        self.le_PWM_led_1.setObjectName(u"le_PWM_led_1")

        self.horizontalLayout_5.addWidget(self.le_PWM_led_1)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_1)

        self.fm_PWM_led_2 = QFrame(self.fm_PWM)
        self.fm_PWM_led_2.setObjectName(u"fm_PWM_led_2")
        self.fm_PWM_led_2.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.fm_PWM_led_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_2 = QLabel(self.fm_PWM_led_2)
        self.lb_PWM_led_2.setObjectName(u"lb_PWM_led_2")

        self.horizontalLayout_11.addWidget(self.lb_PWM_led_2)

        self.le_PWM_led_2 = QLineEdit(self.fm_PWM_led_2)
        self.le_PWM_led_2.setObjectName(u"le_PWM_led_2")

        self.horizontalLayout_11.addWidget(self.le_PWM_led_2)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_2)

        self.fm_PWM_led_3 = QFrame(self.fm_PWM)
        self.fm_PWM_led_3.setObjectName(u"fm_PWM_led_3")
        self.fm_PWM_led_3.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fm_PWM_led_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_3 = QLabel(self.fm_PWM_led_3)
        self.lb_PWM_led_3.setObjectName(u"lb_PWM_led_3")

        self.horizontalLayout_6.addWidget(self.lb_PWM_led_3)

        self.le_PWM_led_3 = QLineEdit(self.fm_PWM_led_3)
        self.le_PWM_led_3.setObjectName(u"le_PWM_led_3")

        self.horizontalLayout_6.addWidget(self.le_PWM_led_3)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_3)

        self.fm_PWM_led_4 = QFrame(self.fm_PWM)
        self.fm_PWM_led_4.setObjectName(u"fm_PWM_led_4")
        self.fm_PWM_led_4.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.fm_PWM_led_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_4 = QLabel(self.fm_PWM_led_4)
        self.lb_PWM_led_4.setObjectName(u"lb_PWM_led_4")

        self.horizontalLayout_12.addWidget(self.lb_PWM_led_4)

        self.le_PWM_led_4 = QLineEdit(self.fm_PWM_led_4)
        self.le_PWM_led_4.setObjectName(u"le_PWM_led_4")

        self.horizontalLayout_12.addWidget(self.le_PWM_led_4)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_4)

        self.fm_PWM_led_5 = QFrame(self.fm_PWM)
        self.fm_PWM_led_5.setObjectName(u"fm_PWM_led_5")
        self.fm_PWM_led_5.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.fm_PWM_led_5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_5 = QLabel(self.fm_PWM_led_5)
        self.lb_PWM_led_5.setObjectName(u"lb_PWM_led_5")

        self.horizontalLayout_13.addWidget(self.lb_PWM_led_5)

        self.le_PWM_led_5 = QLineEdit(self.fm_PWM_led_5)
        self.le_PWM_led_5.setObjectName(u"le_PWM_led_5")

        self.horizontalLayout_13.addWidget(self.le_PWM_led_5)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_5)

        self.fm_PWM_led_6 = QFrame(self.fm_PWM)
        self.fm_PWM_led_6.setObjectName(u"fm_PWM_led_6")
        self.fm_PWM_led_6.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.fm_PWM_led_6)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_6 = QLabel(self.fm_PWM_led_6)
        self.lb_PWM_led_6.setObjectName(u"lb_PWM_led_6")

        self.horizontalLayout_14.addWidget(self.lb_PWM_led_6)

        self.le_PWM_led_6 = QLineEdit(self.fm_PWM_led_6)
        self.le_PWM_led_6.setObjectName(u"le_PWM_led_6")

        self.horizontalLayout_14.addWidget(self.le_PWM_led_6)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_6)

        self.fm_PWM_led_7 = QFrame(self.fm_PWM)
        self.fm_PWM_led_7.setObjectName(u"fm_PWM_led_7")
        self.fm_PWM_led_7.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.fm_PWM_led_7)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_7 = QLabel(self.fm_PWM_led_7)
        self.lb_PWM_led_7.setObjectName(u"lb_PWM_led_7")

        self.horizontalLayout_15.addWidget(self.lb_PWM_led_7)

        self.le_PWM_led_7 = QLineEdit(self.fm_PWM_led_7)
        self.le_PWM_led_7.setObjectName(u"le_PWM_led_7")

        self.horizontalLayout_15.addWidget(self.le_PWM_led_7)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_7)

        self.fm_PWM_led_8 = QFrame(self.fm_PWM)
        self.fm_PWM_led_8.setObjectName(u"fm_PWM_led_8")
        self.fm_PWM_led_8.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.fm_PWM_led_8)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_8 = QLabel(self.fm_PWM_led_8)
        self.lb_PWM_led_8.setObjectName(u"lb_PWM_led_8")

        self.horizontalLayout_16.addWidget(self.lb_PWM_led_8)

        self.le_PWM_led_8 = QLineEdit(self.fm_PWM_led_8)
        self.le_PWM_led_8.setObjectName(u"le_PWM_led_8")

        self.horizontalLayout_16.addWidget(self.le_PWM_led_8)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_8)

        self.fm_PWM_led_9 = QFrame(self.fm_PWM)
        self.fm_PWM_led_9.setObjectName(u"fm_PWM_led_9")
        self.fm_PWM_led_9.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.fm_PWM_led_9)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_9 = QLabel(self.fm_PWM_led_9)
        self.lb_PWM_led_9.setObjectName(u"lb_PWM_led_9")

        self.horizontalLayout_17.addWidget(self.lb_PWM_led_9)

        self.le_PWM_led_9 = QLineEdit(self.fm_PWM_led_9)
        self.le_PWM_led_9.setObjectName(u"le_PWM_led_9")

        self.horizontalLayout_17.addWidget(self.le_PWM_led_9)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_9)

        self.fm_PWM_led_10 = QFrame(self.fm_PWM)
        self.fm_PWM_led_10.setObjectName(u"fm_PWM_led_10")
        self.fm_PWM_led_10.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.fm_PWM_led_10)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_10 = QLabel(self.fm_PWM_led_10)
        self.lb_PWM_led_10.setObjectName(u"lb_PWM_led_10")

        self.horizontalLayout_18.addWidget(self.lb_PWM_led_10)

        self.le_PWM_led_10 = QLineEdit(self.fm_PWM_led_10)
        self.le_PWM_led_10.setObjectName(u"le_PWM_led_10")

        self.horizontalLayout_18.addWidget(self.le_PWM_led_10)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_10)

        self.fm_PWM_led_11 = QFrame(self.fm_PWM)
        self.fm_PWM_led_11.setObjectName(u"fm_PWM_led_11")
        self.fm_PWM_led_11.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.fm_PWM_led_11)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_11 = QLabel(self.fm_PWM_led_11)
        self.lb_PWM_led_11.setObjectName(u"lb_PWM_led_11")

        self.horizontalLayout_19.addWidget(self.lb_PWM_led_11)

        self.le_PWM_led_11 = QLineEdit(self.fm_PWM_led_11)
        self.le_PWM_led_11.setObjectName(u"le_PWM_led_11")

        self.horizontalLayout_19.addWidget(self.le_PWM_led_11)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_11)

        self.fm_PWM_led_12 = QFrame(self.fm_PWM)
        self.fm_PWM_led_12.setObjectName(u"fm_PWM_led_12")
        self.fm_PWM_led_12.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.fm_PWM_led_12)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_12 = QLabel(self.fm_PWM_led_12)
        self.lb_PWM_led_12.setObjectName(u"lb_PWM_led_12")

        self.horizontalLayout_20.addWidget(self.lb_PWM_led_12)

        self.le_PWM_led_12 = QLineEdit(self.fm_PWM_led_12)
        self.le_PWM_led_12.setObjectName(u"le_PWM_led_12")

        self.horizontalLayout_20.addWidget(self.le_PWM_led_12)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_12)

        self.fm_PWM_led_13 = QFrame(self.fm_PWM)
        self.fm_PWM_led_13.setObjectName(u"fm_PWM_led_13")
        self.fm_PWM_led_13.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.fm_PWM_led_13)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_13 = QLabel(self.fm_PWM_led_13)
        self.lb_PWM_led_13.setObjectName(u"lb_PWM_led_13")

        self.horizontalLayout_21.addWidget(self.lb_PWM_led_13)

        self.le_PWM_led_13 = QLineEdit(self.fm_PWM_led_13)
        self.le_PWM_led_13.setObjectName(u"le_PWM_led_13")

        self.horizontalLayout_21.addWidget(self.le_PWM_led_13)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_13)

        self.fm_PWM_led_14 = QFrame(self.fm_PWM)
        self.fm_PWM_led_14.setObjectName(u"fm_PWM_led_14")
        self.fm_PWM_led_14.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.fm_PWM_led_14)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_14 = QLabel(self.fm_PWM_led_14)
        self.lb_PWM_led_14.setObjectName(u"lb_PWM_led_14")

        self.horizontalLayout_22.addWidget(self.lb_PWM_led_14)

        self.le_PWM_led_14 = QLineEdit(self.fm_PWM_led_14)
        self.le_PWM_led_14.setObjectName(u"le_PWM_led_14")

        self.horizontalLayout_22.addWidget(self.le_PWM_led_14)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_14)

        self.fm_PWM_led_15 = QFrame(self.fm_PWM)
        self.fm_PWM_led_15.setObjectName(u"fm_PWM_led_15")
        self.fm_PWM_led_15.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM_led_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.fm_PWM_led_15)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lb_PWM_led_15 = QLabel(self.fm_PWM_led_15)
        self.lb_PWM_led_15.setObjectName(u"lb_PWM_led_15")

        self.horizontalLayout_23.addWidget(self.lb_PWM_led_15)

        self.le_PWM_led_15 = QLineEdit(self.fm_PWM_led_15)
        self.le_PWM_led_15.setObjectName(u"le_PWM_led_15")

        self.horizontalLayout_23.addWidget(self.le_PWM_led_15)


        self.verticalLayout_6.addWidget(self.fm_PWM_led_15)

        self.PWM_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.PWM_spacer)


        self.horizontalLayout_24.addWidget(self.fm_PWM)


        self.verticalLayout_7.addWidget(self.fm_settings_corona)

        self.fm_init_corona = QFrame(self.page_corona)
        self.fm_init_corona.setObjectName(u"fm_init_corona")
        sizePolicy1.setHeightForWidth(self.fm_init_corona.sizePolicy().hasHeightForWidth())
        self.fm_init_corona.setSizePolicy(sizePolicy1)
        self.fm_init_corona.setFrameShape(QFrame.StyledPanel)
        self.fm_init_corona.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.fm_init_corona)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(337, 12, 171, 45))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_init_corona_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_init_corona_2.setObjectName(u"lb_init_corona_2")

        self.gridLayout_2.addWidget(self.lb_init_corona_2, 0, 0, 1, 1)

        self.cb_listPort = QComboBox(self.gridLayoutWidget_2)
        self.cb_listPort.setObjectName(u"cb_listPort")

        self.gridLayout_2.addWidget(self.cb_listPort, 0, 1, 1, 1)

        self.lb_init_corona_1 = QLabel(self.fm_init_corona)
        self.lb_init_corona_1.setObjectName(u"lb_init_corona_1")
        self.lb_init_corona_1.setGeometry(QRect(50, 0, 185, 80))
        self.lb_init_corona_1.setMinimumSize(QSize(0, 80))
        self.lb_init_corona_1.setMaximumSize(QSize(16777215, 80))
        self.lb_init_corona_1.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
        self.pb_init_corona = QPushButton(self.fm_init_corona)
        self.pb_init_corona.setObjectName(u"pb_init_corona")
        self.pb_init_corona.setGeometry(QRect(370, 70, 85, 16))
        self.lb_init_c_error = QLabel(self.fm_init_corona)
        self.lb_init_c_error.setObjectName(u"lb_init_c_error")
        self.lb_init_c_error.setGeometry(QRect(40, 110, 271, 20))
        self.lb_init_c_error.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"Microsoft Sans Serif\";")

        self.verticalLayout_7.addWidget(self.fm_init_corona)

        self.stackedWidget.addWidget(self.page_corona)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.label_12 = QLabel(self.page_settings)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(220, 430, 55, 16))
        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.Ventana_Principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_name_window.setText(QCoreApplication.translate("MainWindow", u"AMILI", None))
        self.pb_error_conection_corona.setText("")
        self.lb_error_conection_corona.setText("")
        self.pb_error_conection_camera.setText("")
        self.lb_error_conection_camera.setText("")
        self.pb_minimum.setText("")
        self.pb_normal.setText("")
        self.pb_maximum.setText("")
        self.pb_exit.setText("")
        self.pb_menu_capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pb_menu_camera.setText(QCoreApplication.translate("MainWindow", u"Settings Camera", None))
        self.pb_menu_corona.setText(QCoreApplication.translate("MainWindow", u"Settings Corona", None))
        self.pb_menu_colorReproduction.setText(QCoreApplication.translate("MainWindow", u"Color Reproduction", None))
        self.pb_menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lb_desplegar_menu.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pb_capture.setText("")
        self.pb_next_capture.setText("")
        self.pb_after_capture.setText("")
        self.pb_save_capture.setText("")
        self.pb_clean_capture.setText("")
        self.lb_wavelenth_capture.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">dddddd</p></body></html>", None))
        self.lb_list_imag_1.setText("")
        self.lb_list_imag_2.setText("")
        self.lb_list_imag_3.setText("")
        self.lb_list_imag_4.setText("")
        self.lb_list_imag_5.setText("")
        self.lb_list_imag_6.setText("")
        self.lb_list_imag_7.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_title_page_sca.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Settings Camara</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Trigger Mode</p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Buffer Count</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Exposure</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Sharpness</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Black Level</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Camera</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Gamma</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Gain</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Gain Auto</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Sharpness Auto</p></body></html>", None))
        self.lb_sca_camera.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Exposure Auto</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Buffer Mode</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Buffer Handling Mode</p></body></html>", None))
        self.cb_gainAuto.setText("")
        self.cb_sharpnessAuto.setText("")
        self.cb_exposureAuto.setText("")
        self.cb_triggerMode.setText("")
        self.pb_sca_configuration.setText(QCoreApplication.translate("MainWindow", u"Configuar", None))
        self.lb_init_camera.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Camara</p></body></html>", None))
        self.lb_init_camera_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Inicializar Camara</p></body></html>", None))
        self.pb_init_camera.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.lb_init_camera_error.setText("")
        self.lb_title_page_sco.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Settings Corona</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">time_out</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">time sleep</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Puerto Serial</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Mensaje de disparo</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">time trigger</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">shot mode</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">time flash</p></body></html>", None))
        self.lb_sc_port.setText("")
        self.pb_sc_leds.setText(QCoreApplication.translate("MainWindow", u"Leds", None))
        self.pb_sc_PWMleds.setText(QCoreApplication.translate("MainWindow", u"PWM Leds", None))
        self.pb_sc_configuration.setText(QCoreApplication.translate("MainWindow", u"Configuar", None))
        self.cb_led_1.setText(QCoreApplication.translate("MainWindow", u"410 nm", None))
        self.cb_led_2.setText(QCoreApplication.translate("MainWindow", u"450 nm", None))
        self.cb_led_3.setText(QCoreApplication.translate("MainWindow", u"470 nm", None))
        self.cb_led_4.setText(QCoreApplication.translate("MainWindow", u"490 nm", None))
        self.cb_led_5.setText(QCoreApplication.translate("MainWindow", u"505 nm", None))
        self.cb_led_6.setText(QCoreApplication.translate("MainWindow", u"530 nm", None))
        self.cb_led_7.setText(QCoreApplication.translate("MainWindow", u"560 nm", None))
        self.cb_led_8.setText(QCoreApplication.translate("MainWindow", u"590 nm", None))
        self.cb_led_9.setText(QCoreApplication.translate("MainWindow", u"600 nm", None))
        self.cb_led_10.setText(QCoreApplication.translate("MainWindow", u"620 nm", None))
        self.cb_led_11.setText(QCoreApplication.translate("MainWindow", u"630 nm", None))
        self.cb_led_12.setText(QCoreApplication.translate("MainWindow", u"650 nm", None))
        self.cb_led_13.setText(QCoreApplication.translate("MainWindow", u"720 nm", None))
        self.cb_led_14.setText(QCoreApplication.translate("MainWindow", u"840 nm", None))
        self.cb_led_15.setText(QCoreApplication.translate("MainWindow", u"960 nm", None))
        self.lb_PWM_led_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">410 nm</p></body></html>", None))
        self.lb_PWM_led_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">450 nm</p></body></html>", None))
        self.lb_PWM_led_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">470 nm</p></body></html>", None))
        self.lb_PWM_led_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">490 nm</p></body></html>", None))
        self.lb_PWM_led_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">505 nm</p></body></html>", None))
        self.lb_PWM_led_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">530 nm</p></body></html>", None))
        self.lb_PWM_led_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">560 nm</p></body></html>", None))
        self.lb_PWM_led_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">590 nm</p></body></html>", None))
        self.lb_PWM_led_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">600 nm</p></body></html>", None))
        self.lb_PWM_led_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">620 nm</p></body></html>", None))
        self.lb_PWM_led_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">630 nm</p></body></html>", None))
        self.lb_PWM_led_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">650 nm</p></body></html>", None))
        self.lb_PWM_led_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">720 nm</p></body></html>", None))
        self.lb_PWM_led_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">840 nm</p></body></html>", None))
        self.lb_PWM_led_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">960 nm</p></body></html>", None))
        self.lb_init_corona_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Puerto Serial</p></body></html>", None))
        self.lb_init_corona_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Inicializar Corona</p></body></html>", None))
        self.pb_init_corona.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.lb_init_c_error.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi