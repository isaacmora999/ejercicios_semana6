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
        lista.agregar(Estudiante("2023001", "Ana", "Lopez", 50, 1.6, "F", 85))
        lista.agregar(Estudiante("2023002", "Luis", "Martinez", 60, 1.7, "M", 90))
        lista.agregar(Estudiante("2023003", "Sofia", "Gomez", 55, 1.5, "F", 95))
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
        lista.insertar_paciente(Paciente("Pedro Perez", 30, "Fiebre", 2))
        lista.insertar_paciente(Paciente("Maria Lopez", 25, "Dolor de cabeza", 3))
        lista.mostrar_pacientes()
        atendido = lista.atender_paciente()
        print("Paciente atendido:", atendido.nombre_completo)
        lista.mostrar_pacientes()

    elif opcion == "4":
        historial = HistorialAcciones()
        historial.agregar_accion(Accion("escribir", "Hola"))
        historial.agregar_accion(Accion("borrar", "o"))
        historial.agregar_accion(Accion("pegar", " mundo"))
        print("Deshacer accion:", historial.deshacer().tipo)
        print("Deshacer accion:", historial.deshacer().tipo)
        print("Rehacer accion:", historial.rehacer().tipo)

    else:
        print("Opcion invalida.")