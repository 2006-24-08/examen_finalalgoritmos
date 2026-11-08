
# TEMA: CLASE PRESTAMO

class Prestamo:
    def __init__(self, numero, isbn, carnet, nombre,
                 fecha_inicial, fecha_final):
        self.numero = numero
        self.isbn = isbn
        self.carnet = carnet
        self.nombre = nombre
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.devuelto = False

    def mostrar(self):
        estado = "Devuelto" if self.devuelto else "Pendiente"
        print(f"Prestamo No. {self.numero}")
        print(f"ISBN: {self.isbn}")
        print(f"Socio: {self.nombre} | Carnet: {self.carnet}")
        print(f"Inicio: {self.fecha_inicial}")
        print(f"Final: {self.fecha_final}")
        print(f"Estado: {estado}")
