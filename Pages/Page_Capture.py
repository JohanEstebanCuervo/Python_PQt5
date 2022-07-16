from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Page_Capture(QWidget):

    def __init__(self, App):
        super(Page_Capture, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

    def Structure_Page(self):

        self.setObjectName(u"Page_Capture")
        self.setStyleSheet(u"QWidget{\n"
                            "background-color: rgb(255, 255, 255);\n"
                            "}\n"
                            "QFrame{\n"
                            "background-color: rgb(161, 187, 215);\n"
                            "}")

        self.LayoutV_Prin = QVBoxLayout(self)
        self.LayoutV_Prin.setSpacing(0)
        self.LayoutV_Prin.setObjectName(u"LayoutV_Prin")
        self.LayoutV_Prin.setContentsMargins(0, 0, 0, 0)
        self.fm_control_capture = QFrame(self)
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
        self.LayoutH_fm_control_capture = QHBoxLayout(self.fm_control_capture)
        self.LayoutH_fm_control_capture.setSpacing(0)
        self.LayoutH_fm_control_capture.setObjectName(u"LayoutH_fm_control_capture")
        self.LayoutH_fm_control_capture.setContentsMargins(0, 0, 0, 0)
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

        self.LayoutH_fm_control_capture.addWidget(self.pb_capture)

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

        self.LayoutH_fm_control_capture.addWidget(self.pb_next_capture)

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

        self.LayoutH_fm_control_capture.addWidget(self.pb_after_capture)

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

        self.LayoutH_fm_control_capture.addWidget(self.pb_save_capture)

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

        self.LayoutH_fm_control_capture.addWidget(self.pb_clean_capture)

        self.lb_wavelenth_capture = QLabel(self.fm_control_capture)
        self.lb_wavelenth_capture.setObjectName(u"lb_wavelenth_capture")
        self.lb_wavelenth_capture.setAlignment(Qt.AlignCenter)
        
        self.LayoutH_fm_control_capture.addWidget(self.lb_wavelenth_capture)


        self.LayoutV_Prin.addWidget(self.fm_control_capture)

        self.gv_Principal_imag = QGraphicsView(self)
        self.gv_Principal_imag.setObjectName(u"gv_Principal_imag")
        self.gv_Principal_imag.setLayoutDirection(Qt.LeftToRight)
        self.gv_Principal_imag.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.gv_Principal_imag.setDragMode(QGraphicsView.ScrollHandDrag)

        self.LayoutV_Prin.addWidget(self.gv_Principal_imag)

        self.fm_list_imag = QFrame(self)
        self.fm_list_imag.setObjectName(u"fm_list_imag")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.fm_list_imag.sizePolicy().hasHeightForWidth())
        self.fm_list_imag.setSizePolicy(sizePolicy)
        self.fm_list_imag.setMaximumSize(QSize(16777215, 100))
        self.fm_list_imag.setFrameShape(QFrame.StyledPanel)
        self.fm_list_imag.setFrameShadow(QFrame.Raised)
        self.LayoutH_fm_list_imag = QHBoxLayout(self.fm_list_imag)
        self.LayoutH_fm_list_imag.setSpacing(1)
        self.LayoutH_fm_list_imag.setObjectName(u"LayoutH_fm_list_imag")
        self.LayoutH_fm_list_imag.setContentsMargins(1, 1, 1, 1)
        self.lb_list_imag_1 = QLabel(self.fm_list_imag)
        self.lb_list_imag_1.setObjectName(u"lb_list_imag_1")
        self.lb_list_imag_1.setScaledContents(True)
        self.lb_list_imag_1.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_1)

        self.lb_list_imag_2 = QLabel(self.fm_list_imag)
        self.lb_list_imag_2.setObjectName(u"lb_list_imag_2")
        self.lb_list_imag_2.setScaledContents(True)
        self.lb_list_imag_2.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_2)

        self.lb_list_imag_3 = QLabel(self.fm_list_imag)
        self.lb_list_imag_3.setObjectName(u"lb_list_imag_3")
        self.lb_list_imag_3.setScaledContents(True)
        self.lb_list_imag_3.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_3)

        self.lb_list_imag_4 = QLabel(self.fm_list_imag)
        self.lb_list_imag_4.setObjectName(u"lb_list_imag_4")
        self.lb_list_imag_4.setScaledContents(True)
        self.lb_list_imag_4.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_4)

        self.lb_list_imag_5 = QLabel(self.fm_list_imag)
        self.lb_list_imag_5.setObjectName(u"lb_list_imag_5")
        self.lb_list_imag_5.setScaledContents(True)
        self.lb_list_imag_5.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_5)

        self.lb_list_imag_6 = QLabel(self.fm_list_imag)
        self.lb_list_imag_6.setObjectName(u"lb_list_imag_6")
        self.lb_list_imag_6.setScaledContents(True)
        self.lb_list_imag_6.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_6)

        self.lb_list_imag_7 = QLabel(self.fm_list_imag)
        self.lb_list_imag_7.setObjectName(u"lb_list_imag_7")
        self.lb_list_imag_7.setScaledContents(True)
        self.lb_list_imag_7.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag_7)


        self.LayoutV_Prin.addWidget(self.fm_list_imag)

        self.LayoutV_Prin.setStretch(2, 20)

    def Names_Page(self):
        self.lb_wavelenth_capture.setText('longitud de imagen')
        