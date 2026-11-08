
# TEMA: CLASE SOCIOS

class Socios:
    def __init__(self, carnet, nombre, apellido):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_inicia_prestamo = ""

    def mostrar(self):
        print(f"Carnet: {self.carnet}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Inicio de prestamo: {self.fecha_inicia_prestamo or 'Sin prestamo'}")
