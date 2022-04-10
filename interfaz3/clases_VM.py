import serial
import time
import PySpin

class Corona_Multiespectral:

	"""docstring for Corona_Multiespectral"""
	def __init__(self, puerto,bps=57600,time_sleep_c=1e-2):
		print("Iniciando Corona_Multiespectral")
		self.__timesleepc = time_sleep_c
		self.__shot_mesage = 'W'
		self.__leds = ['M01N','M02N','M03N','M04N','M05N','M06N','M07N','M08N','M09N','M0AN','M0BN','M0CN','M0DN','M0EN','M0FN']
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
		if self.__comunication_state:
			bandera=0
			iteraciones=0
			while bandera==0 and iteraciones<5:
				try:
					self.__comunication.write(message.encode('utf-8'))
					time.sleep(self.__timesleepc)

					Check=''
					if self.__comunication.inWaiting()==1:
					    
					    Check = self.__comunication.read()
					    
					if Check == b'O':
					    bandera=1

					iteraciones+=1

				except:
					print("error en la comunicacion no se configuro los tiempos de trigger")
					self.__comunication_state=False
					break


			if bandera==0:

				print("No se recibio una respuesta correcta de la corona.")
				return 1

			else:
				self.__shot_mode = message[1]
				self.__shot_time_trigger= message[2:4]
				self.__shot_time_flash = message[4:7]
				self.__shot_time_timeout =message[7:10]

				return 0

		else:
			print("Error Comunicación no iniciada No es posible configurar los tiempos de trigger")
			self.__comunication_state=False
			return 1

	def set_shot_mode(self,value):
		try:
			val=int(value)

			if val!=0 and val!=1:
				print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
				return 1

		except:
			print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
			return 1

		if len(value)==1:

			message =  'T'+ value + self.__shot_time_trigger + self.__shot_time_flash + self.__shot_time_timeout + 'U'

			res = self.set_shot_time_trigger_flash_timeout(message)

			if res!=0:
				print('Error en la configuración del tiempo del modo de disparo')
				return 1

			else:

				return 0 

		else:
			print("Valor incorrecto el mensaje solo debe contener un 0 o un 1")
			return 1

	def set_shot_time_trigger(self,value):
		try:
			int(value)
		except:
			print("Valor incorrecto el mensaje solo debe contener 2 digitos")
			return 1

		if len(value)==2:

			message =  'T'+ self.__shot_mode + value + self.__shot_time_flash + self.__shot_time_timeout + 'U'

			res = self.set_shot_time_trigger_flash_timeout(message)

			if res!=0:
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

			res = self.set_shot_time_trigger_flash_timeout(message)

			if res!=0:
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

			res = self.set_shot_time_trigger_flash_timeout(message)

			if res!=0:
				print('Error en la configuración del tiempo muerto')
				return 1

			else:

				return 0 

		else:
			print("Valor incorrecto se debe ingresar 3 digitos para un valor correcto de tiempo")
			return 1

	def set_shot_leds(self,pos_leds):

		if self.__comunication_state:
			bandera=0
			iteraciones=0
			while bandera==0 and iteraciones<5:
					try:
						self.__comunication.write(self.__leds[pos_leds].encode('utf-8'))
						time.sleep(self.__timesleepc)

						Check=''
						if self.__comunication.inWaiting()==1:
						    
						    Check = self.__comunication.read()
						    
						if Check == b'O':
						    bandera=1

						iteraciones+=1

					except:
						print("error en la comunicacion no se configuro el led para el disparo")
						self.__comunication_state=False
						break

			if bandera==0:
				print("No se recibio una respuesta correcta de la corona.")
				return 1

			else:
				return 0 
		else:
			print("Error Comunicación no iniciada No es posible configurar los leds para el disparo")
			return 1

	def set_PWM_Leds(self,pwm_leds): #medio garantiza que la corona este configurada si despues de configurar la corona esta se desconecta pierde la configuracion

		if self.__comunication_state:
			result=True
			for pwm_led in pwm_leds:

				bandera=0
				iteraciones=0
				while bandera==0 and iteraciones<5:
						try:
							self.__comunication.write(pwm_led.encode('utf-8'))
							time.sleep(self.__timesleepc)

							Check=''
							if self.__comunication.inWaiting()==1:
							    
							    Check = self.__comunication.read()
							    
							if Check == b'O':
							    bandera=1

							iteraciones+=1

						except:
							print("error en la comunicacion")
							self.__comunication_state=False
							break

		    
				if bandera==0:
					print("Error al configurar el PWM de la corona")
					result= False
					break


			if result:
				self.__PWM_leds=pwm_leds


		else:
			print("Error Comunicación no iniciada No es posible configurar el PWM")

	def set_shot_mesage(self,mensaje):

		self.__shot_mesage = mensaje

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

		return self.__shot_mesage

	def get_shot_mode(self):

		return self.__shot_mode

	def get_shot_time_trigger(self):

		return self.__shot_time_trigger

	def get_shot_time_flash(self):

		return self.__shot_time_flash

	def get_shot_time_out(self):

		return self.__shot_time_timeout

	##############################

	#Methods

	##############################


	def shot(self):

		if self.__comunication_state:
			self.__comunication.write(self.__shot_mesage.encode('utf-8'))
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



	##############################

	# Especial Functions

	##############################

	def __del__(self):

		if self.__comunication_state:

			self.__comunication.close()


