import serial
import time

from API.Iluminator_MultiSpectral import *

class MultiSpectral_Crown(Iluminator_MultiSpectral):

    """docstring for Corona_Multiespectral"""

    def __init__(self, puerto, bps=57600, time_sleep_c=0.1, timeshot=1e-2, Virtual_Mode=False):
        super(Corona_Multiespectral, self).__init__(puerto, bps, time_sleep_c, timeshot, Virtual_Mode)

        leds = ['M01N', 'M02N', 'M03N', 'M04N', 'M05N',
                'M06N', 'M07N', 'M08N', 'M09N', 'M0AN',
                'M0BN', 'M0CN', 'M0DN', 'M0EN', 'M0FN']

        self.set_leds(leds)
        self.__timeshot = timeshot
        self.set_shot_message('W')

        pwm_leds = ["J1090K", "J2090K", "J3090K", "J4090K", "J5090K",
                    "J6090K", "J7090K", "J8090K", "J9090K", "JA090K",
                    "JB090K", "JC090K", "JD080K", "JE010K", "JF010K"]

        self.set_PWM_Leds(pwm_leds)
        self.set_shot_leds(3)
        message = "T006014001U"
        self.set_shot_time_trigger_flash_timeout(message)

        self.Wavelengths = ['410', '450', '470', '490', '505', '530', '560', '590', '600',
                            '620', '630', '650', '720', '840', '960']

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
