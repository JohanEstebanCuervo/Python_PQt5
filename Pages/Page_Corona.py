from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

style = open('Styles/Estilo1.txt', 'r').read()


class Page_Corona(QWidget):

    def __init__(self, App):
        super(Page_Corona, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

        self.Control_Buttons()

        self.fm_PWM.hide()

        self.fm_settings_corona.hide()

    def Structure_Page(self):

        self.setObjectName(u"Page_Corona")
        self.setStyleSheet(style)
        self.verticalLayout_7 = QVBoxLayout(self)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_title_page_sco = QLabel(self)
        self.lb_title_page_sco.setObjectName(u"lb_title_page_sco")
        self.lb_title_page_sco.setMinimumSize(QSize(0, 80))
        self.lb_title_page_sco.setMaximumSize(QSize(16777215, 80))
        self.lb_title_page_sco.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
        self.lb_title_page_sco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_title_page_sco)

        self.fm_settings_corona = QFrame(self)
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
        self.label_11.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_5 = QLabel(self.fm_buttons_sc)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_2 = QLabel(self.fm_buttons_sc)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.le_shotMessage = QLineEdit(self.fm_buttons_sc)
        self.le_shotMessage.setObjectName(u"le_shotMessage")

        self.gridLayout.addWidget(self.le_shotMessage, 2, 1, 1, 1)

        self.le_timeSleepc = QLineEdit(self.fm_buttons_sc)
        self.le_timeSleepc.setObjectName(u"le_timeSleepc")

        self.gridLayout.addWidget(self.le_timeSleepc, 1, 1, 1, 1)

        self.label_4 = QLabel(self.fm_buttons_sc)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_8 = QLabel(self.fm_buttons_sc)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.fm_buttons_sc)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

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
        self.label_10.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

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
        self.LayoutV_fm_leds = QVBoxLayout(self.fm_leds)
        self.LayoutV_fm_leds.setSpacing(0)
        self.LayoutV_fm_leds.setObjectName(u"LayoutV_fm_leds")
        self.LayoutV_fm_leds.setContentsMargins(0, 0, 0, 0)

        # Leds Check Box

        self.cb_led = [None] * 15

        for i in range(15):
            self.cb_led[i] = QCheckBox(self.fm_leds)
            self.cb_led[i].setObjectName(str("cb_led_" + str(i + 1)))
            self.LayoutV_fm_leds.addWidget(self.cb_led[i])

        self.space_leds = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_fm_leds.addItem(self.space_leds)

        self.horizontalLayout_24.addWidget(self.fm_leds)

        self.fm_PWM = QFrame(self.fm_settings_corona)
        self.fm_PWM.setObjectName(u"fm_PWM")
        self.fm_PWM.setFrameShape(QFrame.StyledPanel)
        self.fm_PWM.setFrameShadow(QFrame.Raised)

        self.LayoutV_fm_PWM = QVBoxLayout(self.fm_PWM)
        self.LayoutV_fm_PWM.setSpacing(0)
        self.LayoutV_fm_PWM.setObjectName(u"LayoutV_fm_PWM")
        self.LayoutV_fm_PWM.setContentsMargins(0, 0, 0, 0)

        # List Line Edit PWM leds

        self.fm_PWM_led = [None] * 15
        self.fm_PWM_LayoutH_led = [None] * 15
        self.lb_PWM_led = [None] * 15
        self.le_PWM_led = [None] * 15

        for i in range(15):
            self.fm_PWM_led[i] = QFrame(self.fm_PWM)
            self.fm_PWM_led[i].setObjectName(str("fm_PWM_led_" + str(i + 1)))
            self.fm_PWM_led[i].setFrameShape(QFrame.StyledPanel)
            self.fm_PWM_led[i].setFrameShadow(QFrame.Raised)

            self.fm_PWM_LayoutH_led[i] = QHBoxLayout(self.fm_PWM_led[i])
            self.fm_PWM_LayoutH_led[i].setSpacing(0)
            self.fm_PWM_LayoutH_led[i].setObjectName(str("fm_PWM_LayoutH_led_" + str(i + 1)))
            self.fm_PWM_LayoutH_led[i].setContentsMargins(0, 0, 0, 0)

            self.lb_PWM_led[i] = QLabel(self.fm_PWM_led[i])
            self.lb_PWM_led[i].setObjectName(str("lb_PWM_led_" + str(i + 1)))

            self.fm_PWM_LayoutH_led[i].addWidget(self.lb_PWM_led[i])

            self.le_PWM_led[i] = QLineEdit(self.fm_PWM_led[i])
            self.le_PWM_led[i].setObjectName(str("le_PWM_led_" + str(i + 1)))

            self.fm_PWM_LayoutH_led[i].addWidget(self.le_PWM_led[i])

            self.LayoutV_fm_PWM.addWidget(self.fm_PWM_led[i])

        self.PWM_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_fm_PWM.addItem(self.PWM_spacer)

        self.horizontalLayout_24.addWidget(self.fm_PWM)

        self.verticalLayout_7.addWidget(self.fm_settings_corona)

        self.fm_init_corona = QFrame(self)
        self.fm_init_corona.setObjectName(u"fm_init_corona")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
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

    def Names_Page(self):

        self.lb_title_page_sco.setText('Settings Corona')
        self.label_11.setText('time_out')
        self.label_5.setText('time sleep')
        self.label_2.setText('Puerto Serial')
        self.label_4.setText('Mensaje de disparo')
        self.label_8.setText('time trigger')
        self.label_9.setText('shot mode')
        self.label_10.setText('time flash')
        self.lb_sc_port.setText("")
        self.pb_sc_leds.setText("Leds")
        self.pb_sc_PWMleds.setText("PWM Leds")
        self.pb_sc_configuration.setText("Configuar")

        self.Wavelengths = ['410', '450', '470', '490', '505', '530', '560', '590', '600',
                            '620', '630', '650', '720', '840', '960']

        for i, wav in enumerate(self.Wavelengths):
            self.cb_led[i].setText(wav + ' nm')
            self.lb_PWM_led[i].setText(wav + ' nm')

        self.lb_init_corona_2.setText("Puerto Serial")
        self.lb_init_corona_1.setText("Inicializar Corona")
        self.pb_init_corona.setText("Iniciar")
        self.lb_init_c_error.setText("")

        ##############################
        # Control Buttons
        ##############################

    def Control_Buttons(self):

        self.pb_sc_leds.clicked.connect(self.Control_pb_sc_leds)
        self.pb_sc_PWMleds.clicked.connect(self.Control_pb_sc_PWMleds)
        self.pb_init_corona.clicked.connect(self.Control_pb_init_corona)

    def Control_pb_sc_leds(self):

        self.fm_leds.show()
        self.fm_PWM.hide()

    def Control_pb_sc_PWMleds(self):

        self.fm_leds.hide()
        self.fm_PWM.show()

        self.fm_PWM_led_hs()

    def Control_pb_init_corona(self):

        puerto = self.cb_listPort.currentText()

        self.App.Core_App.Construct_Iluminator(puerto)

        if self.App.Core_App.iluminator_init:

            Iluminator = self.App.Core_App.Iluminator_MultiSpectral
            if Iluminator.get_comunication_state():

                self.cb_leds_checked_init()
                self.le_PWM_led_setText_init()

                self.lb_sc_port.setText(puerto)
                self.le_timeSleepc.setText(str(Iluminator.get_time_sleepc()))
                self.le_shotMessage.setText(str(Iluminator.get_shot_message()))
                self.le_timeTrigger.setText(str(Iluminator.get_shot_time_trigger()))
                self.le_timeOut.setText(str(Iluminator.get_shot_time_out()))
                self.le_shotMode.setText(str(Iluminator.get_shot_mode()))
                self.le_timeFlash.setText(str(Iluminator.get_shot_time_flash()))

                self.fm_init_corona.hide()
                self.fm_settings_corona.show()
                self.lb_init_c_error.setText("")

            else:
                self.App.Core_App.iluminator_init = False
                print('Estado de comunicación desconectado')

    def fm_PWM_led_hs(self):

        for i, cb_led in enumerate(self.cb_led):

            if cb_led.isChecked():
                self.fm_PWM_led[i].show()
            else:
                self.fm_PWM_led[i].hide()

    def cb_leds_checked_init(self):
        Iluminator = self.App.Core_App.Iluminator_MultiSpectral

        for led in Iluminator.get_leds():

            index = Iluminator.leds[led]
            self.cb_led[index].setChecked(True)

    def cb_leds_is_checked(self):
        Iluminator = self.App.Core_App.Iluminator_MultiSpectral

        lista_leds = []

        for i, checkBox in enumerate(self.cb_led):

            if checkBox.isChecked():
                name = list(Iluminator.leds.keys())[i]
                lista_leds.append(name)

        return lista_leds

    def le_PWM_led_setText_init(self):

        Iluminator = self.App.Core_App.Iluminator_MultiSpectral

        for i, pwm_led in enumerate(Iluminator.get_PWM_leds()):

            self.le_PWM_led[i].setText(pwm_led[2:5])
