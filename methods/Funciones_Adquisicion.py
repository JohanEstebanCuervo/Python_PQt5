#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import PySpin
import serial
import time

# Esta funcion busca los puertos serial en uso. En caso de conocer el puerto serial se puede cambiar el parametro port='Nombre_del_puerto'


def Serial_Port_Select(port=0, terminal=True):

    if port != 0:
        return port  # retorna el puerto en caso de que sea conocido

    x = str(subprocess.check_output('python -m serial.tools.list_ports', shell=True), 'UTF-8')
    lista = []
    inicio = 0
    i = x.find(' ', inicio, len(x))

    while i > 0:
        lista.append(x[inicio:i])
        inicio = x.find('\n', inicio, len(x)) + 1
        i = x.find(' ', inicio, len(x))

    if len(lista) == 0:
        print("No hay puertos seriales conectados")
        return 1

    else:

        if terminal:
            print("Puertos: ")
            if len(lista) == 1:
                print(lista[0])

                return lista[0]

            for i in range(len(lista)):
                print(str(i + 1) + '. ' + lista[i])
            correct = 0
            while correct == 0:
                try:
                    sel = int(input("Seleccione numero de puerto: "))
                    if sel > 0 and sel <= len(lista):
                        correct = 1

                    else:
                        print("Valor erroneo ingrese el numero correspondiene al puerto")

                except:
                    print("Valor erroneo ingrese el numero correspondiene al puerto")

            return lista[sel - 1]

        else:
            return lista


def Cameras_List():

    system = PySpin.System.GetInstance()

    # Retrieve list of cameras from the system
    cam_list = system.GetCameras()

    num_cameras = cam_list.GetSize()

    if num_cameras == 0:

        cam_list.Clear()
        system.ReleaseInstance()

        return 1

    cam_name_list = []
    for i in range(num_cameras):

        cam = cam_list[i]

        if cam.TLDevice.DeviceModelName.GetAccessMode() == PySpin.RO:
            cam_name_list.append(str(i + 1) + " " + cam.TLDevice.DeviceModelName.ToString())

        else:
            cam_name_list.append(str(i + 1) + " " + 'unName camera')

        del cam

    cam_list.Clear()
    system.ReleaseInstance()

    return cam_name_list


def indetify_iluminator(puerto):

    try:
        comunication = serial.Serial(puerto, 57600)
        message = 'Version_Firmware'
        comunication.write(message.encode('utf-8'))
        time.sleep(0.3)

        if comunication.in_waiting > 0:

            rx = comunication.read()
            rx = rx.decode('utf-8')
            if rx == 'Iluminator_MultiSpectral':
                comunication.close()
                return 'Iluminator_MultiSpectral'

        message = 'W'
        comunication.write(message.encode('utf-8'))
        time.sleep(0.3)

        if comunication.in_waiting > 0:

            rx = comunication.read()
            rx = rx.decode('utf-8')
            if rx == 'O':
                comunication.close()
                return 'MultiSpectralCrown'

        else:
            comunication.close()
            return 'No device identify'

    except:

        print('Error en la identificación de la corona. Comunicación Fracasada')

        return 'No device identify'


if __name__ == '__main__':
    nombre = Serial_Port_Select()

    print(nombre)
