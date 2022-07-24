from API.VirtualComunication import *
import serial
import time


class Iluminator_MultiSpectral:
    """docstring for Iluminator_MultiSppectral"""

    def __init__(self, puerto, bps=57600, time_sleep_c=0.1, timeshot=1e-2, Virtual_Mode=False):
        print("Iniciando Corona_Multiespectral")
        self.__timesleepc = time_sleep_c
        self.__shot_message = None
        self.__timeshot = None
        self.__correct_tx = b'O'
        self.__PWM_leds = None
        self.__leds = None
        self.__shot_time_trigger = None
        self.__shot_time_timeout = None
        self.__shot_mode = None
        self.__shot_time_flash = None

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

        message = "T006014001U"
        self.set_shot_time_trigger_flash_timeout(message)

        print('Comunicacion Correcta')

    #################################
    # SET functions
    #################################
    def set_shot_time_trigger_flash_timeout(self, message):

        if self.tx_msg(message):

            print("Error al configurar los tiempos de la corona")
            return 1

        else:

            self.__shot_mode = message[1]
            self.__shot_time_trigger = message[2:4]
            self.__shot_time_flash = message[4:7]
            self.__shot_time_timeout = message[7:10]

            return 0

    def set_shot_mode(self, message):

        if self.tx_msg(message):

            print("Error al configurar shot mode")
            return 1

        else:

            self.__shot_mode = message

            return 0

    def set_shot_time_trigger(self, message):

        if self.tx_msg(message):

            print("Error al configurar time trigger")
            return 1

        else:

            self.__shot_time_trigger = message
            return 0


    def set_shot_time_flash(self, message):

        if self.tx_msg(message):

            print("Error al configurar tiempo de flash")
            return 1

        else:

            self.__shot_time_flash = message
            return 0


    def set_shot_time_timeout(self, message):

        if self.tx_msg(message):

            print("Error al configurar el tiempo muerto")
            return 1

        else:

            self.__shot_time_timeout = message


    def set_shot_led(self, index):

        if self.tx_msg(self.__leds[index]):

            print("Error al configurar el led " + str(index + 1) + " en el iluminador")
            return 1

    def set_PWM_Leds(self, pwm_leds):

        self.__PWM_leds = pwm_leds

        return 0

    def set_shot_message(self, message):

        self.__shot_message = message

    def set_time_sleepc(self, time):  # Float Number, Seconds

        self.__timesleepc = time

    def set_timeshot(self, timeshot):

        self.__timeshot = timeshot

    def set_leds(self, leds):
        self.__leds = leds

    def set_correct_tx(self, correct_tx):  # Correct mensaje en string
        self.__correct_tx = correct_tx.encode('utf-8')

    #########################

    # GET Functions

    #########################

    def get_comunication_state(self):

        return self.__comunication_state

    def get_leds(self):

        return self.__leds

    def get_PWM_leds(self):

        return self.__PWM_leds

    def get_time_sleepc(self):

        return self.__timesleepc

    def get_shot_message(self):

        return self.__shot_message

    def get_shot_mode(self):

        return self.__shot_mode

    def get_shot_time_trigger(self):

        return self.__shot_time_trigger

    def get_shot_time_flash(self):

        return self.__shot_time_flash

    def get_shot_time_out(self):

        return self.__shot_time_timeout

    def get_timeshot(self):

        return self.__timeshot

    ##############################
    # Methods
    ##############################

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
            self.__comunication.write(self.__shot_message.encode('utf-8'))
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
