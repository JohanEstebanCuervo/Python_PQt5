import os
import numpy as np
import methods.Functions_ColorReproduction as fcr


class Color_Reprocution:

    """docstring for ColorReprocution"""

    def __init__(self):

        self.__Init_Variables()

    def __Init_Variables(self):

        self.__images = None
        self.__Mask = None
        self.__wavelength = None
        self.__cie_1931 = None
        self.__illuminant_d65 = None
        self.__select_wavelength = None
        self.__size_image = None

    def Load_Capture(self, file, Num_Wave, start=0):

        listing = os.listdir(file)

        listing = listing[start:start + Num_Wave]

        self.__images, self.__size_image = fcr.Read_Capture(file, listing)

        self.__wavelength = fcr.Read_Wavelength_Capture(listing)

        # self.__cie_1931 = fcr.Read_CIE1931_XYZ(self.__wavelength)

        self.__cie_1931 = np.array([
                                   [410, 0.043510, 0.001210, 0.207400],
                                   [450, 0.336200, 0.038000, 1.772110],
                                   [470, 0.195360, 0.090980, 1.287640],
                                   [490, 0.032010, 0.208020, 0.465180],
                                   [505, 0.002400, 0.407300, 0.212300],
                                   [530, 0.165500, 0.862000, 0.042160],
                                   [560, 0.594500, 0.995000, 0.003900],
                                   [590, 1.026300, 0.757000, 0.001100],
                                   [600, 1.062200, 0.631000, 0.000800],
                                   [620, 0.854450, 0.381000, 0.000190],
                                   [630, 0.642400, 0.265000, 0.000050],
                                   [650, 0.283500, 0.107000, 0.000000],
                                   [720, 0.002899, 0.001047, 0.000000]])

        self.__illuminant_d65 = np.array([
                                         [410, 91.486000],
                                         [450, 117.00800],
                                         [470, 114.86100],
                                         [490, 108.81100],
                                         [505, 108.57800],
                                         [530, 107.68900],
                                         [560, 100.00000],
                                         [590, 88.685600],
                                         [600, 90.006200],
                                         [620, 87.698700],
                                         [630, 83.288600],
                                         [650, 80.026800],
                                         [720, 61.604000]])
