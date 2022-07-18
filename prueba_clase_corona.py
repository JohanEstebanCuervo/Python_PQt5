from clases_VM import *

from Funciones_Adquisicion import *


puerto = Serial_Port_Select()
corona = Corona_Multiespectral(puerto,time_sleep_c=1e-1)

corona.shot()

corona.set_shot_time_trigger('01')

corona.set_shot_time_timeout('915')
print(corona.get_shot_time_out())