class Camera_PySpin():
	"""docstring for Camera_PySpin"""
	def __init__(self,pyspin_camlis,Gamma=1.25,ExposureTime=8000,Gain=0,Sharpness=1800,BlackLevel=0.7,BufferMode='Continuous',BufferHandlingMode = 'NewestOnly',TriggerSource= 'Line2'):
		try:

			self.__init_states()

			self.__cam = pyspin_camlis

			nodemap_tldevice = self.__cam.GetTLDeviceNodeMap()

			self.Device_Info(nodemap_tldevice)

			self.__cam.Init()

			self.__nodemap = self.__cam.GetNodeMap()

		except:

			self.__init_complete = False


		self.Set_Trigger_Mode(False)
		self.Set_Trigger_Source(TriggerSource)
		self.Set_Trigger_Mode(True)



		self.Set_Gamma(Gamma)

		self.Set_BlackLevel(BlackLevel)

		
		self.Set_Exposure_Auto(False)
		self.Set_Exposure(ExposureTime)

		
		self.Set_Gain_Auto(False)
		self.Set_Gain(Gain)

		
		self.Set_Sharpness_Auto(False)
		self.Set_Sharpness(Sharpness)

		
	
		self.Set_Buffer_Mode(BufferMode)
		self.Set_Buffer_Count(1)
		self.Set_Buffer_Handling_Mode(BufferHandlingMode)
		
	def __init_states(self):
		self.__error_config = False
		self.__init_complete = None
		self.__trigger_mode = None
		self.__exposure_auto = None
		self.__gain_auto = None
		self.__sharpness_auto = None
		self.__trigger_mode=None
		self.__buffer_mode = None
		self.__buffer_count= None
		self.__buffer_handling_mode = None
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

	def Set_Exposure(self,exposure):

		if self.__cam.ExposureTime.GetAccessMode() != PySpin.RW:
		    print('Unable to set exposure time. Aborting...')
		    return False

		# Ensure desired exposure time does not exceed the maximum

		exposure_time_to_set = min(self.__cam.ExposureTime.GetMax(), exposure)

		self.__cam.ExposureTime.SetValue(exposure_time_to_set)

		self.__exposure = exposure


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
			return 1

		self.__trigger_source = line

		if trigger_mode:

			self.Set_Trigger_Mode(True)


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

			return 1


		self.__buffer_mode = mode

	def Set_Buffer_Count(self,numbuffer):

		streaming_node = self.__cam.GetTLStreamNodeMap()
		stream_buffer_count_mode = PySpin.CEnumerationPtr(streaming_node.GetNode('StreamBufferCountMode'))
		if not PySpin.IsAvailable(stream_buffer_count_mode) or not PySpin.IsWritable(stream_buffer_count_mode):
		    print('Unable to set Buffer Count Mode (node retrieval). Aborting...\n')
		    return False

		stream_buffer_count_mode_manual = PySpin.CEnumEntryPtr(stream_buffer_count_mode.GetEntryByName('Manual'))
		if not PySpin.IsAvailable(stream_buffer_count_mode_manual) or not PySpin.IsReadable(stream_buffer_count_mode_manual):
		    print('Unable to set Buffer Count Mode entry (Entry retrieval). Aborting...\n')
		    return False

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
			return 1

		self.__buffer_handling_mode = mode

	#############################################
	# Mode Functions 
	############################################
	def Mode_Acquisition_Multispectral(self):

		self.Set_Gain_Auto(False)
		self.Set_Gain(self.__gain)
		self.Set_Sharpness_Auto(False)
		self.Set_Sharpness(self.__sharpness)
		self.Set_Exposure_Auto(False)
		self.Set_Exposure(self.exposure)

		self.Set_Trigger_Mode(True)


	def Mode_Acquisition_Video(self):

		self.Set_Gain_Auto(True)
		self.Set_Sharpness_Auto(True)
		self.Set_Exposure_Auto(True)
		self.Set_Trigger_Mode(False)



	###################################
	# Get Funcitons
	###################################

	def Get_Device_Info(self):

		return self.__device_info


	def Reset(self):
		####presenta error en spinnakker#####
		return self.__cam.DeviceReset.Execute()



	##################################
	# Special Functions
	################################

	def __del__(self):
		self.Mode_Video()
		self.__cam.DeInit()