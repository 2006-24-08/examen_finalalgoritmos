
# TEMA: CLASE ISBN

class ISBN:
    def __init__(self, isbn, titulo_libro, autor, cantidad):
        self.isbn = isbn
        self.titulo_libro = titulo_libro
        self.autor = autor
        self.cantidad = cantidad

    def disponible(self):
        return self.cantidad > 0

    def no_disponible(self):
        return self.cantidad == 0

    def mostrar(self):
        estado = "Disponible" if self.disponible() else "No disponible"
        print(f"{self.isbn} | {self.titulo_libro} | {self.autor}")
        print(f"Stock: {self.cantidad} | {estado}")
