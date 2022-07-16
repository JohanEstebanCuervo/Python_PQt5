from API.Flea3Cam_API import *
from API.MultiespectralCrown_API import *
from API.ColorReproduction_API import *

import methods.Funciones_Adquisicion as Fun_Ad

from PyQt5.QtCore import QDir, QTimer
import PySpin
import subprocess


class Core_App:
    """docstring for Core_App"""
    def __init__(self,App):
        self.App = App

        # carpeta temporal
        subprocess.run('md temp', shell=True)
    ##########################################
    # timer para actualizacion del boton
    ##########################################

        self.timer = QTimer()
        self.timer.timeout.connect(self.Check_Conection)
        self.timer.start(2000)
        self.corona_init = False

    def Check_Conection(self):
        self.Update_list_ports()

        if self.corona_init:
            
            bandera = 0
            for port in self.list_ports:
                if(port == self.App.Stacked_Pages.page_corona.lb_sc_port.text()):
                    bandera = 1
                    break

            if bandera == 0:
                self.corona_init = False
                self.pb_error_conection_corona.setStyleSheet("background-color : red; border-radius: 10px")
                self.lb_error_conection_corona.setText("Corona desconectada")
                self.fm_init_corona.show()
                self.fm_settings_corona.hide()

    def Update_list_ports(self,Update_cb_listPort=False):
        self.list_ports = Fun_Ad.Serial_Port_Select(terminal=False)
        self.list_ports.append('VirtualIluminator')

        if Update_cb_listPort:
            self.App.Stacked_Pages.page_corona.cb_listPort.clear()

            if len(self.list_ports) > 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItems(self.list_ports)

            elif len(self.list_ports) == 1:
                self.App.Stacked_Pages.page_corona.cb_listPort.addItem(list_ports[0])