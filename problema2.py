from models.nodo import Nodo

class Estacion:
    def __init__(self, nombre, tiempo_a_siguiente):
        self.nombre = nombre
        self.tiempo_a_siguiente = tiempo_a_siguiente

class Ruta:
    def __init__(self):
        self.head = None

    def agregar_estacion(self, estacion):
        nuevo = Nodo(estacion)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def tiempo_estimado(self, origen, destino):
        actual = self.head
        suma = 0
        contando = False
        while actual:
            if actual.data.nombre == origen:
                contando = True
            if contando:
                suma += actual.data.tiempo_a_siguiente
            if actual.data.nombre == destino:
                break
            actual = actual.next
        return suma