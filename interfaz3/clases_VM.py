import serial
import time
import PySpin
import matplotlib.pyplot as plt
import os
import cv2


import Functions_ColorReproduction as fcr


class Corona_Multiespectral:

	"""docstring for Corona_Multiespectral"""
	def __init__(self, puerto,bps=57600,time_sleep_c=0.1,timeshot=1e-2):
		print("Iniciando Corona_Multiespectral")
		self.__timesleepc = time_sleep_c
		self.__shot_message = 'W'
		self.__leds = ['M01N','M02N','M03N','M04N','M05N','M06N','M07N','M08N','M09N','M0AN','M0BN','M0CN','M0DN','M0EN','M0FN']
		self.__timeshot = timeshot
		try:		
			self.__comunication = serial.Serial(puerto,bps)
			self.__comunication_state=True
		except:

			self.__comunication_state=False
			print("No se ejecuto el puerto serial")


		pwm_leds = ["J1090K","J2090K","J3090K","J4090K","J5090K","J6090K","J7090K","J8090K","J9090K","JA090K","JB090K","JC090K","JD080K","JE010K","JF010K"]
		self.set_PWM_Leds(pwm_leds)
		self.set_shot_leds(3)
		message = "T006014001U"
		self.set_shot_time_trigger_flash_timeout(message)


	#################################

	# SET functions

	#################################
	def set_shot_time_trigger_flash_timeout(self,message):
		
		if self.tx_msg(message):

			print("Error al configurar los tiempos de la corona")
			return 1

		else:
			self.__shot_mode = message[1]
			self.__shot_time_trigger= message[2:4]
			self.__shot_time_flash = message[4:7]
			self.__shot_time_timeout =message[7:10]

			return 0


	def set_shot_mode(self,value):
		try:
			val=int(value)

			if val!=0 and val!=1:
				print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
				return 1

		except:
			print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
			return 1


		message =  'T'+ str(val) + self.__shot_time_trigger + self.__shot_time_flash + self.__shot_time_timeout + 'U'


		if self.set_shot_time_trigger_flash_timeout(message):
			print('Error en la configuración del tiempo del modo de disparo')
			return 1

		else:

			return 0 


	def set_shot_time_trigger(self,value):
		try:
			int(value)
		except:
			print("Valor incorrecto el mensaje solo debe contener 2 digitos")
			return 1

		if len(value)==2:

			message =  'T'+ self.__shot_mode + value + self.__shot_time_flash + self.__shot_time_timeout + 'U'

			if self.set_shot_time_trigger_flash_timeout(message):
				print('Error en la configuración del tiempo de trigger')
				return 1

			else:

				return 0 

		else:
			print("Valor incorrecto se debe ingresar 2 digitos para un valor correcto de tiempo")
			return 1

	def set_shot_time_flash(self,value):
		try:
			int(value)
		except:
			print("Valor incorrecto el mensaje solo debe contener 3 digitos")
			return 1

		if len(value)==3:

			message =  'T'+ self.__shot_mode + self.__shot_time_trigger + value + self.__shot_time_timeout + 'U'

			if self.set_shot_time_trigger_flash_timeout(message):
				print('Error en la configuración del tiempo de flash')
				return 1

			else:

				return 0 

		else:
			print("Valor incorrecto se debe ingresar 3 digitos para un valor correcto de tiempo")
			return 1

	def set_shot_time_timeout(self,value):
		try:
			int(value)
		except:
			print("Valor incorrecto el mensaje solo debe contener 3 digitos")
			return 1

		if len(value)==3:

			message =  'T'+ self.__shot_mode + self.__shot_time_trigger + self.__shot_time_flash + value + 'U'

			if self.set_shot_time_trigger_flash_timeout(message):
				print('Error en la configuración del tiempo muerto')
				return 1

			else:

				return 0 

		else:
			print("Valor incorrecto se debe ingresar 3 digitos para un valor correcto de tiempo")
			return 1

	def set_shot_leds(self,pos_led):

		if self.tx_msg(self.__leds[pos_led]):
				print("Error al configurar el led "+str(pos_led+1)+" en la corona")
				return 1


	def set_PWM_Leds(self,pwm_leds): #medio garantiza que la corona este configurada si despues de configurar la corona esta se desconecta pierde la configuracion

		for pwm_led in pwm_leds:
			
			if self.tx_msg(pwm_led):
				print("Error al configurar el PWM de la corona")
				return 1


		self.__PWM_leds=pwm_leds

		return 0


	def set_shot_message(self,message):

		self.__shot_message = message

	def set_time_sleepc(self,time):

		self.__timesleepc = time

	def set_timeshot(self,timeshot):

		self.__timeshot = timeshot

	#########################

	# GET Functions

	#########################

	def get_comunication_state(self):

		return self.__comunication_state

	def get_leds(self):

		return self.__leds

	def get_PWM_leds(self):

		return self.__PWM_leds

	def get_time_sleepc(self):

		return self.__timesleepc

	def get_shot_message(self):

		return self.__shot_message

	def get_shot_mode(self):

		return self.__shot_mode

	def get_shot_time_trigger(self):

		return self.__shot_time_trigger

	def get_shot_time_flash(self):

		return self.__shot_time_flash

	def get_shot_time_out(self):

		return self.__shot_time_timeout

	def get_timeshot(self):

		return self.__timeshot

	##############################

	#Methods

	##############################

	def tx_msg(self,message,comp=True):
		print(message)
		if self.__comunication_state:
			bandera=0
			iteraciones=0
			if ~comp:   #Si no se necesita comprobacion solo ingresa al while 1 vez
				iteraciones=4

			while bandera==0 and iteraciones<5 :
					try:
						self.__comunication.write(message.encode('utf-8'))
						time.sleep(self.__timesleepc)

						Check=''
						if self.__comunication.in_waiting>0:
						    
						    Check = self.__comunication.read()
						    
						if Check == b'O':
						    bandera=1

						iteraciones+=1

					except:
						print("error en la comunicacion")
						self.__comunication_state=False
						return 1

	    
			if bandera==0 and comp:
				print("No se recibio respuesta")
				return 1


			return 0

		else:
			print("Comunicación no iniciada No es posible enviar el mensaje")
			return 1


	def shot(self):

		if self.__comunication_state:
			self.__comunication.write(self.__shot_message.encode('utf-8'))
			time.sleep(self.__timesleepc)
			if self.__comunication.inWaiting()==1:    
					Check = self.__comunication.read()

					if Check==b'O':

						return 0

					else:
						print("Es posible que el disparo no se halla realizado")
						return 2

			else:
				print("No se recibio respuesta de la corona")

				return 1

	def shot_multispectral(self):

		for i in range(len(self.__leds)):

			if self.set_shot_leds(i):

				return 1

			if self.shot():

				return 1

			time.sleep(self.__timeshot)

		return 0
		


	##############################

	# Especial Functions

	##############################

	def __del__(self):

		if self.__comunication_state:

			self.__comunication.close()


