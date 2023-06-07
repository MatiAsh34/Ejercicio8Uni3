from Lista import *
from ObjectEncoder import *
from Personal import *
from Apoyo import *
from Docente import *
from Investigador import *
from DocenteInvestigador import *
from ITesorero import ITesorero
from IDirector import IDirector

if __name__ == '__main__':
	Lista_Enlazada = Lista()
	JsonF = ObjectEncoder()
	diccionario = JsonF.leerJSONArchivo('personal.json')
	Lista_Enlazada = JsonF.decodificarDiccionario(diccionario)

	codigo = None
	while codigo != '0':
		print("\n1- Insertar a agentes a la colección.")
		print("2- Agregar agentes a la colección.")
		print("3- Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
		print("4- Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes-investigadores.")
		print("5- Dada un área de investigación, contar la cantidad de agentes que son docente-investigador, y la cantidad de investigadores que trabajen en ese área.")
		print("6- Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
		print("7- Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.")
		print("8- Almacenar los datos de todos los agentes en el archivo “personal.json”")
		print("0- Salir")

		codigo = input("\nIngrese codigo: ")

		if codigo == '1':
			print("\n1)Apoyo - 2)Docente - 3)Investigador 4)DocenteInvestigador")
			cod = input("Ingrese cod: ")

			if cod == '1' or cod == '2' or cod == '3' or cod == '4':
				cuil = input("Inserte cuil: ")
				apellido = input("Inserte apellido: ")
				nombre = input("Inserte nombre: ")
				sueldo_basico = float(input("Inserte sueldo basico: "))
				antiguedad = int(input("Inserte antiguedad: "))

				if cod == '1':
					categoria = input("Categoria: ")
					unAgente = Apoyo(cuil,apellido,nombre,sueldo_basico,antiguedad,categoria)

				elif cod == '2':
					carrera = input("Inserte carrera: ")
					cargo = input("Inserte cargo: ")
					catedra = input("Inserte catedra: ")
					unAgente = Docente(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,'','')

				elif cod == '3':
					area = input("Inserte area")
					tipo = input("Inserte tipo: ")
					unAgente = Investigador(cuil,apellido,nombre,sueldo_basico,antiguedad,'','','',area,tipo)

				elif cod == '4':
					carrera = input("Inserte carrera: ")
					cargo = input("Inserte cargo: ")
					catedra = input("Inserte catedra: ")
					area = input("Inserte area")
					tipo = input("Inserte tipo: ")
					categoria = input("Inserte categoria: ")
					importe = float(input("Inserte importe: "))
					unAgente = DocenteInvestigador(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo,categoria,importe)

				posicion = int(input("Ingrese posicion: "))
				Lista_Enlazada.InsertarPersonal(unAgente,posicion)

			else:
				print("Codigo incorrecto!")


		elif codigo == '2':
			print("\n1)Apoyo - 2)Docente - 3)Investigador 4)DocenteInvestigador")
			cod = input("Ingrese cod: ")

			if cod == '1' or cod == '2' or cod == '3' or cod == '4':
				cuil = input("Inserte cuil: ")
				apellido = input("Inserte apellido: ")
				nombre = input("Inserte nombre: ")
				sueldo_basico = float(input("Inserte sueldo basico: "))
				antiguedad = int(input("Inserte antiguedad: "))

				if cod == '1':
					categoria = input("Categoria: ")
					unAgente = Apoyo(cuil,apellido,nombre,sueldo_basico,antiguedad,categoria)

				elif cod == '2':
					carrera = input("Inserte carrera: ")
					cargo = input("Inserte cargo: ")
					catedra = input("Inserte catedra: ")
					unAgente = Docente(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra)

				elif cod == '3':
					area = input("Inserte area: ")
					tipo = input("Inserte tipo: ")
					unAgente = Investigador(cuil,apellido,nombre,sueldo_basico,antiguedad,area,tipo)

				elif cod == '4':
					carrera = input("Inserte carrera: ")
					cargo = input("Inserte cargo: ")
					catedra = input("Inserte catedra: ")
					area = input("Inserte area: ")
					tipo = input("Inserte tipo: ")
					categoria = input("Inserte categoria: ")
					importe = float(input("Inserte importe: "))
					unAgente = DocenteInvestigador(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo,categoria,importe)

				Lista_Enlazada.AgregarPersonal(unAgente)

			else:
				print("Codigo incorrecto!")

		elif codigo == '3':
			posicion = int(input("Ingrese una posicion: "))
			Lista_Enlazada.Mostrar_Posicion(posicion)

		elif codigo == '4':
			carrera = input("Ingrese carrera: ")
			Lista_Enlazada.Genera_Listado_Carrera(carrera)	

		elif codigo == '5':
			area = input("Ingrese un area: ")
			Lista_Enlazada.Cuenta_Cantidad(area)

		elif codigo == '6':
			Lista_Enlazada.Genera_Listado()

		elif codigo == '7':
			categoria = input("Ingrese categoria: ")
			Lista_Enlazada.Mostrar_Categoria(categoria)

		elif codigo == '8':
			d = Lista_Enlazada.toJSON()
			JsonF.guardarJSONArchivo(d,'nuevopersonal.json')

		elif codigo == '0':
			print("Saliendo...")

		usuario=input("Usuario (uTesorero/uDirector):\n")
            clave=input("Clave:\n")
            if usuario.upper()=='uTesorero'.upper() and clave=='ag@74ck':
                print ("Consultar gastos de sueldo para un agente")
                Tesorero(ITesorero(agentes))
            elif usuario.upper()=='uDirector'.upper() and clave=='ufC77#!1':
                Director(ITesorero(agentes))
            aux=input("\nIngrese cualquier tecla para continuar\n")