from Personal import *

class Apoyo(Personal):
	def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,categoria):
		super().__init__(cuil,apellido,nombre,sueldo_basico,antiguedad)
		self.__categoria = categoria

	def getCategoria(self):
		return self.__categoria

	

	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__=dict(
				cuil = self.getCuil(),
				apellido = self.getApellido(),
				nombre = self.getNombre(),
				sueldo_basico = self.getSueldo_Basico(),
				antiguedad = self.getAntiguedad(),
				categoria = self.__categoria
				)
			)
		return d
		