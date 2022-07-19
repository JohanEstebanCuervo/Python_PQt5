from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Viewer(QGraphicsView):
    photoClicked = pyqtSignal(QPoint)

    def __init__(self, App):
        super(Viewer, self).__init__(App)
        self.App = App
        self._zoom = 0
        self._empty = True
        self._scene = QGraphicsScene(self)
        self._photo = QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QBrush(QColor(161, 187, 215)))
        self.setFrameShape(QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0

        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())
        #self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            factor = 1.25
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 1 / factor
                self._zoom -= 1
            if self._zoom >= 0:
                self.scale(factor, factor)
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            self.setDragMode(QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
        super(Viewer, self).mousePressEvent(event)

class Page_Capture(QWidget):

    def __init__(self, App):
        super(Page_Capture, self).__init__(App)
        self.App = App

        self.Structure_Page()

        self.Names_Page()

        self.Control_Buttons()

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

        self.pb_after_capture = QPushButton(self.fm_control_capture)
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

        self.pb_next_capture = QPushButton(self.fm_control_capture)
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

        ##############################
        # Control Buttons
        ##############################

    def Control_Buttons(self):

        self.pb_capture.clicked.connect(self.Control_pb_capture)
        self.pb_next_capture.clicked.connect(self.Control_pb_next_capture)
        self.pb_after_capture.clicked.connect(self.Control_pb_after_capture)

    def Control_pb_capture(self):

        if self.App.Core_App.camera_init and self.App.Core_App.iluminator_init:

            Iluminator = self.App.Core_App.Iluminator_MultiSpectral
            Camera = self.App.Core_App.Camera

            Camera.Mode_Acquisition_Multispectral()

            Camera.Set_Buffer_Count(len(Iluminator.get_leds()))

            Camera.Set_Buffer_Handling_Mode('OldestFirstOverwrite')

            Camera.Init_Acquisition()

            Iluminator.set_time_sleepc(1e-1)

            Iluminator.shot_multispectral()

            for led in Iluminator.get_leds():
                index = Iluminator.leds[led]
                Camera.Acquire_Image(Iluminator.Wavelengths[index])

            Camera.End_Acquisition()

            self.Charge_Images(0)

    def Charge_Images(self,index_prin):
        Iluminator = self.App.Core_App.Iluminator_MultiSpectral

        Imagenes = self.App.Core_App.Patch_Acquisition.entryInfoList(["*.bmp"],
                                                                     QDir.Files, QDir.Name)

        self.imagenesCarpeta = [imagen.absoluteFilePath() for imagen in Imagenes]

        self.index_PImag = index_prin
        imagen_prin = QPixmap(self.imagenesCarpeta[self.index_PImag])
        index = Iluminator.leds[Iluminator.get_leds()[self.index_PImag]]
        self.lb_wavelenth_capture.setText(Iluminator.Wavelengths[index] + ' nm')
        self.gv_Principal_imag.setPhoto(imagen_prin)

        self.Charge_lb_list_imag()

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
