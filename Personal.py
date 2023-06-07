from abc import *

class Personal(ABC):
	def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,carrera='',cargo='',catedra='',area='',tipo=''):
		self.__cuil = cuil
		self.__apellido = apellido
		self.__nombre = nombre
		self.__sueldo_basico = sueldo_basico
		self.__antiguedad = antiguedad
	
	def getCuil(self):
		return self.__cuil

	def getApellido(self):
		return self.__apellido

	def getNombre(self):
		return self.__nombre

	def getSueldo_Basico(self):
		return self.__sueldo_basico

	def getAntiguedad(self):
		return self.__antiguedad

	def __str__(self):
		pass

	def __lt__(self,otro):
		return self.__apellido < otro.__apellido

	@abstractmethod
	def toJSON(self):
		pass