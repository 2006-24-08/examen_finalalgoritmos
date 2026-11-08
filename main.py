
# TEMA: MENU PRINCIPAL
# PROYECTO: GESTOR DE LIBROS

from gestor import GestorLibros


def main():
    gestor = GestorLibros()

    while True:
        print("\n========== GESTOR DE LIBROS ==========")
        print("1. Registrar libro")
        print("2. Registrar socio")
        print("3. Ver libros")
        print("4. Ver socios")
        print("5. Registrar prestamo")
        print("6. Devolver libro")
        print("7. Ver prestamos")
        print("8. Alertas de stock")
        print("9. Salir")
        print("======================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            gestor.registrar_libro()
        elif opcion == "2":
            gestor.registrar_socio()
        elif opcion == "3":
            gestor.ver_libros()
        elif opcion == "4":
            gestor.ver_socios()
        elif opcion == "5":
            gestor.registrar_prestamo()
        elif opcion == "6":
            gestor.devolver_libro()
        elif opcion == "7":
            gestor.ver_prestamos()
        elif opcion == "8":
            gestor.ver_alertas()
        elif opcion == "9":
            gestor.guardar()
            print("Datos guardados. Hasta pronto.")
            break
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    main()
