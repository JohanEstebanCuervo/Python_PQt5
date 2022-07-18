#!/usr/bin/python
import cv2

class VirtualCam:

    def __init__(self, pyspin_camlis, Gamma=1.25, ExposureTime=8000, Gain=0,
                 Sharpness=1800, BlackLevel=0.7, BufferMode='Continuous',
                 BufferHandlingMode='NewestOnly', TriggerSource='Line2',
                 BufferCount=3):

        print('Iniciando Camara Virtual')
        self.__init_atributes()

        if self.Set_Trigger_Mode(False):

            print('error set trigger mode configure')

        elif self.Set_Trigger_Source(TriggerSource):

            print('error set trigger source configure')

        elif self.Set_Trigger_Mode(True):

            print('error set trigger mode reconfigure ')

        elif self.Set_Gamma(Gamma):

            print('error set gamma configure')

        elif self.Set_BlackLevel(BlackLevel):

            print('error set black level configure')

        elif self.Set_Exposure_Auto(False):

            print('error set exposure auto configure')

        elif self.Set_Exposure(ExposureTime):

            print('error set exposure')

        elif self.Set_Gain_Auto(False):

            print('error set gain auto configure')

        elif self.Set_Gain(Gain):

            print('error set gain configure')

        elif self.Set_Sharpness_Auto(False):

            print('error set sharpness auto configure')

        elif self.Set_Sharpness(Sharpness):

            print('error set sharpness configure')

        elif self.Set_Buffer_Mode(BufferMode):

            print('error set buffer mode configure')

        elif self.Set_Buffer_Count(BufferCount):

            print('error set buffer count configure')

        elif self.Set_Buffer_Handling_Mode(BufferHandlingMode):

            print('error set buffer handling mode configure')

        else:

            self.__init_complete = True

    def __init_atributes(self):
        self.__gamma = None
        self.__blacklevel = None
        self.__error_config = False
        self.__init_complete = False
        self.__trigger_mode = None
        self.__exposure_auto = None
        self.__exposure = None
        self.__gain_auto = None
        self.__gain = None
        self.__sharpness_auto = None
        self.__sharpness = None
        self.__buffer_mode = None
        self.__buffer_count = None
        self.__buffer_handling_mode = None
        self.__trigger_source = None

    ##################################
    # Device info
    ##################################

    def Device_Info(self, nodemap):

        self.__device_info = []

    ################################
    # Set Funcionts
    ################################

    def Set_BlackLevel(self, blacklevel):

        self.__blacklevel = blacklevel

        return 0

    def Set_Gamma(self, gamma):

        self.__gamma = gamma

        return 0

    def Set_Gain(self, gain):

        self.__gain = gain

        return 0

    def Set_Sharpness(self, sharpness):

        self.__sharpness = sharpness

        return 0

    def Set_Exposure(self, exposure):

        self.__exposure = exposure

        return 0

    def Set_Gain_Auto(self, boolean):

        self.__gain_auto = boolean

        return 0

    def Set_Exposure_Auto(self, boolean):

        self.__exposure_auto = boolean

        return 0

    def Set_Sharpness_Auto(self, boolean):

        self.__sharpness_auto = boolean

        return 0

    def Set_Trigger_Mode(self, boolean):

        self.__trigger_mode = boolean

        return 0

    def Set_Trigger_Source(self, line):

        if line == 'Software':

            pass

        elif line == 'Line0':

            pass

        elif line == 'Line1':

            pass

        elif line == 'Line2':

            pass

        else:
            print('Trigger Source Invalid')
            return 1

        self.__trigger_source = line

        return 0

    def Set_Buffer_Mode(self, mode):

        if mode == 'Continuous':

            pass

        elif mode == 'SingleFrame':

            pass

        elif mode == 'MultiFrame':

            pass

        else:
            print('Buffer Mode Invalid')
            return 1

        self.__buffer_mode = mode

        return 0

    def Set_Buffer_Count(self, numbuffer):
        max_buffer_count = 100
        numbuffer = min(max_buffer_count, numbuffer)

        self.__buffer_count = numbuffer

        return 0

    def Set_Buffer_Handling_Mode(self, mode):

        if mode == 'NewestFirst' or mode == 'NewestOnly' or mode == 'OldestFirst' or mode == 'OldestFirstOverwrite':

            pass

        else:
            print('buffer handling mode invalid')
            return 1

        self.__buffer_handling_mode = mode

        return 0

    #############################################
    # Mode Functions
    ############################################
    def Mode_Acquisition_Multispectral(self):

        self.Set_Gain_Auto(False)
        self.Set_Gain(self.__gain)
        self.Set_Sharpness_Auto(False)
        self.Set_Sharpness(self.__sharpness)
        self.Set_Exposure_Auto(False)
        self.Set_Exposure(self.__exposure)

        self.Set_Trigger_Mode(True)

    def Mode_Acquisition_Video(self):

        self.Set_Gain_Auto(True)
        self.Set_Sharpness_Auto(True)
        self.Set_Exposure_Auto(True)
        self.Set_Trigger_Mode(False)

    def Acquire_Image(self, nombre):

        pass  # Agregar Funcionalidad para copiar una imagen

    def Init_Acquisition(self):

        pass

    def End_Acquisition(self):

        pass

    ###################################
    # Get Funcitons
    ###################################

    def get_device_info(self):

        return self.__device_info

    def get_init_complete(self):

        return self.__init_complete

    def get_error_config(self):

        return self.__error_config

    def get_trigger_mode(self):

        return self.__trigger_mode

    def get_exposure_auto(self):

        return self.__exposure_auto

    def get_gain_auto(self):

        return self.__gain_auto

    def get_sharpness_auto(self):

        return self.__sharpness_auto

    def get_trigger_source(self):

        return self.__trigger_source

    def get_buffer_mode(self):

        return self.__buffer_mode

    def get_buffer_count(self):

        return self.__buffer_count

    def get_buffer_handling_mode(self):

        return self.__buffer_handling_mode

    def get_gain(self):

        return self.__gain

    def get_blacklevel(self):

        return self.__blacklevel

    def get_sharpness(self):

        return self.__sharpness

    def get_gamma(self):

        return self.__gamma

    def get_exposure(self):

        return self.__exposure

    ##################################
    # Special Functions
    ################################

    def Reset(self):

        pass

    def __del__(self):

        self.Mode_Acquisition_Video()
