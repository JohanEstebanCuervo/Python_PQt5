from API.Iluminator_MultiSpectral import *


def attributes_iluminator():
    attributes = {'time_flash': {'value': 1.4, 'message': "T006014001U", 'min': 0.1, 'max': 99.9},
                  'time_trigger': {'value': 0.6, 'message': "T006014001U", 'min': 0.1, 'max': 9.9},
                  'time_out': {'value': 0.01, 'message': "T006014001U", 'min': 0.01, 'max': 9.99},
                  'shot_mode': {'value': 0, 'message': "T006014001U", 'min': 0, 'max': 1},
                  'time_sleep': {'value': None, 'min': 0.00001, 'max': 0.5},
                  'time_shot': {'value': None, 'min': 0.00001, 'max': 2},
                  'shot_message': {'value': None}}

    leds = {410: {'active': True, 'PWM_val': 90, 'PWM_message': "J1090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M01N'},
            450: {'active': True, 'PWM_val': 90, 'PWM_message': "J2090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M02N'},
            470: {'active': True, 'PWM_val': 90, 'PWM_message': "J3090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M03N'},
            490: {'active': True, 'PWM_val': 90, 'PWM_message': "J4090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M04N'},
            505: {'active': True, 'PWM_val': 90, 'PWM_message': "J5090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M05N'},
            530: {'active': True, 'PWM_val': 90, 'PWM_message': "J6090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M06N'},
            560: {'active': True, 'PWM_val': 90, 'PWM_message': "J7090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M07N'},
            590: {'active': True, 'PWM_val': 90, 'PWM_message': "J8090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M08N'},
            600: {'active': True, 'PWM_val': 90, 'PWM_message': "J9090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M09N'},
            620: {'active': True, 'PWM_val': 90, 'PWM_message': "JA090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0AN'},
            630: {'active': True, 'PWM_val': 90, 'PWM_message': "JB090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0BN'},
            650: {'active': True, 'PWM_val': 90, 'PWM_message': "JC090K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0CN'},
            720: {'active': True, 'PWM_val': 80, 'PWM_message': "JD080K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0DN'},
            840: {'active': True, 'PWM_val': 10, 'PWM_message': "JE010K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0EN'},
            960: {'active': True, 'PWM_val': 10, 'PWM_message': "JF010K",
                  'PWM_min': 1, 'PWM_max': 100, 'led_message': 'M0FN'}}

    return attributes, leds


class Virtual_Iluminator_MultiSpectral(Iluminator_MultiSpectral):

    """docstring for Virtual_Iluminator_MultiSpectral"""

    def __init__(self, puerto, bps=57600, time_sleep_c=0.1, timeshot=1e-2):
        super(Virtual_Iluminator_MultiSpectral, self).__init__(puerto, bps, time_sleep_c, timeshot, True)

        self.set_shot_message('W')
        self.attributes, self.leds = attributes_iluminator()

        if self.config_PWM():
            pass
        elif self.config_list_leds():
            pass
        elif self.set_shot_led(3):
            pass
        else:
            print('Iluminador iniciado correctamente')

    def config_attributes(self, attribute, value):

        if attribute != 'shot_message':
            if value < self.attributes[attribute]['min']:
                value = self.attributes[attribute]['min']
            if value > self.attributes[attribute]['max']:
                value = self.attributes[attribute]['max']

        if attribute == 'time_flash':
            value_str = str(int(value * 10 // 1))
            if len(value_str) != 3:
                dif = 3 - len(value_str)
                if dif == 1:
                    value_str = '0' + value_str
                if dif == 2:
                    value_str = '00' + value_str
            message = list(self.attributes[attribute]['message'])
            message[4:7] = list(value_str)
            message = "".join(message)

        if attribute == 'time_trigger':
            value_str = str(int(value * 10 // 1))
            if len(value_str) != 2:
                value_str = '0' + value_str
            message = list(self.attributes[attribute]['message'])
            message[2:4] = list(value_str)
            message = "".join(message)

        if attribute == 'time_out':
            value_str = str(int(value * 100 // 1))
            if len(value_str) != 3:
                dif = 3 - len(value_str)
                if dif == 1:
                    value_str = '0' + value_str
                if dif == 2:
                    value_str = '00' + value_str
            message = list(self.attributes[attribute]['message'])
            message[7:10] = list(value_str)
            message = "".join(message)

        if attribute == 'shot_mode':
            value_str = str(int(value // 1))
            message = list(self.attributes[attribute]['message'])
            message[1] = value_str
            message = "".join(message)

        if (attribute == 'time_flash' or attribute == 'time_trigger'
            or attribute == 'time_out' or attribute == 'shot_mode'):
            self.attributes[attribute]['value'] = value
            self.attributes['time_flash']['message'] = message
            self.attributes['time_trigger']['message'] = message
            self.attributes['time_out']['message'] = message
            self.attributes['shot_mode']['message'] = message

            if self.config(message):
                return 1

        if attribute == 'shot_message':

            self.attributes['shot_message']['value'] = str(value)
            self.set_shot_message(str(value))

        if attribute == 'time_sleep':

            self.attributes['time_sleep']['value'] = value
            self.set_time_sleepc(value)

        if attribute == 'time_shot':

            self.attributes['time_shot']['value'] = value
            self.set_timeshot(value)

        return 0

    def config_leds(self, leds, attribute, values):
        if attribute == 'active':

            for i, led in enumerate(leds):
                value = values[i]
                if value is False or value is True:
                    self.leds[led]['active'] = value
                else:
                    print('value no compatible con el dato')
                    return 1

            self.config_list_leds()

        if attribute == 'PWM_val':
            for i, led in enumerate(leds):
                value = values[i]
                value = int(value // 1)
                if value < self.leds[led]['PWM_min']:
                    value = self.leds[led]['PWM_min']

                elif value > self.leds[led]['PWM_max']:
                    value = self.leds[led]['PWM_max']

                self.leds[led]['PWM_val'] = value

                value = str(value)

                if len(value) != 3:

                    dif = 3 - len(value)
                    if dif == 1:
                        value = '0' + value

                    if dif == 2:
                        value = '00' + value

                msg = list(self.leds[led]['PWM_message'])
                msg[2:5] = list(value)
                msg = "".join(msg)
                self.leds[led]['PWM_message'] = msg

            if self.config_PWM():
                return 1

        return 0

    def config_PWM(self):

        leds = list(self.leds.keys())
        pwm_list = []

        for led in leds:
            if self.leds[led]['active']:
                pwm_message = self.leds[led]['PWM_message']
                pwm_list.append(pwm_message)

        if self.set_PWM_Leds(pwm_list):

            return 1

        return 0

    def config_list_leds(self):

        leds = list(self.leds.keys())
        leds_list = []

        for led in leds:
            if self.leds[led]['active']:
                led_message = self.leds[led]['led_message']
                leds_list.append(led_message)

        if self.set_leds(leds_list):
            return 1

        return 0
