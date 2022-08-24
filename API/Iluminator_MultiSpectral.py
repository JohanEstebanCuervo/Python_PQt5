from API.VirtualComunication import *
import serial
import time


class Iluminator_MultiSpectral:
    """docstring for Iluminator_MultiSppectral"""

    def __init__(self, puerto, bps=57600, time_sleep_c=0.1, timeshot=1e-2, Virtual_Mode=False):
        print("Iniciando Corona_Multiespectral")
        self.__timesleepc = time_sleep_c
        self.__timeshot = timeshot
        self.__correct_tx = b'O'

        try:
            self.__comunication = serial.Serial(puerto, bps)
            self.__comunication_state = True

        except:

            if Virtual_Mode:
                self.__comunication = VirtualComunication()
                self.__comunication_state = True

            else:
                self.__comunication_state = False
                print("No se ejecuto el puerto serial")

        print('Comunicacion Correcta')

    ##############################
    # Methods
    ##############################

    def config(self, message):

        if self.tx_msg(message):
            print('Configuracion: ' + str(message) + ' NO realizada')
            return 1

        else:
            print('Configuracion: ' + str(message) + ' realizada')
            return 0

    def get_comunication_state(self):

        return self.__comunication_state

    def set_shot_led(self, index):

        if self.tx_msg(self.__leds[index]):

            print("Error al configurar el led " + str(index + 1) + " en la corona")
            return 1

        else:

            return 0

    def set_time_sleepc(self, time):

        self.__timesleepc = time

    def set_timeshot(self, timeshot):

        self.__timeshot = timeshot

    def set_PWM_Leds(self, pwm_leds):

        for pwm_led in pwm_leds:

            if self.tx_msg(pwm_led):
                print("Error al configurar el PWM de la corona: " + str(pwm_led))
                return 1

        return 0

    def set_leds(self, leds):
        self.__leds = leds

    def set_shot_message(self, message):

        self.__shot_message = message.encode('utf-8')

    def set_correct_tx(self, val):

        self.__correct_tx = val.encode('utf-8')

    def tx_msg(self, message, comp=True):
        if self.__comunication_state:
            bandera = 0
            iteraciones = 0
            # Si no se necesita comprobacion solo ingresa al while 1 vez
            if ~comp:
                iteraciones = 4

            while bandera == 0 and iteraciones < 5:
                try:
                    self.__comunication.write(message.encode('utf-8'))
                    time.sleep(self.__timesleepc)

                    Check = ''
                    if self.__comunication.in_waiting > 0:

                        Check = self.__comunication.read()

                    if Check == self.__correct_tx:
                        bandera = 1

                    iteraciones += 1

                except:

                    print("error en la comunicacion")
                    self.__comunication_state = False
                    return 1

            if bandera == 0 and comp:
                print("No se recibio respuesta")
                return 1

            return 0

        else:
            print("Comunicación no iniciada No es posible enviar el mensaje")
            return 1

    def shot(self):

        if self.__comunication_state:
            self.__comunication.write(self.__shot_message)
            time.sleep(self.__timesleepc)

            if self.__comunication.in_waiting > 0:
                Check = self.__comunication.read()

                if Check == self.__correct_tx:

                    return 0

                else:
                    print("Es posible que el disparo no se halla realizado")
                    return 2  # Mejorar el return

            else:
                print("No se recibio respuesta de la corona")

                return 1

    def shot_multispectral(self):

        for i in range(len(self.__leds)):

            if self.set_shot_led(i):

                return 1

            if self.shot():

                return 1

            time.sleep(self.__timeshot)

        return 0

    ##############################
    # Especial Functions
    ##############################

    def __del__(self):

        if self.__comunication_state:

            self.__comunication.close()
