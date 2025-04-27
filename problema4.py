from models.nodo import Nodo

class Accion:
    def __init__(self, tipo, contenido):
        self.tipo = tipo
        self.contenido = contenido

class HistorialAcciones:
    def __init__(self):
        self.head = None
        self.tail = None
        self.actual = None

    def agregar_accion(self, accion):
        nuevo = Nodo(accion)
        if not self.head:
            self.head = self.tail = nuevo
        else:
            self.tail.next = nuevo
            nuevo.prev = self.tail
            self.tail = nuevo
        self.actual = self.tail

    def deshacer(self):
        if self.actual and self.actual.prev:
            self.actual = self.actual.prev
            return self.actual.data
        return None

    def rehacer(self):
        if self.actual and self.actual.next:
            self.actual = self.actual.next
            return self.actual.data
        return None
    