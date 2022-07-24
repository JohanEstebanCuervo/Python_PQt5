from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from API.ColorReproduction_API import *
from Pages.Viewer import *

import cv2


class Page_ColorReproduction(QWidget):

    def __init__(self, App):
        super(Page_ColorReproduction, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

        self.Control_Buttons()

        self.fm_options_ColorReproduction.hide()

    def Structure_Page(self):

        self.setObjectName(u"Page_ColorReproduction")
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
        self.fm_control_ColorReproduction = QFrame(self)
        self.fm_control_ColorReproduction.setObjectName(u"fm_control_ColorReproduction")
        self.fm_control_ColorReproduction.setMinimumSize(QSize(0, 30))
        self.fm_control_ColorReproduction.setMaximumSize(QSize(16777215, 30))
        self.fm_control_ColorReproduction.setStyleSheet(u"QFrame{\n"
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
        self.fm_control_ColorReproduction.setFrameShape(QFrame.StyledPanel)
        self.fm_control_ColorReproduction.setFrameShadow(QFrame.Raised)
        self.LayoutH_fm_control_capture = QHBoxLayout(self.fm_control_ColorReproduction)
        self.LayoutH_fm_control_capture.setSpacing(0)
        self.LayoutH_fm_control_capture.setObjectName(u"LayoutH_fm_control_capture")
        self.LayoutH_fm_control_capture.setContentsMargins(0, 0, 0, 0)

        self.pb_charge_data = QPushButton(self.fm_control_ColorReproduction)
        self.pb_charge_data.setObjectName(u"pb_charge_data")
        self.pb_charge_data.setMinimumSize(QSize(30, 30))
        self.pb_charge_data.setMaximumSize(QSize(30, 30))
        self.pb_charge_data.setStyleSheet(u"QPushButton:hover{\n"
                                      "background-color: rgb(0, 170, 0);\n"
                                      "}")
        icon4 = QIcon()
        icon4.addFile(u"iconos/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_charge_data.setIcon(icon4)
        self.pb_charge_data.setIconSize(QSize(25, 25))

        self.LayoutH_fm_control_capture.addWidget(self.pb_charge_data)

        self.pb_charge_capture = QPushButton(self.fm_control_ColorReproduction)
        self.pb_charge_capture.setObjectName(u"pb_charge_capture")
        self.pb_charge_capture.setMinimumSize(QSize(30, 30))
        self.pb_charge_capture.setMaximumSize(QSize(30, 30))
        self.pb_charge_capture.setStyleSheet(u"QPushButton:hover{\n"
                                      "background-color: rgb(0, 170, 0);\n"
                                      "}")
        icon4 = QIcon()
        icon4.addFile(u"iconos/importar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_charge_capture.setIcon(icon4)
        self.pb_charge_capture.setIconSize(QSize(25, 25))

        self.LayoutH_fm_control_capture.addWidget(self.pb_charge_capture)

        self.pb_after_capture = QPushButton(self.fm_control_ColorReproduction)
        self.pb_after_capture.setObjectName(u"pb_after_capture")
        self.pb_after_capture.setMinimumSize(QSize(30, 30))
        self.pb_after_capture.setMaximumSize(QSize(30, 30))
        self.pb_after_capture.setStyleSheet(u"QPushButton:hover{\n"
                                             "background-color: rgb(255, 255, 0);\n"
                                             "}")
        icon6 = QIcon()
        icon6.addFile(u"iconos/after.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_after_capture.setIcon(icon6)
        self.pb_after_capture.setIconSize(QSize(25, 25))

        self.LayoutH_fm_control_capture.addWidget(self.pb_after_capture)

        self.pb_next_capture = QPushButton(self.fm_control_ColorReproduction)
        self.pb_next_capture.setObjectName(u"pb_next_capture")
        self.pb_next_capture.setMinimumSize(QSize(30, 30))
        self.pb_next_capture.setMaximumSize(QSize(30, 30))
        self.pb_next_capture.setStyleSheet(u"QPushButton:hover{\n"
                                           "background-color: rgb(255, 255, 0);\n"
                                           "}")
        icon5 = QIcon()
        icon5.addFile(u"iconos/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_next_capture.setIcon(icon5)
        self.pb_next_capture.setIconSize(QSize(25, 25))

        self.LayoutH_fm_control_capture.addWidget(self.pb_next_capture)

        self.pb_save_viewer = QPushButton(self.fm_control_ColorReproduction)
        self.pb_save_viewer.setObjectName(u"pb_save_viewer")
        self.pb_save_viewer.setMinimumSize(QSize(30, 30))
        self.pb_save_viewer.setMaximumSize(QSize(30, 30))
        self.pb_save_viewer.setStyleSheet(u"QPushButton:hover{\n"
                                          "background-color:  rgb(170, 0, 127);\n"
                                          "}")
        icon7 = QIcon()
        icon7.addFile(u"iconos/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_viewer.setIcon(icon7)
        self.pb_save_viewer.setIconSize(QSize(25, 25))

        self.LayoutH_fm_control_capture.addWidget(self.pb_save_viewer)

        self.pb_clean_capture = QPushButton(self.fm_control_ColorReproduction)
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

        self.lb_wavelenth_capture = QLabel(self.fm_control_ColorReproduction)
        self.lb_wavelenth_capture.setObjectName(u"lb_wavelenth_capture")
        self.lb_wavelenth_capture.setAlignment(Qt.AlignCenter)

        self.LayoutH_fm_control_capture.addWidget(self.lb_wavelenth_capture)

        self.LayoutV_Prin.addWidget(self.fm_control_ColorReproduction)

        self.fm_options_ColorReproduction = QFrame(self)
        self.fm_options_ColorReproduction.setObjectName(u"fm_options_ColorReproduction")
        self.fm_options_ColorReproduction.setMinimumSize(QSize(0, 30))
        self.fm_options_ColorReproduction.setMaximumSize(QSize(16777215, 30))
        self.fm_options_ColorReproduction.setStyleSheet(u"QFrame{\n"
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
        self.fm_options_ColorReproduction.setFrameShape(QFrame.StyledPanel)
        self.fm_options_ColorReproduction.setFrameShadow(QFrame.Raised)
        self.LayoutH_fm_options_ColorReproduction = QHBoxLayout(self.fm_options_ColorReproduction)
        self.LayoutH_fm_options_ColorReproduction.setSpacing(0)
        self.LayoutH_fm_options_ColorReproduction.setObjectName(u"LayoutH_fm_options_ColorReproduction")
        self.LayoutH_fm_options_ColorReproduction.setContentsMargins(0, 0, 0, 0)

        self.pb_colorReproduce = QPushButton(self.fm_options_ColorReproduction)
        self.pb_colorReproduce.setObjectName(u"pb_colorReproduce")
        self.pb_colorReproduce.setMinimumSize(QSize(10, 30))
        self.pb_colorReproduce.setMaximumSize(QSize(16777215, 30))
        self.LayoutH_fm_options_ColorReproduction.addWidget(self.pb_colorReproduce)

        self.pb_masks = QPushButton(self.fm_options_ColorReproduction)
        self.pb_masks.setObjectName(u"pb_masks")
        self.pb_masks.setMinimumSize(QSize(10, 30))
        self.pb_masks.setMaximumSize(QSize(16777215, 30))
        self.LayoutH_fm_options_ColorReproduction.addWidget(self.pb_masks)

        self.pb_ecualizacion = QPushButton(self.fm_options_ColorReproduction)
        self.pb_ecualizacion.setObjectName(u"pb_ecualizacion")
        self.pb_ecualizacion.setMinimumSize(QSize(10, 30))
        self.pb_ecualizacion.setMaximumSize(QSize(16777215, 30))
        self.LayoutH_fm_options_ColorReproduction.addWidget(self.pb_ecualizacion)

        self.pb_colorCorrection = QPushButton(self.fm_options_ColorReproduction)
        self.pb_colorCorrection.setObjectName(u"pb_colorCorrection")
        self.pb_colorCorrection.setMinimumSize(QSize(10, 30))
        self.pb_colorCorrection.setMaximumSize(QSize(16777215, 30))
        self.LayoutH_fm_options_ColorReproduction.addWidget(self.pb_colorCorrection)

        self.spacer_bar = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.LayoutH_fm_options_ColorReproduction.addItem(self.spacer_bar)

        self.LayoutV_Prin.addWidget(self.fm_options_ColorReproduction)

        self.gv_Principal_imag = Viewer(self)
        self.gv_Principal_imag.setObjectName(u"gv_Principal_imag")
        self.gv_Principal_imag.setLayoutDirection(Qt.LeftToRight)
        # self.gv_Principal_imag.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        # self.gv_Principal_imag.setDragMode(QGraphicsView.ScrollHandDrag)

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

        self.lb_list_imag = [None] * 7

        for i in range(7):

            self.lb_list_imag[i] = QLabel(self.fm_list_imag)
            self.lb_list_imag[i].setObjectName("lb_list_imag_" + str(i + 1))
            self.lb_list_imag[i].setScaledContents(True)
            self.lb_list_imag[i].setAlignment(Qt.AlignCenter)

            self.LayoutH_fm_list_imag.addWidget(self.lb_list_imag[i])

        self.LayoutV_Prin.addWidget(self.fm_list_imag)

        self.LayoutV_Prin.setStretch(2, 20)

    def Names_Page(self):

        self.lb_wavelenth_capture.setText('longitud de imagen')
        self.pb_colorReproduce.setText(' Color ')
        self.pb_masks.setText(' Mascaras ')
        self.pb_ecualizacion.setText(' Ecualización ')
        self.pb_colorCorrection.setText(' Corrección ')

        ##############################
        # Control Buttons
        ##############################

    def Control_Buttons(self):

        self.pb_charge_capture.clicked.connect(self.Control_pb_charge_capture)
        self.pb_next_capture.clicked.connect(self.Control_pb_next_capture)
        self.pb_after_capture.clicked.connect(self.Control_pb_after_capture)
        self.pb_colorReproduce.clicked.connect(self.Control_pb_colorReproduce)

    def Control_pb_colorReproduce(self):

        imagen = np.array(self.Color_repro.ReproduccionCie1931()).astype('float')
        imagen = (imagen * 255).astype(np.uint8)

        pixmap = self.convert_cv_qt(imagen)

        self.gv_Principal_imag.setPhoto(pixmap)
        self.lb_wavelenth_capture.setText('Imagen RGB')

    def Control_pb_charge_capture(self):
        self.Color_repro = ColorReproduction()

        self.Charge_Images(0)

        self.Color_repro.Charge_CIE()
        file = self.App.Core_App.Patch_Acquisition.absolutePath()
        N = len(self.imagenesCarpeta)
        self.Color_repro.Load_Capture(file, N)

        self.fm_options_ColorReproduction.show()

    def Charge_Images(self, index_prin):

        Imagenes = self.App.Core_App.Patch_Acquisition.entryInfoList(["*.bmp"],
                                                                     QDir.Files, QDir.Name)

        self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in Imagenes]
        if len(self.imagenesCarpeta) != 0:
            Iluminator = self.App.Core_App.Iluminator_MultiSpectral
            self.index_PImag = index_prin
            imagen_prin = QPixmap(self.imagenesCarpeta[self.index_PImag])
            index = Iluminator.leds[Iluminator.get_leds()[self.index_PImag]]
            self.lb_wavelenth_capture.setText(Iluminator.Wavelengths[index] + ' nm')
            self.gv_Principal_imag.setPhoto(imagen_prin)

            self.Charge_lb_list_imag()
            self.Color_repro.wavelengths = []
            for led_name in Iluminator.get_leds():
                index = Iluminator.leds[led_name]
                self.Color_repro.wavelengths.append(int(Iluminator.Wavelengths[index]))

    def Charge_lb_list_imag(self):

        if len(self.imagenesCarpeta) < 7:

            inicio = 0
            fin = len(self.imagenesCarpeta)

        else:
            inicio = self.index_PImag - 3
            fin = inicio + 7

            if inicio < 0:
                fin -= inicio
                inicio -= inicio

            if fin > len(self.imagenesCarpeta):
                dif = fin - len(self.imagenesCarpeta)
                inicio -= dif
                fin -= dif

        for i, nombreimagen in enumerate(self.imagenesCarpeta[inicio:fin]):
            rect = self.lb_list_imag[i].rect()
            imagen = QPixmap(nombreimagen)
            imagen = imagen.scaled(rect.height(), rect.width(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.lb_list_imag[i].setPixmap(imagen)

    def Control_pb_next_capture(self):

        index = self.index_PImag + 1

        if index < len(self.imagenesCarpeta):
            self.Charge_Images(index)

    def Control_pb_after_capture(self):

        index = self.index_PImag - 1

        if index >= 0:
            self.Charge_Images(index)

    def convert_cv_qt(self, imagen_ent):
        """Convert from an opencv image to QPixmap"""
        imagen = cv2.cvtColor(imagen_ent, cv2.COLOR_BGR2RGB)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        h, w, ch = imagen.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(imagen.data, w, h, bytes_per_line, QImage.Format_RGB888)

        return QPixmap.fromImage(convert_to_Qt_format)
