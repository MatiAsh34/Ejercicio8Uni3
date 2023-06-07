import json
from pathlib import *
from Lista import *
from Apoyo import *
from Docente import *
from Investigador import *
from DocenteInvestigador import *

class ObjectEncoder(object):
	def decodificarDiccionario(self, d):
		if '__class__' not in d:
			return d
		else:
			class_name=d['__class__']
			class_=eval(class_name)
		if class_name=='Lista':
			personal=d['personal']
			dpersonal = personal[0]
			manejador=class_()
		for i in range(len(personal)):
			dpersonal=personal[i]
			class_name=dpersonal.pop('__class__')
			class_=eval(class_name)
			atributos=dpersonal['__atributos__']
			unpersonal=class_(**atributos)
			manejador.AgregarPersonal(unpersonal)
		return manejador

	def guardarJSONArchivo(self, diccionario, archivo):
		with Path(archivo).open("w", encoding="UTF-8") as destino:json.dump(diccionario, destino, indent=4)
		destino.close()
	
	def leerJSONArchivo(self,archivo):
		with Path(archivo).open(encoding="UTF-8") as fuente:diccionario=json.load(fuente)
		fuente.close()
		return diccionario
	
	def convertirTextoADiccionario(self, texto):
		return json.loads(texto)