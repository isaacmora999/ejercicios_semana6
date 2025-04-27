from models.nodo import Nodo

class Paciente:
    def __init__(self, nombre_completo, edad, sintoma_principal, prioridad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.sintoma_principal = sintoma_principal
        self.prioridad = prioridad

class ListaPacientes:
    def __init__(self):
        self.head = None

    def insertar_paciente(self, paciente):
        nuevo = Nodo(paciente)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def atender_paciente(self):
        if self.head:
            atendido = self.head.data
            self.head = self.head.next
            return atendido
        return None

    def mostrar_pacientes(self):
        actual = self.head
        while actual:
            p = actual.data
            print(p.nombre_completo, p.edad, p.sintoma_principal, p.prioridad)
            actual = actual.next