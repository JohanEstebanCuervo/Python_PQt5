from API.Virtual_Iluminator_MultiSpectral import *

iluminador = Virtual_Iluminator_MultiSpectral('virtual')

iluminador.config_leds([410],'PWM_val',[23.433])

print(iluminador.leds[410])
