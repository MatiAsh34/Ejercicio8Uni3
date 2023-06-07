from Investigador import *
from Personal import *
from Docente import *

class DocenteInvestigador(Investigador,Docente):
	def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo,categoria,importe):
		super().__init__(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo)
		self.__categoria = categoria
		self.__importe = importe

	def getCategoria(self):
		return self.__categoria

	def getImporte(self):
		return self.__importe


	def __str__(self):
		return "%s %s %s %s" % (self.getCuil(),self.getApellido(),self.getNombre(),self.getSueldo_Basico())

	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__=dict(
				cuil = self.getCuil(),
				apellido = self.getApellido(),
				nombre = self.getNombre(),
				sueldo_basico = self.getSueldo_Basico(),
				antiguedad = self.getAntiguedad(),
				carrera = self.getCarrera(),
				cargo = self.getCargo(),
				catedra = self.getCatedra(),
				area = self.getArea(),
				tipo = self.getTipo(),
				categoria = self.__categoria,
				importe = self.__importe
				)
			)
		return d
		