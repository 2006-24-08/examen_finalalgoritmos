
# TEMA: CLASE STOCK

class Stock:
    STOCK_MINIMO = 3

    def alertar_stock_minimo(self, cantidad):
        return 0 < cantidad <= self.STOCK_MINIMO

    def sin_alerta_stock(self, cantidad):
        return cantidad > self.STOCK_MINIMO

    def alertar_no_disponible(self, cantidad):
        return cantidad == 0

    def revisar(self, libro):
        if self.alertar_no_disponible(libro.cantidad):
            return "ALERTA: Libro no disponible"
        elif self.alertar_stock_minimo(libro.cantidad):
            return "ALERTA: Stock minimo (3 o menos)"
        else:
            return "Sin alerta de stock"
