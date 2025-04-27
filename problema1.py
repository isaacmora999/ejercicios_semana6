from models.nodo import Nodo

class Estudiante:
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

class ListaEstudiantes:
    def __init__(self):
        self.head = None

    def agregar(self, estudiante):
        nuevo = Nodo(estudiante)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def ordenar_por(self, atributo):
        if not self.head or not self.head.next:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.head
            while actual.next:
                if getattr(actual.data, atributo) > getattr(actual.next.data, atributo):
                    actual.data, actual.next.data = actual.next.data, actual.data
                    cambiado = True
                actual = actual.next

    def mostrar(self):
        actual = self.head
        while actual:
            e = actual.data
            print(e.carnet, e.nombres, e.apellidos, e.peso, e.estatura, e.sexo, e.promedio)
            actual = actual.next