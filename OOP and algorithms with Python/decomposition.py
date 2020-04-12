class Automovil(object):

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
    def acelerar(self, tipo="despacio"):
        if tipo == 'rapido':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3)
        self._estado = 'en_movimiento'
    
class Motor(object):
    def __init__(self, cilindros, tipo="Gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura
    
    def inyectar_gasolina(self, cantidad):
        pass
        
        