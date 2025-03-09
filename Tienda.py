class Cajero:
    def __init__(self, nombre: str, sueldo: float):
        self.nombre = nombre
        self.sueldo = sueldo
        self.ventas = 0

    def vender(self, monto: float):
        self.ventas += 1
        self.sueldo += monto * 0.6

    def get_ventas(self) -> int:
        return self.ventas

class Tienda:
    def __init__(self, nombre: str, id: int, ingresos: float, cajero: Cajero):
        self.nombre = nombre
        self.id = id
        self.ingresos = ingresos
        self.cajero = cajero

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self) -> str:
        return self.nombre

    def calcular_ventas(self) -> int:
        return self.cajero.get_ventas()

if __name__ == "__main__":
    cajero = Cajero("Juan", 500)
    tienda = Tienda("Tienda1", 1, 1000, cajero)
    cajero.vender(100)
    cajero.vender(200)
    cajero.vender(300)
    print("*** Bienvenido a la tienda,", tienda.get_nombre(), " ***")
    print("Calcular ventas:", tienda.calcular_ventas())
    print("Sueldo del cajero Juan:",cajero.sueldo)
    cajero.vender(400)
    print("Juan realizo una venta de 400:",tienda.calcular_ventas())
    print("El nuevo sueldo de Juan",cajero.sueldo)