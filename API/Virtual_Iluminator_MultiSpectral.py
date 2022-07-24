from API.Iluminator_MultiSpectral import *

class Virtual_Iluminator_MultiSpectral(Iluminator_MultiSpectral):

    """docstring for Virtual_Iluminator_MultiSpectral"""

    def __init__(self, puerto, bps=57600, time_sleep_c=0.1, timeshot=1e-2, Virtual_Mode=False):
        super(Virtual_Iluminator_MultiSpectral, self).__init__(puerto, bps, time_sleep_c, timeshot, True)

        leds = ['M01N', 'M02N', 'M03N', 'M04N', 'M05N',
                'M06N', 'M07N', 'M08N', 'M09N', 'M0AN',
                'M0BN', 'M0CN', 'M0DN', 'M0EN', 'M0FN']

        self.set_leds(leds)
        self.set_timeshot(timeshot)
        self.set_shot_message('W')

        self.pwm_leds = ["J1090K", "J2090K", "J3090K", "J4090K", "J5090K",
                         "J6090K", "J7090K", "J8090K", "J9090K", "JA090K",
                         "JB090K", "JC090K", "JD080K", "JE010K", "JF010K"]

        self.set_PWM_Leds(self.pwm_leds)
        self.set_shot_leds(3)

        self.Wavelengths = ['410', '450', '470', '490', '505',
                            '530', '560', '590', '600', '620',
                            '630', '650', '720', '840', '960']

        self.Dicts(leds)

        print('Iluminador iniciado correctamente')

    def Dicts(self, leds):

        self.leds = {}
        for i, led in enumerate(leds):
            self.leds[led] = i

        get