class Camera_PySpin():
	"""docstring for Camera_PySpin"""
	def __init__(self,pyspin_camlis,Gamma=1.25,ExposureTime=8000,Gain=0,Sharpness=1800,BlackLevel=0.7,BufferMode='Continuous',BufferHandlingMode = 'NewestOnly',TriggerSource= 'Line2',BufferCount=3):
		try:

			self.__init_atributes()

			self.__cam = pyspin_camlis

			nodemap_tldevice = self.__cam.GetTLDeviceNodeMap()

			self.Device_Info(nodemap_tldevice)

			self.__cam.Init()

			self.__nodemap = self.__cam.GetNodeMap()

		except:
			print('Error en el inicio de la camara')
			self.__init_complete = False


		if self.Set_Trigger_Mode(False):

			print('error set trigger mode configure')

		if self.Set_Trigger_Source(TriggerSource):

			print('error set trigger source configure')

		if self.Set_Trigger_Mode(True):

			print('error set trigger mode reconfigure ')



		if self.Set_Gamma(Gamma):

			print('error set gamma configure')

		if self.Set_BlackLevel(BlackLevel):

			print('error set black level configure')

		
		if self.Set_Exposure_Auto(False):

			print('error set exposure auto configure')

		if self.Set_Exposure(ExposureTime):

			print('error set exposure')

		if self.Set_Gain_Auto(False):

			print('error set gain auto configure')
		if self.Set_Gain(Gain):

			print('error set gain configure')


		if self.Set_Sharpness_Auto(False):
			print('error set sharpness auto configure')

		if self.Set_Sharpness(Sharpness):
			print('error set sharpness configure')

		
	
		if self.Set_Buffer_Mode(BufferMode):
			print('error set buffer mode configure')

		if self.Set_Buffer_Count(BufferCount):
			print('error set buffer count configure')

		if self.Set_Buffer_Handling_Mode(BufferHandlingMode):
			print('error set buffer handling mode configure')


		self.__init_complete = True
		
	def __init_atributes(self):
		self.__gamma = None
		self.__blacklevel = None
		self.__error_config = False
		self.__init_complete = None
		self.__trigger_mode = None
		self.__exposure_auto = None
		self.__exposure = None
		self.__gain_auto = None
		self.__gain = None
		self.__sharpness_auto = None
		self.__sharpness = None
		self.__buffer_mode = None
		self.__buffer_count= None
		self.__buffer_handling_mode = None
		self.__trigger_source= None

	##################################
	#  Device info 
	##################################


	def Device_Info(self,nodemap):

	    try:
	        node_device_information = PySpin.CCategoryPtr(nodemap.GetNode('DeviceInformation'))
	        self.__device_info = []

	        if PySpin.IsAvailable(node_device_information) and PySpin.IsReadable(node_device_information):
	            features = node_device_information.GetFeatures()
	            for feature in features:
	                node_feature = PySpin.CValuePtr(feature)
	                self.__device_info.append([node_feature.GetName(), 
	                	node_feature.ToString() if PySpin.IsReadable(node_feature) else 'Node not readable'])

	        else:
	            print('Device control information not available.')

	    except PySpin.SpinnakerException as ex:
	        print('Error: %s' % ex)
	        
	        if self.__init_complete is None:
	        	self.__init_complete=False

	        else:
	        	self.__error_config= True


	################################
	# Set Funcionts
	################################

	def Set_BlackLevel(self, blacklevel):

		node_BlackLevel = PySpin.CFloatPtr(self.__nodemap.GetNode('BlackLevel'))
		if not PySpin.IsAvailable(node_BlackLevel) or not PySpin.IsWritable(node_BlackLevel):
		    print('\nUnable to set BlackLevel (float retrieval). Aborting...\n')
		    
		    if self.__init_complete is None:
		    	self.__init_complete=False

		    else:
		    	self.__error_config= True

		    return 1

		node_BlackLevel.SetValue(blacklevel)

		self.__blacklevel = blacklevel

		return 0

	def Set_Gamma(self,gamma):

		node_Gamma = PySpin.CFloatPtr(self.__nodemap.GetNode('Gamma'))
		if not PySpin.IsAvailable(node_Gamma) or not PySpin.IsWritable(node_Gamma):
		    print('\nUnable to set Gamma Time (Integer retrieval). Aborting...\n')

		    if self.__init_complete is None:
		    	self.__init_complete=False

		    else:
		    	self.__error_config= True

		    return 1

		node_Gamma.SetValue(gamma)

		self.__gamma = gamma

		return 0

	def Set_Gain(self,gain):

		node_Gain = PySpin.CFloatPtr(self.__nodemap.GetNode('Gain'))
		if not PySpin.IsAvailable(node_Gain) or not PySpin.IsWritable(node_Gain):
		    print('\nUnable to set Gain (float retrieval). Aborting...\n')

		    if self.__init_complete is None:
		        self.__init_complete=False

		    else:
		        self.__error_config= True

		    return 1

		node_Gain.SetValue(gain)

		self.__gain = gain

		return 0

	def Set_Sharpness(self,sharpness):

	    node_Sharpness = PySpin.CIntegerPtr(self.__nodemap.GetNode('Sharpness'))
	    if not PySpin.IsAvailable(node_Sharpness) or not PySpin.IsWritable(node_Sharpness):
	        print('\nUnable to set Sharpness Time (Integer retrieval). Aborting...\n')

	        if self.__init_complete is None:
	            self.__init_complete=False


	        else:
	            self.__error_config= True

	        return 1

	    node_Sharpness.SetValue(sharpness)

	    self.__sharpness = sharpness

	    return 0

	def Set_Exposure(self,exposure):

		if self.__cam.ExposureTime.GetAccessMode() != PySpin.RW:
		    print('Unable to set exposure time. Aborting...')
		    return 1

		# Ensure desired exposure time does not exceed the maximum

		exposure_time_to_set = min(self.__cam.ExposureTime.GetMax(), exposure)

		self.__cam.ExposureTime.SetValue(exposure_time_to_set)

		self.__exposure = exposure

		return 0 

	def Set_Gain_Auto(self,boolean):
		
		if boolean == self.__gain_auto:
			return 0

		node_gain_auto = PySpin.CEnumerationPtr(self.__nodemap.GetNode('GainAuto'))
		if not PySpin.IsAvailable(node_gain_auto) or not PySpin.IsWritable(node_gain_auto):
		    print('\nUnable to set Gain Auto (enumeration retrieval). Aborting...\n')

		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1


		if boolean:
		    entry_gain_auto_on = node_gain_auto.GetEntryByName('Continuous')
		    if not PySpin.IsAvailable(entry_gain_auto_on) or not PySpin.IsReadable(entry_gain_auto_on):
		        print('\nUnable to set Gain Auto (entry retrieval). Aborting...\n')

		        if self.__init_complete is None:
		            self.__init_complete = False

		        else:
		            self.__error_config= True

		        return 1

		    gain_auto_on = entry_gain_auto_on.GetValue()

		    node_gain_auto.SetIntValue(gain_auto_on)

		else:

		    entry_gain_auto_off = node_gain_auto.GetEntryByName('Off')
		    if not PySpin.IsAvailable(entry_gain_auto_off) or not PySpin.IsReadable(entry_gain_auto_off):
		        print('\nUnable to set Gain Auto (entry retrieval). Aborting...\n')

		        if self.__init_complete is None:
		            self.__init_complete = False

		        else:
		            self.__error_config= True

		        return 1

		    gain_auto_off = entry_gain_auto_off.GetValue()

		    node_gain_auto.SetIntValue(gain_auto_off)

		self.__gain_auto = boolean

		return 0

	def Set_Exposure_Auto(self,boolean):

		if boolean == self.__exposure_auto:
			return 0

		trigger_mode = self.__trigger_mode

		if trigger_mode:

			self.Set_Trigger_Mode(False)


		if self.__cam.ExposureAuto.GetAccessMode() != PySpin.RW:
		    print('Unable to disable automatic exposure. Aborting...')

		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1


		if boolean:

		    self.__cam.ExposureAuto.SetValue(PySpin.ExposureAuto_Continuous)

		else:

		    self.__cam.ExposureAuto.SetValue(PySpin.ExposureAuto_Off)

		self.__exposure_auto = boolean

		if trigger_mode:
			self.Set_Trigger_Mode(True)

		return 0

	def Set_Sharpness_Auto(self,boolean):

		if boolean == self.__sharpness_auto:
			return 0

		node_Sharpness_auto = PySpin.CEnumerationPtr(self.__nodemap.GetNode('SharpnessAuto'))
		if not PySpin.IsAvailable(node_Sharpness_auto) or not PySpin.IsWritable(node_Sharpness_auto):
		    print('\nUnable to set Sharpness Auto (enumeration retrieval). Aborting...\n')

		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1


		if boolean:
		    entry_Sharpness_auto_on = node_Sharpness_auto.GetEntryByName('Continuous')
		    if not PySpin.IsAvailable(entry_Sharpness_auto_on) or not PySpin.IsReadable(entry_Sharpness_auto_on):
		        print('\nUnable to set Sharpness Auto (entry retrieval). Aborting...\n')

		        if self.__init_complete is None:
		            self.__init_complete = False

		        else:
		            self.__error_config= True

		        return 1

		    Sharpness_auto_on = entry_Sharpness_auto_on.GetValue()

		    node_Sharpness_auto.SetIntValue(Sharpness_auto_on)

		else:

		    entry_Sharpness_auto_off = node_Sharpness_auto.GetEntryByName('Off')
		    if not PySpin.IsAvailable(entry_Sharpness_auto_off) or not PySpin.IsReadable(entry_Sharpness_auto_off):
		        print('\nUnable to set Sharpness Auto (entry retrieval). Aborting...\n')

		        if self.__init_complete is None:
		            self.__init_complete = False

		        else:
		            self.__error_config= True

		        return 1

		    Sharpness_auto_off = entry_Sharpness_auto_off.GetValue()

		    node_Sharpness_auto.SetIntValue(Sharpness_auto_off)

		self.__sharpness_auto = boolean

		return 0

	def Set_Trigger_Mode(self,boolean):

		if boolean == self.__trigger_mode:
			return 0

		if self.__cam.TriggerMode.GetAccessMode() != PySpin.RW:
		    print('Unable to disable trigger mode (node retrieval). Aborting...')

		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1


		if boolean:

		    self.__cam.TriggerMode.SetValue(PySpin.TriggerMode_On)

		else:

		    self.__cam.TriggerMode.SetValue(PySpin.TriggerMode_Off)

		self.__trigger_mode = boolean

		return 0


	def Set_Trigger_Source(self,line):

		trigger_mode = self.__trigger_mode
		if trigger_mode:

			self.Set_Trigger_Mode(False)

		if self.__cam.TriggerSource.GetAccessMode() != PySpin.RW:
		    print('Unable to get trigger source (node retrieval). Aborting...')
		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1

		self.__cam.TriggerSource.SetValue(PySpin.TriggerSelector_FrameStart)

		if line=='Software':

			self.__cam.TriggerSource.SetValue(PySpin.TriggerSource_Software)

		elif line=='Line0' :

			self.__cam.TriggerSource.SetValue(PySpin.TriggerSource_Line0)

		elif line=='Line1' :

			self.__cam.TriggerSource.SetValue(PySpin.TriggerSource_Line1)

		elif line=='Line2' :

			self.__cam.TriggerSource.SetValue(PySpin.TriggerSource_Line2)

		else:
			print('Trigger Source Invalid')
			return 1

		self.__trigger_source = line

		if trigger_mode:

			self.Set_Trigger_Mode(True)

		return 0


	def Set_Buffer_Mode(self,mode):

		if self.__cam.AcquisitionMode.GetAccessMode() != PySpin.RW:
		    print('Unable to disable acquisition mode. Aborting...')

		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1


		if mode == 'Continuous':

		    self.__cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_Continuous)

		elif mode == 'SingleFrame':

		    self.__cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_SingleFrame)

		elif mode == 'MultiFrame':

			self.__cam.AcquisitionMode.SetValue(PySpin.AcquisitionMode_MultiFrame)

		else :
			print('Buffer Mode Invalid')
			return 1


		self.__buffer_mode = mode

		return 0

	def Set_Buffer_Count(self,numbuffer):

		streaming_node = self.__cam.GetTLStreamNodeMap()
		stream_buffer_count_mode = PySpin.CEnumerationPtr(streaming_node.GetNode('StreamBufferCountMode'))
		if not PySpin.IsAvailable(stream_buffer_count_mode) or not PySpin.IsWritable(stream_buffer_count_mode):
		    print('Unable to set Buffer Count Mode (node retrieval). Aborting...\n')
		    return 1

		stream_buffer_count_mode_manual = PySpin.CEnumEntryPtr(stream_buffer_count_mode.GetEntryByName('Manual'))
		if not PySpin.IsAvailable(stream_buffer_count_mode_manual) or not PySpin.IsReadable(stream_buffer_count_mode_manual):
		    print('Unable to set Buffer Count Mode entry (Entry retrieval). Aborting...\n')
		    return 1

		stream_buffer_count_mode.SetIntValue(stream_buffer_count_mode_manual.GetValue())


		# Retrieve and modify Stream Buffer Count
		buffer_count = PySpin.CIntegerPtr(streaming_node.GetNode('StreamBufferCountManual'))
		if not PySpin.IsAvailable(buffer_count) or not PySpin.IsWritable(buffer_count):
		    print('Unable to set Buffer Count (Integer node retrieval). Aborting...\n')
		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1

		# No exceder el maximo de buffer
		numbufer = min(buffer_count.GetMax(),numbuffer)

		buffer_count.SetValue(numbuffer)

		self.__buffer_count = numbuffer

		return 0

    
	def Set_Buffer_Handling_Mode(self,mode):

		streaming_node = self.__cam.GetTLStreamNodeMap()

		handling_mode = PySpin.CEnumerationPtr(streaming_node.GetNode('StreamBufferHandlingMode'))
		if not PySpin.IsAvailable(handling_mode) or not PySpin.IsWritable(handling_mode):
		    print('Unable to set Buffer Handling mode (node retrieval). Aborting...\n')
		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1

		handling_mode_entry = PySpin.CEnumEntryPtr(handling_mode.GetCurrentEntry())
		if not PySpin.IsAvailable(handling_mode_entry) or not PySpin.IsReadable(handling_mode_entry):
		    print('Unable to set Buffer Handling mode (Entry retrieval). Aborting...\n')
		    if self.__init_complete is None:
		        self.__init_complete = False

		    else:
		        self.__error_config= True

		    return 1

		if mode=='NewestFirst' or mode=='NewestOnly' or mode=='OldestFirst' or mode=='OldestFirstOverwrite':
		        handling_mode_entry = handling_mode.GetEntryByName(mode)
		        handling_mode.SetIntValue(handling_mode_entry.GetValue())

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


	def Acquire_Image(self,nombre):

		image_result = self.__cam.GetNextImage(500)

		if image_result.IsIncomplete():
		    print('Image incomplete with image status %d ...' % image_result.GetImageStatus())

		else:

		    image_converted = image_result.Convert(PySpin.PixelFormat_Mono8, PySpin.HQ_LINEAR)

		    filename = 'temp/'+nombre+'.bmp'

		    image_converted.Save(filename)
		    
		    image_result.Release()

	def Init_Acquisition(self):

		self.__cam.BeginAcquisition()

	def End_Acquisition(self):

		self.__cam.EndAcquisition()

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
		####presenta error en spinnakker#####
		return self.__cam.DeviceReset.Execute()

	def __del__(self):

		self.Mode_Acquisition_Video()

		self.__cam.DeInit()


		############ prueba


