from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Menu(QFrame):

    """docstring for Menu"""

    def __init__(self, App):
        super(Menu, self).__init__(App)
        self.App = App

        self.Structure_Menu()

        self.Names_Menu()

        self.Control_Buttons()

    def Structure_Menu(self):
        self.setObjectName(u"Menu")
        self.setMinimumSize(QSize(300, 0))
        self.setMaximumSize(QSize(300, 16777215))
        self.setStyleSheet(u"QFrame{\n"
                           "background-color: rgb(161, 187, 215);\n"
                           "}\n"
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
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.LayoutV_principal = QVBoxLayout(self)
        self.LayoutV_principal.setSpacing(1)
        self.LayoutV_principal.setObjectName(u"LayoutV_principal")
        self.LayoutV_principal.setContentsMargins(0, 0, 0, 0)
        self.pb_menu_capture = QPushButton(self)
        self.pb_menu_capture.setObjectName(u"pb_menu_capture")
        self.pb_menu_capture.setMinimumSize(QSize(0, 30))
        self.pb_menu_capture.setMaximumSize(QSize(16777215, 30))

        self.LayoutV_principal.addWidget(self.pb_menu_capture)

        self.pb_menu_camera = QPushButton(self)
        self.pb_menu_camera.setObjectName(u"pb_menu_camera")
        self.pb_menu_camera.setMinimumSize(QSize(0, 30))
        self.pb_menu_camera.setMaximumSize(QSize(16777215, 30))

        self.LayoutV_principal.addWidget(self.pb_menu_camera)

        self.pb_menu_corona = QPushButton(self)
        self.pb_menu_corona.setObjectName(u"pb_menu_corona")
        self.pb_menu_corona.setMinimumSize(QSize(0, 30))
        self.pb_menu_corona.setMaximumSize(QSize(16777215, 30))

        self.LayoutV_principal.addWidget(self.pb_menu_corona)

        self.pb_menu_colorReproduction = QPushButton(self)
        self.pb_menu_colorReproduction.setObjectName(u"pb_menu_colorReproduction")
        self.pb_menu_colorReproduction.setMinimumSize(QSize(0, 30))
        self.pb_menu_colorReproduction.setMaximumSize(QSize(16777215, 30))

        self.LayoutV_principal.addWidget(self.pb_menu_colorReproduction)

        self.pb_menu_settings = QPushButton(self)
        self.pb_menu_settings.setObjectName(u"pb_menu_settings")
        self.pb_menu_settings.setMinimumSize(QSize(0, 30))
        self.pb_menu_settings.setMaximumSize(QSize(16777215, 30))

        self.LayoutV_principal.addWidget(self.pb_menu_settings)

        self.spacer_menu = QSpacerItem(20, 503, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_principal.addItem(self.spacer_menu)

    def Names_Menu(self):

        self.pb_menu_capture.setText("Capture")
        self.pb_menu_camera.setText("Settings Camera")
        self.pb_menu_corona.setText("Settings Corona")
        self.pb_menu_colorReproduction.setText("Color Reproduction")
        self.pb_menu_settings.setText("Settings")

    #########################
    # Control Buttons
    #########################

    def Control_Buttons(self):
        Stacked_Pages = self.App.Stacked_Pages
        self.pb_menu_capture.clicked.connect(lambda: Stacked_Pages.setCurrentWidget(Stacked_Pages.page_capture))
        self.pb_menu_camera.clicked.connect(self.Control_pb_menu_camera)
        self.pb_menu_corona.clicked.connect(self.Control_pb_menu_corona)
        self.pb_menu_colorReproduction.clicked.connect(lambda: Stacked_Pages.setCurrentWidget(Stacked_Pages.page_colorReproduction))
        self.pb_menu_settings.clicked.connect(lambda: Stacked_Pages.setCurrentWidget(Stacked_Pages.page_settings))

    def Control_pb_menu_corona(self):
        if not self.App.Core_App.iluminator_init:
            self.App.Core_App.Update_list_ports(Update_cb_listPort=True)

        Stacked_Pages = self.App.Stacked_Pages
        Stacked_Pages.setCurrentWidget(Stacked_Pages.page_corona)

    def Control_pb_menu_camera(self):
        if not self.App.Core_App.camera_init:
            self.App.Core_App.Update_list_cameras(Update_cb_listCameras=True)

        Stacked_Pages = self.App.Stacked_Pages
        Stacked_Pages.setCurrentWidget(Stacked_Pages.page_camera)
