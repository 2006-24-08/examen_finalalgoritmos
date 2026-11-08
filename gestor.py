
# TEMA: CLASE GESTOR LIBROS
# TEMA: ARCHIVOS, DICCIONARIOS Y LISTAS

import json
from pathlib import Path
from datetime import date

from libro import ISBN
from socios import Socios
from stock import Stock
from prestamo import Prestamo


class GestorLibros:
    def __init__(self):
        self.libros = {}
        self.socios = {}
        self.prestamos = []
        self.stock = Stock()
        self.archivo = Path(__file__).with_name("datos.json")
        self.cargar()

    # TEMA: GUARDAR DATOS
    def guardar(self):
        datos = {
            "libros": [vars(x) for x in self.libros.values()],
            "socios": [vars(x) for x in self.socios.values()],
            "prestamos": [vars(x) for x in self.prestamos]
        }

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    # TEMA: CARGAR DATOS
    def cargar(self):
        if not self.archivo.exists():
            return

        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        for x in datos.get("libros", []):
            libro = ISBN(x["isbn"], x["titulo_libro"],
                         x["autor"], x["cantidad"])
            self.libros[libro.isbn] = libro

        for x in datos.get("socios", []):
            socio = Socios(x["carnet"], x["nombre"], x["apellido"])
            socio.fecha_inicia_prestamo = x.get(
                "fecha_inicia_prestamo", "")
            self.socios[socio.carnet] = socio

        for x in datos.get("prestamos", []):
            p = Prestamo(x["numero"], x["isbn"], x["carnet"],
                         x["nombre"], x["fecha_inicial"],
                         x["fecha_final"])
            p.devuelto = x.get("devuelto", False)
            self.prestamos.append(p)

    # TEMA: REGISTRAR LIBROS
    def registrar_libro(self):
        isbn = input("ISBN: ").strip()

        if not isbn:
            print("El ISBN es obligatorio.")
            return

        if isbn in self.libros:
            print("Este ISBN ya esta registrado.")
            return

        titulo = input("Titulo del libro: ").strip()
        autor = input("Autor: ").strip()

        if not titulo or not autor:
            print("El titulo y autor son obligatorios.")
            return

        try:
            cantidad = int(input("Cantidad de libros: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
        except ValueError:
            print("Debe ingresar un numero entero.")
            return

        libro = ISBN(isbn, titulo, autor, cantidad)
        self.libros[isbn] = libro
        self.guardar()

        print("Libro registrado correctamente.")
        print(self.stock.revisar(libro))

    # TEMA: REGISTRAR SOCIOS
    def registrar_socio(self):
        carnet = input("Carnet: ").strip()

        if not carnet:
            print("El carnet es obligatorio.")
            return

        if carnet in self.socios:
            print("El socio ya esta registrado.")
            return

        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()

        if not nombre or not apellido:
            print("Nombre y apellido son obligatorios.")
            return

        self.socios[carnet] = Socios(carnet, nombre, apellido)
        self.guardar()
        print("Socio registrado correctamente.")

    # TEMA: VER LIBROS
    def ver_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
            return

        for libro in self.libros.values():
            print("-------------------------")
            libro.mostrar()
            print(self.stock.revisar(libro))

    # TEMA: VER SOCIOS
    def ver_socios(self):
        if not self.socios:
            print("No hay socios registrados.")
            return

        for socio in self.socios.values():
            print("-------------------------")
            socio.mostrar()

    # TEMA: REGISTRAR PRESTAMO
    def registrar_prestamo(self):
        isbn = input("ISBN del libro: ").strip()
        carnet = input("Carnet del socio: ").strip()

        if isbn not in self.libros:
            print("Libro no encontrado.")
            return

        if carnet not in self.socios:
            print("Socio no encontrado.")
            return

        libro = self.libros[isbn]
        socio = self.socios[carnet]

        if libro.no_disponible():
            print("ALERTA: Libro no disponible.")
            return

        try:
            inicio = date.fromisoformat(
                input("Fecha inicial (AAAA-MM-DD): ").strip())
            final = date.fromisoformat(
                input("Fecha final (AAAA-MM-DD): ").strip())
        except ValueError:
            print("Fecha incorrecta. Ejemplo: 2026-11-08")
            return

        if final < inicio:
            print("La fecha final no puede ser anterior.")
            return

        numero = max(
            (p.numero for p in self.prestamos), default=0
        ) + 1

        nombre = socio.nombre + " " + socio.apellido

        prestamo = Prestamo(numero, isbn, carnet, nombre,
                           inicio.isoformat(), final.isoformat())

        self.prestamos.append(prestamo)
        libro.cantidad -= 1
        socio.fecha_inicia_prestamo = inicio.isoformat()

        self.guardar()

        print(f"Prestamo No. {numero} registrado.")
        print(self.stock.revisar(libro))

    # TEMA: DEVOLVER LIBRO
    def devolver_libro(self):
        try:
            numero = int(input("Numero de prestamo: "))
        except ValueError:
            print("Numero incorrecto.")
            return

        for p in self.prestamos:
            if p.numero == numero:
                if p.devuelto:
                    print("Este libro ya fue devuelto.")
                    return

                p.devuelto = True
                self.libros[p.isbn].cantidad += 1
                self.guardar()

                print("Libro devuelto correctamente.")
                print(self.stock.revisar(self.libros[p.isbn]))
                return

        print("Prestamo no encontrado.")

    # TEMA: VER PRESTAMOS
    def ver_prestamos(self):
        if not self.prestamos:
            print("No hay prestamos registrados.")
            return

        for p in self.prestamos:
            print("-------------------------")
            p.mostrar()

    # TEMA: ALERTAS DE STOCK
    def ver_alertas(self):
        if not self.libros:
            print("No hay libros registrados.")
            return

        for libro in self.libros.values():
            print(f"{libro.titulo_libro}: {self.stock.revisar(libro)}")