class Color_Reprocution:
	"""docstring for ColorReprocution"""
	def __init__(self):
		
		self.__Init_Variables()
		

	def __Init_Variables(self):

		self.__images=None
		self.__Mask=None
		self.__wavelength=None
		self.__cie_1931=None
		self.__illuminant_d65=None
		self.__select_wavelength=None
		self.__size_image=None

	def Load_Capture(self,file, Num_Wave, start=0):

		listing = os.listdir(file)

		listing=listing[start:start+Num_Wave]

		self.__images, self.__size_image = fcr.Read_Capture(file,listing)

		self.__wavelength = fcr.Read_Wavelength_Capture(listing)


		#self.__cie_1931 = fcr.Read_CIE1931_XYZ(self.__wavelength)

		self.__cie_1931 =  np.array([
         
         [410,	0.043510,	0.001210,	0.207400],
         [450,	0.336200,	0.038000,	1.772110],
         [470,	0.195360,	0.090980,	1.287640],
         [490,	0.032010,	0.208020,	0.465180],
         [505,	0.002400,	0.407300,	0.212300],
         [530,	0.165500,	0.862000,	0.042160],
         [560,	0.594500,	0.995000,	0.003900],
         [590,	1.026300,	0.757000,	0.001100],
         [600,	1.062200,	0.631000,	0.000800],
         [620,	0.854450,	0.381000,	0.000190],
         [630,	0.642400,	0.265000,	0.000050],
         [650,	0.283500,	0.107000,	0.000000],
         [720,	0.002899,	0.001047,	0.000000],
         ])

		self.__illuminant_d65 = np.array([
          [410,	91.486000],
          [450,	117.008000],
          [470,	114.861000],
          [490,	108.811000],
          [505,	108.578000],
          [530,	107.689000],
          [560,	100.000000],
          [590,	88.685600],
          [600,	90.006200],
          [620,	87.698700],
          [630, 83.288600],
          [650,	80.026800],
          [720,	61.604000],
      
          ])





















