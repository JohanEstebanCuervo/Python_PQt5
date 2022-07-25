from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

style = open('Styles/Estilo1.txt', 'r').read()


class Page_Iluminator(QWidget):

    def __init__(self, App):
        super(Page_Iluminator, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

        self.Control_Buttons()

        self.fm_PWM.hide()

        self.fm_settings_iluminator.hide()

        self.Veriq = {'leds':False,'PWM': False}

    def Structure_Page(self):

        self.setObjectName(u"Page_Iluminator")
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
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.fm_settings_iluminator = QFrame(self)
        self.fm_settings_iluminator.setObjectName(u"fm_settings_iluminator")
        self.fm_settings_iluminator.setFrameShape(QFrame.StyledPanel)
        self.fm_settings_iluminator.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.fm_settings_iluminator)
        self.horizontalLayout_24.setSpacing(3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fm_buttons_sc = QFrame(self.fm_settings_iluminator)
        self.fm_buttons_sc.setObjectName(u"fm_buttons_sc")
        self.fm_buttons_sc.setFrameShape(QFrame.StyledPanel)
        self.fm_buttons_sc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.fm_buttons_sc)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_time_out = QLabel(self.fm_buttons_sc)
        self.lb_time_out.setObjectName(u"lb_time_out")
        self.lb_time_out.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_time_out, 6, 0, 1, 1)

        self.lb_time_sleep = QLabel(self.fm_buttons_sc)
        self.lb_time_sleep.setObjectName(u"lb_time_sleep")
        self.lb_time_sleep.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_time_sleep, 1, 0, 1, 1)

        self.lb_serial_port = QLabel(self.fm_buttons_sc)
        self.lb_serial_port.setObjectName(u"lb_serial_port")
        self.lb_serial_port.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_serial_port, 0, 0, 1, 1)

        self.le_shotMessage = QLineEdit(self.fm_buttons_sc)
        self.le_shotMessage.setObjectName(u"le_shotMessage")

        self.gridLayout.addWidget(self.le_shotMessage, 2, 1, 1, 1)

        self.sb_timeSleepc = QDoubleSpinBox(self.fm_buttons_sc)
        self.sb_timeSleepc.setObjectName(u"sb_timeSleepc")
        self.sb_timeSleepc.setSuffix(' ms')
        self.sb_timeSleepc.setSingleStep(0.1)
        self.sb_timeSleepc.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.sb_timeSleepc, 1, 1, 1, 1)

        self.lb_shot_message = QLabel(self.fm_buttons_sc)
        self.lb_shot_message.setObjectName(u"lb_shot_message")
        self.lb_shot_message.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_shot_message, 2, 0, 1, 1)

        self.lb_time_trigger = QLabel(self.fm_buttons_sc)
        self.lb_time_trigger.setObjectName(u"lb_time_trigger")
        self.lb_time_trigger.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_time_trigger, 3, 0, 1, 1)

        self.lb_shot_mode = QLabel(self.fm_buttons_sc)
        self.lb_shot_mode.setObjectName(u"lb_shot_mode")
        self.lb_shot_mode.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_shot_mode, 4, 0, 1, 1)

        self.sb_shotMode = QSpinBox(self.fm_buttons_sc)
        self.sb_shotMode.setObjectName(u"sb_shotMode")
        self.sb_shotMode.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gridLayout.addWidget(self.sb_shotMode, 4, 1, 1, 1)

        self.sb_timeTrigger = QDoubleSpinBox(self.fm_buttons_sc)
        self.sb_timeTrigger.setObjectName(u"sb_timeTrigger")
        self.sb_timeTrigger.setSuffix(' ms')
        self.sb_timeTrigger.setSingleStep(0.1)
        self.sb_timeTrigger.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.sb_timeTrigger, 3, 1, 1, 1)

        self.sb_timeFlash = QDoubleSpinBox(self.fm_buttons_sc)
        self.sb_timeFlash.setObjectName(u"sb_timeFlash")
        self.sb_timeFlash.setSuffix(' ms')
        self.sb_timeFlash.setSingleStep(0.1)
        self.sb_timeFlash.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.sb_timeFlash, 5, 1, 1, 1)

        self.sb_timeOut = QDoubleSpinBox(self.fm_buttons_sc)
        self.sb_timeOut.setObjectName(u"sb_timeOut")
        self.sb_timeOut.setSuffix(' ms')
        self.sb_timeOut.setSingleStep(0.1)
        self.sb_timeOut.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.sb_timeOut, 6, 1, 1, 1)

        self.lb_time_flash = QLabel(self.fm_buttons_sc)
        self.lb_time_flash.setObjectName(u"lb_time_flash")
        self.lb_time_flash.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_time_flash, 5, 0, 1, 1)

        self.lb_port = QLabel(self.fm_buttons_sc)
        self.lb_port.setObjectName(u"lb_port")

        self.gridLayout.addWidget(self.lb_port, 0, 1, 1, 1)

        self.verticalLayout_5.addLayout(self.gridLayout)

        self.pb_leds = QPushButton(self.fm_buttons_sc)
        self.pb_leds.setObjectName(u"pb_leds")

        self.verticalLayout_5.addWidget(self.pb_leds)

        self.pb_PWMleds = QPushButton(self.fm_buttons_sc)
        self.pb_PWMleds.setObjectName(u"pb_PWMleds")

        self.verticalLayout_5.addWidget(self.pb_PWMleds)

        self.verticalSpacer = QSpacerItem(20, 147, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.pb_configuration = QPushButton(self.fm_buttons_sc)
        self.pb_configuration.setObjectName(u"pb_configuration")

        self.verticalLayout_5.addWidget(self.pb_configuration)

        self.pb_eliminar_iluminator = QPushButton(self.fm_buttons_sc)
        self.pb_eliminar_iluminator.setObjectName(u"pb_eliminar_iluminator")
        self.pb_eliminar_iluminator.setStyleSheet(u"QPushButton:hover{\n"
                                                  "background-color: rgb(255, 0, 0);\n"
                                                  "}")
        self.verticalLayout_5.addWidget(self.pb_eliminar_iluminator)

        self.horizontalLayout_24.addWidget(self.fm_buttons_sc)
        self.fm_leds = QFrame(self.fm_settings_iluminator)
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
            self.cb_led[i].stateChanged.connect(self.Edit_leds)
            self.LayoutV_fm_leds.addWidget(self.cb_led[i])

            self.cb_led[i].hide()

        self.space_leds = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_fm_leds.addItem(self.space_leds)

        self.horizontalLayout_24.addWidget(self.fm_leds)

        self.fm_PWM = QFrame(self.fm_settings_iluminator)
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
        self.sb_PWM_led = [None] * 15

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

            self.sb_PWM_led[i] = QSpinBox(self.fm_PWM_led[i])
            self.sb_PWM_led[i].setObjectName(str("le_PWM_led_" + str(i + 1)))
            self.sb_PWM_led[i].setRange(1,100)
            self.sb_PWM_led[i].setSuffix('%')
            self.sb_PWM_led[i].setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.fm_PWM_LayoutH_led[i].addWidget(self.sb_PWM_led[i])

            self.LayoutV_fm_PWM.addWidget(self.fm_PWM_led[i])

            self.fm_PWM_led[i].hide()

        self.PWM_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LayoutV_fm_PWM.addItem(self.PWM_spacer)

        self.horizontalLayout_24.addWidget(self.fm_PWM)

        self.verticalLayout_7.addWidget(self.fm_settings_iluminator)

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
        self.lb_init_iluminador_2 = QLabel(self.gridLayoutWidget_2)
        self.lb_init_iluminador_2.setObjectName(u"lb_init_iluminador_2")

        self.gridLayout_2.addWidget(self.lb_init_iluminador_2, 0, 0, 1, 1)

        self.cb_listPort = QComboBox(self.gridLayoutWidget_2)
        self.cb_listPort.setObjectName(u"cb_listPort")

        self.gridLayout_2.addWidget(self.cb_listPort, 0, 1, 1, 1)

        self.lb_init_iluminador_1 = QLabel(self.fm_init_corona)
        self.lb_init_iluminador_1.setObjectName(u"lb_init_iluminador_1")
        self.lb_init_iluminador_1.setGeometry(QRect(50, 0, 185, 80))
        self.lb_init_iluminador_1.setMinimumSize(QSize(0, 80))
        self.lb_init_iluminador_1.setMaximumSize(QSize(16777215, 80))
        self.lb_init_iluminador_1.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
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

        self.lb_title_page_sco.setText('Settings Iluminador Multiespectral')
        self.lb_time_out.setText('time out')
        self.lb_time_sleep.setText('time sleep')
        self.lb_serial_port.setText('Puerto Serial')
        self.lb_shot_message.setText('Mensaje de disparo')
        self.lb_time_trigger.setText('time trigger')
        self.lb_shot_mode.setText('shot mode')
        self.lb_time_flash.setText('time flash')
        self.lb_port.setText("")
        self.pb_leds.setText("Leds")
        self.pb_PWMleds.setText("PWM Leds")
        self.pb_configuration.setText("Configuar")
        self.pb_eliminar_iluminator.setText("Eliminar")
        self.lb_init_iluminador_2.setText("Puerto Serial")
        self.lb_init_iluminador_1.setText("Inicializar Iluminador")
        self.pb_init_corona.setText("Iniciar")
        self.lb_init_c_error.setText("")

        ##############################
        # Control Buttons
        ##############################

    def Control_Buttons(self):

        self.pb_leds.clicked.connect(self.Control_pb_sc_leds)
        self.pb_PWMleds.clicked.connect(self.Control_pb_sc_PWMleds)
        self.pb_init_corona.clicked.connect(self.Control_pb_init_corona)
        self.pb_configuration.clicked.connect(self.Control_pb_configuration)

    def Control_pb_configuration(self):
        Iluminator = self.App.Core_App.Iluminator_MultiSpectral

        if self.sb_timeSleepc.isModified():
            time_sleep = float(self.sb_timeSleepc.text())
            Iluminator.set_time_sleepc(time_sleep)
            self.sb_timeSleepc.setText(str(time_sleep))
            print(time_sleep)
            
    def Edit_leds(self):
        self.Veriq['leds'] = True

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

                self.lb_port.setText(puerto)
                self.sb_timeSleepc.setValue(Iluminator.attributes['time_sleep']['value'])
                self.sb_timeSleepc.setRange(Iluminator.attributes['time_sleep']['min'],
                                            Iluminator.attributes['time_sleep']['max'])
                self.le_shotMessage.setText(Iluminator.attributes['shot_message']['value'])
                self.sb_timeTrigger.setValue(Iluminator.attributes['time_trigger']['value'])
                self.sb_timeTrigger.setRange(Iluminator.attributes['time_trigger']['min'],
                                             Iluminator.attributes['time_trigger']['max'])
                self.sb_timeOut.setValue(Iluminator.attributes['time_out']['value'])
                self.sb_timeOut.setRange(Iluminator.attributes['time_out']['min'],
                                         Iluminator.attributes['time_out']['max'])
                self.sb_shotMode.setValue(Iluminator.attributes['shot_mode']['value'])
                self.sb_shotMode.setRange(Iluminator.attributes['shot_mode']['min'],
                                          Iluminator.attributes['shot_mode']['max'])
                self.sb_timeFlash.setValue(Iluminator.attributes['time_flash']['value'])
                self.sb_timeFlash.setRange(Iluminator.attributes['time_flash']['min'],
                                           Iluminator.attributes['time_flash']['max'])

                Wavelengths = list(Iluminator.leds.keys())
                self.Rename_cblb_leds(Wavelengths)
                self.fm_init_corona.hide()
                self.fm_settings_iluminator.show()
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
        leds = list(Iluminator.leds.keys())
        for led in Iluminator.get_leds():

            index = leds.index(led)
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

        for i, led in enumerate(Iluminator.get_leds()):
            pwm_val = Iluminator.leds[led]['PWM_val']
            self.sb_PWM_led[i].setValue(pwm_val)

    def Rename_cblb_leds(self, Wavelengths):

        for i, wav in enumerate(Wavelengths):
            self.cb_led[i].setText(str(wav) + ' nm')
            self.lb_PWM_led[i].setText(str(wav) + ' nm PWM')
            self.cb_led[i].show()
            self.fm_PWM_led[i].show()
