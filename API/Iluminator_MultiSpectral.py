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

    #################################
    # SET functions
    #################################

    def set_shot_mode(self, value):

        try:
            val = int(value)

            if val != 0 and val != 1:
                print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
                return 1

        except:

            print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
            return 1

        message = 'T' + str(val) + self.__shot_time_trigger + self.__shot_time_flash + self.__shot_time_timeout + 'U'

        if self.set_shot_time_trigger_flash_timeout(message):
            print('Error en la configuración del tiempo del modo de disparo')
            return 1

        else:

            return 0

    def set_shot_time_trigger(self, value):

        try:

            int(value)

        except:

            print("Valor incorrecto el mensaje solo debe contener 2 digitos")
            return 1

        if len(value) == 2:

            message = 'T' + self.__shot_mode + value + self.__shot_time_flash + self.__shot_time_timeout + 'U'

            if self.set_shot_time_trigger_flash_timeout(message):

                print('Error en la configuración del tiempo de trigger')
                return 1

            else:

                return 0

        else:

            print("Valor incorrecto se debe ingresar 2 digitos para un valor correcto de tiempo")
            return 1


    def set_shot_time_flash(self,value):

        try:

            int(value)

        except:

            print("Valor incorrecto el mensaje solo debe contener 3 digitos")
            return 1

        if len(value) == 3:

            message = 'T' + self.__shot_mode + self.__shot_time_trigger + value + self.__shot_time_timeout + 'U'

            if self.set_shot_time_trigger_flash_timeout(message):
                print('Error en la configuración del tiempo de flash')
                return 1

            else:

                return 0

        else:
            print("Valor incorrecto se debe ingresar 3 digitos para un valor correcto de tiempo")
            return 1

    def set_shot_time_timeout(self, value):

        try:

            int(value)

        except:

            print("Valor incorrecto el mensaje solo debe contener 3 digitos")
            return 1

        if len(value) == 3:

            message = 'T' + self.__shot_mode + self.__shot_time_trigger + self.__shot_time_flash + value + 'U'

            if self.set_shot_time_trigger_flash_timeout(message):
                print('Error en la configuración del tiempo muerto')
                return 1

            else:

                return 0

        else:

            print("Valor incorrecto se debe ingresar 3 digitos para un valor correcto de tiempo")
            return 1

    def set_shot_leds(self, pos_led):

        if self.tx_msg(self.__leds[pos_led]):

            print("Error al configurar el led " + str(pos_led + 1) + " en la corona")
            return 1

    def set_PWM_Leds(self, pwm_leds):

        for pwm_led in pwm_leds:

            if self.tx_msg(pwm_led):
                print("Error al configurar el PWM de la corona")
                return 1

        self.__PWM_leds = pwm_leds

        return 0

    def set_shot_message(self, message):

        self.__shot_message = message

    def set_time_sleepc(self, time):

        self.__timesleepc = time

    def set_timeshot(self, timeshot):

        self.__timeshot = timeshot

    def set_leds(self,leds):
        self.__leds = leds

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

            if self.set_shot_leds(i):

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
