from API.ColorReproduction_API import *
from methods import Funciones_Adquisicion as fs
import numpy as np
import cv2

pesos = [157, 157, 160, 162, 157, 173, 171, 186]
pesos = np.divide(243*np.ones(len(pesos)), pesos)
print(pesos)

colorr = ColorReproduction()

colorr.wavelengths = [450, 500, 525, 550, 620, 660, 740, 850]

ruta = r'Imagenes Pruebas\2022_6_8_19_56_26,5\agpic'
colorr.Load_Capture(ruta, 8)
colorr.Charge_CIE()
imagen = colorr.ReproduccionCie1931()*255
imagen = imagen.astype('uint8')
print(type(imagen))
print(np.shape(imagen))

cv2.imwrite(ruta + '/imagen.bmp', imagen)
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows() 
