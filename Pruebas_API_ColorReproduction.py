import numpy as np
from API.ColorReproduction_API import *
import methods.Functions_ColorReproduction as fcr
x = np.array([4, 5, 7])
ColorRepro = ColorReproduction()

file = 'C:/Users/cuerv/OneDrive/Documentos/Color_Reproduction_Multiespectral_Images/Informacion/patron'
N = 15

ColorRepro.Load_Capture(file, N)

pesos_ecu = np.array([5.16994, 1.34287, 2.78332, 1.61328, 2.18158, 1.74666, 1.59841,
                      3.80323, 2.32905, 1.18668, 1.87999, 2.09624, 1, 1, 1])

ColorRepro.pesos_ecu = pesos_ecu

imagen = np.array(ColorRepro.ReproduccionCie1931()).astype('float')

fcr.imshow('reproducción de color', imagen)

x = []

print(len(x))