from API.Flea3Cam_API import *
from API.MultiespectralCrown import *
from API.Virtual_Iluminator_MultiSpectral import *
from API.ColorReproduction_API import *
from API.VirtualCam import *

import methods.Funciones_Adquisicion as Fun_Ad

from PyQt5.QtCore import QDir, QTimer, QThread
import subprocess


class Check_Connection_proces(QThread):

    def __init__(self, App):
        super().__init__()
        self.App = App
        self.corona_error = False
        self.camera_error = False

    def run(self):
        Core_App = self.App.Core_App
        self.corona_error = False
        self.camera_error = False
        if Core_App.iluminator_init:
            self.Update_list_ports()
            bandera = 0
            for port in self.list_ports:
                if(port == self.App.Stacked_Pages.page_corona.lb_sc_port.text()):
                    bandera = 1
                    break

            if bandera == 0:
                self.corona_error = True

        if Core_App.camera_init:
            self.Update_list_cameras()  # optimizar ya que es muy lento
            bandera = 0
            for cam in self.list_cameras:
                if(cam == self.App.Stacked_Pages.page_camera.lb_sca_camera.text()):
                    bandera = 1
                    break

            if bandera == 0:
                self.camera_error = True

    def Update_list_ports(self, Update_cb_listPort=False):
        self.list_ports = Fun_Ad.Serial_Port_Select(terminal=False)
        self.list_ports.append('VirtualIluminator')

        if Update_cb_listPort:
            self.App.Stacked_Pages.page_corona.cb_listPort.clear()

            if len(self.list_ports) > 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItems(self.list_ports)

            elif len(self.list_ports) == 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItem(list_ports[0])

    def Update_list_cameras(self, Update_cb_listCameras=False):
        self.list_cameras = Fun_Ad.Cameras_List()
        if self.list_cameras:

            self.list_cameras = ['VirtualCamera']
        else:

            self.list_cameras.append('VirtualCamera')

        if Update_cb_listCameras:
            ComBox_cameras = self.App.Stacked_Pages.page_camera.cb_listCameras

            ComBox_cameras.clear()
            if len(self.list_cameras) > 1:
                ComBox_cameras.addItems(self.list_cameras)

            elif len(self.list_cameras) == 1:
                ComBox_cameras.addItem(self.list_cameras[0])


class Core_App:

    """docstring for Core_App"""

    def __init__(self, App):
        self.App = App

        # carpeta temporal
        subprocess.run('md temp', shell=True)
        subprocess.run('attrib +h temp', shell=True)
        self.Patch_Acquisition = QDir(QDir.currentPath() + '/temp')
    ##########################################
    # timer para actualizacion del boton
    ##########################################

        self.check = Check_Connection_proces(self.App)
        self.check.finished.connect(self.CompCheck)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.check.start())
        self.timer.start(2000)
        self.iluminator_init = False
        self.camera_init = False

    def CompCheck(self):

        if self.check.camera_error:

            self.camera_init = False
            self.App.Barra_Principal.pb_error_conection_camera.setStyleSheet("background-color : red; border-radius: 10px")
            self.App.Barra_Principal.lb_error_conection_camera.setText("Camara desconectada")
            self.App.Stacked_Pages.page_camera.fm_init_camera.show()
            self.App.Stacked_Pages.page_camera.fm_settings_camera.hide()

        if self.check.corona_error:

            self.iluminator_init = False
            self.App.Barra_Principal.pb_error_conection_corona.setStyleSheet("background-color : red; border-radius: 10px")
            self.App.Barra_Principal.lb_error_conection_corona.setText("Corona desconectada")
            self.App.Stacked_Pages.page_corona.fm_init_corona.show()
            self.App.Stacked_Pages.page_corona.fm_settings_corona.hide()

    def Update_list_ports(self, Update_cb_listPort=False):
        self.list_ports = Fun_Ad.Serial_Port_Select(terminal=False)
        self.list_ports.append('VirtualIluminator')

        if Update_cb_listPort:
            self.App.Stacked_Pages.page_corona.cb_listPort.clear()

            if len(self.list_ports) > 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItems(self.list_ports)

            elif len(self.list_ports) == 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItem(list_ports[0])

    def Update_list_cameras(self, Update_cb_listCameras=False):
        self.list_cameras = Fun_Ad.Cameras_List()
        if self.list_cameras:

            self.list_cameras = ['VirtualCamera']
        else:

            self.list_cameras.append('VirtualCamera')

        if Update_cb_listCameras:
            ComBox_cameras = self.App.Stacked_Pages.page_camera.cb_listCameras

            ComBox_cameras.clear()
            if len(self.list_cameras) > 1:
                ComBox_cameras.addItems(self.list_cameras)

            elif len(self.list_cameras) == 1:
                ComBox_cameras.addItem(self.list_cameras[0])

    def Construct_Iluminator(self, puerto):

        if puerto == 'VirtualIluminator':

            self.Iluminator_MultiSpectral = Virtual_Iluminator_MultiSpectral('virtual')
            self.iluminator_init = True

        else:

            Iluminator = Fun_Ad.indetify_iluminator(puerto)

            if Iluminator == 'No device identify':

                self.App.Stacked_Pages.page_corona.lb_init_c_error.setText("Error al iniciar el Iluminador")

            if Iluminator == 'MultiSpectralCrown':

                self.Iluminator_MultiSpectral = MultiespectralCrown(puerto)
                self.iluminator_init = True

            if Iluminator == 'Iluminator_MultiSpectral':
                # Implementación futura iluminador de victor
                pass

        self.App.Barra_Principal.pb_error_conection_corona.setStyleSheet("background-color : green; border-radius: 10px")
        self.App.Barra_Principal.lb_error_conection_corona.setText("")

    def Construct_Camera(self, camera):

        if camera == 'VirtualCamera':

            self.Camera = VirtualCam()
            self.camera_init = True

        else:

            pass  # Implementación para spinakker cam

        self.App.Barra_Principal.pb_error_conection_camera.setStyleSheet("background-color : green; border-radius: 10px")
        self.App.Barra_Principal.lb_error_conection_camera.setText("")
