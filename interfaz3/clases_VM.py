import serial
import time


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



		

