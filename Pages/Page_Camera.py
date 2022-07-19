from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Page_Camera(QWidget):

    def __init__(self, App):
        super(Page_Camera, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

        self.Control_Buttons()

        self.fm_settings_camera.hide()

    def Structure_Page(self):
        self.setObjectName(u"Page_Camera")
        self.LayoutV_Principal = QVBoxLayout(self)
        self.LayoutV_Principal.setObjectName(u"LayoutV_Principal")
        self.lb_title_page_sca = QLabel(self)
        self.lb_title_page_sca.setObjectName(u"lb_title_page_sca")
        self.lb_title_page_sca.setMinimumSize(QSize(0, 80))
        self.lb_title_page_sca.setMaximumSize(QSize(16777215, 80))
        self.lb_title_page_sca.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
        self.lb_title_page_sca.setAlignment(Qt.AlignCenter)

        self.LayoutV_Principal.addWidget(self.lb_title_page_sca)

        self.fm_settings_camera = QFrame(self)
        self.fm_settings_camera.setObjectName(u"fm_settings_camera")
        self.fm_settings_camera.setFrameShape(QFrame.StyledPanel)
        self.fm_settings_camera.setFrameShadow(QFrame.Raised)
        self.LayoutH_fm_settings_camera = QHBoxLayout(self.fm_settings_camera)
        self.LayoutH_fm_settings_camera.setSpacing(3)
        self.LayoutH_fm_settings_camera.setObjectName(u"LayoutH_fm_settings_camera")
        self.LayoutH_fm_settings_camera.setContentsMargins(0, 0, 0, 0)
        self.fm_buttons_sca = QFrame(self.fm_settings_camera)
        self.fm_buttons_sca.setObjectName(u"fm_buttons_sca")
        self.fm_buttons_sca.setFrameShape(QFrame.StyledPanel)
        self.fm_buttons_sca.setFrameShadow(QFrame.Raised)
        self.LayoutV_fm_buttons_sca = QVBoxLayout(self.fm_buttons_sca)
        self.LayoutV_fm_buttons_sca.setSpacing(2)
        self.LayoutV_fm_buttons_sca.setObjectName(u"LayoutV_fm_buttons_sca")
        self.LayoutV_fm_buttons_sca.setContentsMargins(0, 0, 0, 0)
        self.LayoutG_fm_buttons_sca = QGridLayout()
        self.LayoutG_fm_buttons_sca.setObjectName(u"LayoutG_fm_buttons_sca")
        self.label_21 = QLabel(self.fm_buttons_sca)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_21, 9, 0, 1, 1)

        self.label_19 = QLabel(self.fm_buttons_sca)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_19, 11, 0, 1, 1)

        self.label_22 = QLabel(self.fm_buttons_sca)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_22, 8, 0, 1, 1)

        self.label_13 = QLabel(self.fm_buttons_sca)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_13, 6, 0, 1, 1)

        self.label_6 = QLabel(self.fm_buttons_sca)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_3 = QLabel(self.fm_buttons_sca)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_3, 0, 0, 1, 1)

        self.le_gamma = QLineEdit(self.fm_buttons_sca)
        self.le_gamma.setObjectName(u"le_gamma")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_gamma, 2, 1, 1, 1)

        self.le_blackLevel = QLineEdit(self.fm_buttons_sca)
        self.le_blackLevel.setObjectName(u"le_blackLevel")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_blackLevel, 1, 1, 1, 1)

        self.label_14 = QLabel(self.fm_buttons_sca)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_16 = QLabel(self.fm_buttons_sca)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_16, 4, 0, 1, 1)

        self.le_gain = QLineEdit(self.fm_buttons_sca)
        self.le_gain.setObjectName(u"le_gain")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_gain, 4, 1, 1, 1)

        self.label_15 = QLabel(self.fm_buttons_sca)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_15, 3, 0, 1, 1)

        self.le_sharpness = QLineEdit(self.fm_buttons_sca)
        self.le_sharpness.setObjectName(u"le_sharpness")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_sharpness, 6, 1, 1, 1)

        self.label_17 = QLabel(self.fm_buttons_sca)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_17, 5, 0, 1, 1)

        self.lb_sca_camera = QLabel(self.fm_buttons_sca)
        self.lb_sca_camera.setObjectName(u"lb_sca_camera")

        self.LayoutG_fm_buttons_sca.addWidget(self.lb_sca_camera, 0, 1, 1, 1)

        self.label_18 = QLabel(self.fm_buttons_sca)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_18, 7, 0, 1, 1)

        self.label_20 = QLabel(self.fm_buttons_sca)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_20, 10, 0, 1, 1)

        self.label_23 = QLabel(self.fm_buttons_sca)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.LayoutG_fm_buttons_sca.addWidget(self.label_23, 12, 0, 1, 1)

        self.le_exposure = QLineEdit(self.fm_buttons_sca)
        self.le_exposure.setObjectName(u"le_exposure")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_exposure, 8, 1, 1, 1)

        self.le_bufferMode = QLineEdit(self.fm_buttons_sca)
        self.le_bufferMode.setObjectName(u"le_bufferMode")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_bufferMode, 10, 1, 1, 1)

        self.le_bufferCount = QLineEdit(self.fm_buttons_sca)
        self.le_bufferCount.setObjectName(u"le_bufferCount")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_bufferCount, 11, 1, 1, 1)

        self.le_bufferHandlingMode = QLineEdit(self.fm_buttons_sca)
        self.le_bufferHandlingMode.setObjectName(u"le_bufferHandlingMode")

        self.LayoutG_fm_buttons_sca.addWidget(self.le_bufferHandlingMode, 12, 1, 1, 1)

        self.cb_gainAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_gainAuto.setObjectName(u"cb_gainAuto")

        self.LayoutG_fm_buttons_sca.addWidget(self.cb_gainAuto, 3, 1, 1, 1)

        self.cb_sharpnessAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_sharpnessAuto.setObjectName(u"cb_sharpnessAuto")

        self.LayoutG_fm_buttons_sca.addWidget(self.cb_sharpnessAuto, 5, 1, 1, 1)

        self.cb_exposureAuto = QCheckBox(self.fm_buttons_sca)
        self.cb_exposureAuto.setObjectName(u"cb_exposureAuto")

        self.LayoutG_fm_buttons_sca.addWidget(self.cb_exposureAuto, 7, 1, 1, 1)

        self.cb_triggerMode = QCheckBox(self.fm_buttons_sca)
        self.cb_triggerMode.setObjectName(u"cb_triggerMode")

        self.LayoutG_fm_buttons_sca.addWidget(self.cb_triggerMode, 9, 1, 1, 1)

        self.LayoutV_fm_buttons_sca.addLayout(self.LayoutG_fm_buttons_sca)

        self.verticalSpacer_2 = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_fm_buttons_sca.addItem(self.verticalSpacer_2)

        self.pb_sca_configuration = QPushButton(self.fm_buttons_sca)
        self.pb_sca_configuration.setObjectName(u"pb_sca_configuration")

        self.LayoutV_fm_buttons_sca.addWidget(self.pb_sca_configuration)

        self.LayoutH_fm_settings_camera.addWidget(self.fm_buttons_sca)

        self.LayoutV_Principal.addWidget(self.fm_settings_camera)

        self.fm_init_camera = QFrame(self)
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

        self.LayoutV_Principal.addWidget(self.fm_init_camera)

    def Names_Page(self):

        self.lb_title_page_sca.setText('Settings Camara')
        self.label_21.setText('Trigger Mode')
        self.label_19.setText('Buffer Count')
        self.label_22.setText('Exposure')
        self.label_13.setText('Sharpness')
        self.label_6.setText('Black Level')
        self.label_3.setText('Camera')
        self.label_14.setText('Gamma')
        self.label_16.setText('Gain')
        self.label_15.setText('Gain Auto')
        self.label_17.setText('Sharpness Auto')
        self.lb_sca_camera.setText("")
        self.label_18.setText('Exposure Auto')
        self.label_20.setText('Buffer Mode')
        self.label_23.setText('Buffer Handling Mode')
        self.cb_gainAuto.setText("")
        self.cb_sharpnessAuto.setText("")
        self.cb_exposureAuto.setText("")
        self.cb_triggerMode.setText("")
        self.pb_sca_configuration.setText("Configuar")
        self.lb_init_camera.setText('Camara')
        self.lb_init_camera_2.setText('Inicializar Camara')
        self.pb_init_camera.setText('Iniciar')
        self.lb_init_camera_error.setText("")

    ##############################
        # Control Buttons
        ##############################

    def Control_Buttons(self):

        self.pb_init_camera.clicked.connect(self.Control_pb_init_camera)

    def Control_pb_init_camera(self):

        Camera = self.cb_listCameras.currentText()
        self.App.Core_App.Construct_Camera(Camera)

        if self.App.Core_App.camera_init:

            camera = self.App.Core_App.Camera

            if self.App.Core_App.camera_init:

                self.lb_sca_camera.setText(Camera)

                self.le_blackLevel.setText(str(camera.get_blacklevel()))

                self.le_gamma.setText(str(camera.get_gamma()))

                self.le_gain.setText(str(camera.get_gain()))

                self.le_sharpness.setText(str(camera.get_sharpness()))

                self.le_exposure.setText(str(camera.get_exposure()))

                self.le_bufferMode.setText(str(camera.get_buffer_mode()))

                self.le_bufferCount.setText(str(camera.get_buffer_count()))

                self.le_bufferHandlingMode.setText(str(camera.get_buffer_handling_mode()))

                self.cb_gainAuto.setChecked(camera.get_gain_auto())

                self.cb_sharpnessAuto.setChecked(camera.get_sharpness_auto())

                self.cb_exposureAuto.setChecked(camera.get_exposure_auto())

                self.cb_triggerMode.setChecked(camera.get_trigger_mode())

                self.fm_init_camera.hide()
                self.fm_settings_camera.show()
                self.camera_init = True
                self.lb_init_camera_error.setText("")

            else:

                self.lb_init_camera_error.setText("No se ha podido iniciar la camara")
