from problema1 import ListaEstudiantes, Estudiante
from problema2 import Ruta, Estacion
from problema3 import ListaPacientes, Paciente
from problema4 import HistorialAcciones, Accion

if __name__ == "__main__":
    print("Seleccione el problema a ejecutar:")
    print("1. Ordenar estudiantes")
    print("2. Ruta de estaciones")
    print("3. Gestion de pacientes")
    print("4. Historial de acciones")
    opcion = input("Opcion: ")

    if opcion == "1":
        lista = ListaEstudiantes()
        while True:
            carnet = input("Carnet: ")
            nombres = input("Nombres: ")
            apellidos = input("Apellidos: ")
            peso = float(input("Peso: "))
            estatura = float(input("Estatura: "))
            sexo = input("Sexo: ")
            promedio = float(input("Promedio: "))
            lista.agregar(Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio))
            if input("¿Agregar otro estudiante? (s/n): ").lower() != "s":
                break
        atributo = input("Ordenar por (carnet, nombres, apellidos, peso, estatura, sexo, promedio): ")
        lista.ordenar_por(atributo)
        lista.mostrar()

    elif opcion == "2":
        ruta = Ruta()
        ruta.agregar_estacion(Estacion("A", 5))
        ruta.agregar_estacion(Estacion("B", 7))
        ruta.agregar_estacion(Estacion("C", 4))
        origen = input("Estacion origen: ")
        destino = input("Estacion destino: ")
        print("Tiempo estimado:", ruta.tiempo_estimado(origen, destino), "minutos")

    elif opcion == "3":
        lista = ListaPacientes()
        while True:
            print("\n1. Agregar paciente")
            print("2. Mostrar pacientes")
            print("3. Atender (eliminar) paciente")
            print("4. Salir")
            subopcion = input("Opcion: ")
            if subopcion == "1":
                nombre = input("Nombre completo: ")
                edad = int(input("Edad: "))
                sintoma = input("Sintoma principal: ")
                prioridad = int(input("Prioridad (1-5): "))
                lista.insertar_paciente(Paciente(nombre, edad, sintoma, prioridad))
            elif subopcion == "2":
                lista.mostrar_pacientes()
            elif subopcion == "3":
                paciente = lista.atender_paciente()
                if paciente:
                    print("Paciente atendido:", paciente.nombre_completo)
                else:
                    print("No hay pacientes para atender.")
            elif subopcion == "4":
                break

    elif opcion == "4":
        historial = HistorialAcciones()
        while True:
            print("\n1. Agregar accion")
            print("2. Deshacer")
            print("3. Rehacer")
            print("4. Salir")
            subopcion = input("Opcion: ")
            if subopcion == "1":
                tipo = input("Tipo de accion (escribir, borrar, pegar, copiar): ")
                contenido = input("Contenido: ")
                historial.agregar_accion(Accion(tipo, contenido))
            elif subopcion == "2":
                accion = historial.deshacer()
                if accion:
                    print("Accion deshecha:", accion.tipo)
                else:
                    print("No hay accion para deshacer.")
            elif subopcion == "3":
                accion = historial.rehacer()
                if accion:
                    print("Accion rehecha:", accion.tipo)
                else:
                    print("No hay accion para rehacer.")
            elif subopcion == "4":
                break

    else:
        print("Opcion invalida.")
