from Personal import *

class Docente(Personal):
	def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo):
		super().__init__(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo)
		self.__carrera = carrera
		self.__cargo = cargo
		self.__catedra = catedra
		
	def getCarrera(self):
		return self.__carrera

	def getCargo(self):
		return self.__cargo

	def getCatedra(self):
		return self.__catedra

	

	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__=dict(
				cuil = self.getCuil(),
				apellido = self.getApellido(),
				nombre = self.getNombre(),
				sueldo_basico = self.getSueldo_Basico(),
				antiguedad = self.getAntiguedad(),
				carrera = self.__carrera,
				cargo = self.__cargo,
				catedra = self.__catedra
				)
			)
		return d
		