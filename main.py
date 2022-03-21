

class Auto:

    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):

        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:

            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.registro or asiento.registro != self.motor.registro:
                    return "Las piezas no son originales"

        return "Auto origina"



class Asiento:

    def __init___(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    
    def cambiarColor(self, color):

        coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]

        if color in coloresPermitidos:
            self.color = color
    
class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):

        self.registro = registro
    
    def asignarTipo(self, tipo):

        tipoPermitido = ["gasolina", "electrico"]

        if tipo in tipoPermitido:

            self.tipo = tipo
    


