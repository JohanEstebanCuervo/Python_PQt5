def attributes_iluminator():
    attributes = {'time_flash': {'value': None, 'message': None, 'min': 0.1, 'max': 99.9},
                  'time_trigger': {'value': None, 'message': None, 'min': 0.1, 'max': 9.9},
                  'time_out': {'value': None, 'message': None, 'min': 0.01, 'max': 9.99},
                  'shot_mode': {'value': None, 'message': None, 'min': 0, 'max': 1},
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