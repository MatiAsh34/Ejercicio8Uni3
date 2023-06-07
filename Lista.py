from Nodo import *
from Apoyo import *
from Docente import *
from Investigador import *
from DocenteInvestigador import *

class Lista(object):
	def __init__(self):
		self.__comienzo = None

	def AgregarPersonal(self,personal):
		nodo = Nodo(personal)
		nodo.setSiguiente(self.__comienzo)
		self.__comienzo = nodo

	def InsertarPersonal(self,personal,posicion):
		aux = self.__comienzo
		try:
			for i in range(posicion-1):
				anterior = aux
				aux = aux.getSiguiente()

			nodo = Nodo(personal)
			anterior.setSiguiente(nodo)	
			nodo.setSiguiente(aux)
		except AttributeError:
			print("Fuera de rango!")
			print("Posicion disponible ", i+1)

	def Mostrar_Posicion(self,posicion):
		aux = self.__comienzo
		i = 1

		while i < posicion and aux != None:
			aux = aux.getSiguiente()
			i += 1

		if i == posicion:
			if isinstance(aux.getDato(),Apoyo):
				print("Es un agente de apoyo!")
			elif isinstance(aux.getDato(),Docente):
				if isinstance(aux.getDato(),DocenteInvestigador):
					print("Es un docente investigador!")
				else:
					print("Es un docente!")
			elif isinstance(aux.getDato(),Investigador):
				print("Es un investigador!")
		else:
			print("Posicion no encontrada!")

	def Genera_Listado_Carrera(self,carrera):
		aux = self.__comienzo
		lista_ordenada = []
		while aux != None:
			if isinstance(aux.getDato(),Docente):
				if isinstance(aux.getDato(),DocenteInvestigador):
					agente = aux.getDato()
					if agente.getCarrera() == carrera:
						lista_ordenada.append(agente)
			aux = aux.getSiguiente()

		lista_ordenada.sort(key=lambda agente: agente.getNombre())
		for i in range(len(lista_ordenada)):
			print(lista_ordenada[i])
			
	def Cuenta_Cantidad(self,area):
		aux = self.__comienzo
		contDI = 0
		contI = 0
		while aux != None:
			if isinstance(aux.getDato(),Investigador):
				if isinstance(aux.getDato(),DocenteInvestigador):
					agente = aux.getDato()
					if agente.getArea() == area:
						contDI += 1
				else:
					agente = aux.getDato()
					if agente.getArea() == area:
						contI += 1
			aux = aux.getSiguiente()
		print("Cantidad de investigadores de ese area: {}, Cantidad de docente-investigadores de ese area: {}".format(contI,contDI))
				
	def Genera_Listado(self):
		aux = self.__comienzo
		lista_ordenada = []
		while aux != None:
			agente = aux.getDato()
			lista_ordenada.append(agente)
			aux = aux.getSiguiente()

		lista_ordenada.sort()

		for i in range(len(lista_ordenada)):
			print("\nNombre: {}, Apellido: {}, Sueldo: {}".format(lista_ordenada[i].getNombre(),lista_ordenada[i].getApellido(),lista_ordenada[i].getSueldo_Basico()))
			if isinstance(lista_ordenada[i],Apoyo):
				print("Es un agente de apoyo")

			elif isinstance(lista_ordenada[i],Docente):
				if isinstance(lista_ordenada[i],DocenteInvestigador):
					print("Es un docente investigador")

				else:
					print("Es un docente")

			elif isinstance(lista_ordenada[i],Investigador):
				print("Es un investigador")

	def Mostrar_Categoria(self,categoria):
		aux = self.__comienzo
		importe_total = 0
		while aux != None:
			if isinstance(aux.getDato(),Docente):
				if isinstance(aux.getDato(),DocenteInvestigador):
					agente = aux.getDato()
					if agente.getCategoria() == categoria:
						print("Apellido: {}, Nombre: {}, Importe extra: {}".format(agente.getApellido(),agente.getNombre(),agente.getImporte()))
						importe_total += agente.getImporte()
			aux = aux.getSiguiente()

		print("Total de dinero que la Secretaría de Investigación debe solicitar al Ministerio: {}".format(importe_total))

	def toJSON(self):
		aux=self.__comienzo
		listanormal=[]
		while aux!=None:
			listanormal.append(aux.getDato())
			aux=aux.getSiguiente()
		d=dict(
			__class__="Lista",
			personal=[personal.toJSON() for personal in listanormal]
		)
		return d