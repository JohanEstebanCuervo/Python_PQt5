import os
import numpy as np
import methods.Functions_ColorReproduction as fcr
import pandas as pd


class ColorReproduction:

    """docstring for ColorReprocution"""

    def __init__(self, **kwargs):

        self.__Init_Variables(kwargs)

    def __Init_Variables(self, *args):
        self.images = None
        self.mask = None
        self.wavelengths = None
        self.cie_1931 = None
        self.illuminant_d65 = None
        self.select_wavelengths = 'ALL'
        self.size_image = None
        self.pesos_ecu = None

        Dictionary = args[0]
        Keys = list(Dictionary.keys())

        for key in Keys:
            if key == 'images':

                self.images = Dictionary[key]

            elif key == 'mask':

                self.mask = Dictionary[key]

            elif key == 'mask':

                self.wavelengths = Dictionary[key]
                self.Charge_CIE()

            else:
                print(key + ': No es un argumento posible argumento no tomado')

    def Charge_CIE(self):
        nombre = 'data/CIETABLES.xls'
        hoja = pd.read_excel(nombre, skiprows=4, sheet_name='Table4')

        cie = np.array(hoja.iloc[: - 1, :4])

        wavelengths = list(cie[:, 0])

        self.cie_1931 = []
        for wavelength in self.wavelengths:
            if wavelength <= 780:
                index = wavelengths.index(wavelength)
                self.cie_1931.append(cie[index])
            else:
                self.cie_1931.append([wavelength, 0, 0, 0])

        self.cie_1931 = np.array(self.cie_1931)

        nombre = 'data/CIETABLES.xls'
        hoja = pd.read_excel(nombre, skiprows=4, sheet_name='Table1')

        d65 = np.array(hoja.iloc[:, [0, 2]])

        wavelengths = list(d65[:, 0])

        self.illuminant_d65 = []
        for wavelength in self.wavelengths:
            if wavelength <= 780:
                index = wavelengths.index(wavelength)
                self.illuminant_d65.append(d65[index])
            else:
                self.illuminant_d65.append([wavelength, 0])

        self.illuminant_d65 = np.array(self.illuminant_d65)

    def Load_Capture(self, file, Num_Wave, start=0):

        listing = os.listdir(file)

        listing = listing[start:start + Num_Wave]

        self.images, self.size_image = fcr.Read_Capture(file, listing)

        if self.wavelengths is None:
            self.wavelengths = fcr.Read_Wavelength_Capture(listing)

        self.Charge_CIE()

    def ReproduccionCie1931(self):

        if (self.select_wavelengths == 'ALL'):
            select_wavelengths = range(np.shape(self.images)[0])

        else:
            select_wavelengths = []
            for wavelength in self.select_wavelengths:
                index = self.wavelengths.index(wavelength)
                select_wavelengths.append(index)

        if self.pesos_ecu is None:
            pesos_ecu = np.ones(len(self.images))

        else:
            pesos_ecu = self.pesos_ecu

        XYZ2RGB = np.array([[3.2406, -1.5372, -0.4986],
                            [-0.9689, 1.8758, 0.0415],
                            [0.0557, -0.2040, 1.0570]])

        # Coeficientes
        Coef = (self.cie_1931[select_wavelengths, 1:] * (np.ones((3, 1)) * self.illuminant_d65[select_wavelengths, 1].T).T).T
        N = np.sum(Coef, axis=1)

        # Reproduccion de color usando CIE

        xyz = np.dot(Coef, (self.images[select_wavelengths, :].T * pesos_ecu).T).T
        xyz = xyz / N[1]

        rgb = fcr.recorte(np.dot(XYZ2RGB, xyz.T).T)
        shape_imag = list(self.size_image)
        shape_imag.append(3)
        im_RGB = np.reshape(rgb, shape_imag)

        return im_RGB
