class Vehiculo:

    def vehiculo(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        print('El vehiculo es de color {}, tiene {} ruedas y {} puertas'.format(self.color, self.ruedas, self.puertas))

class Coche(Vehiculo):
    Velocidad = '100 Km/h'
    cilindrada = '0'

c = Coche()

c.vehiculo('negro','4','4')
print('Alcanza una velocidad de',c.Velocidad)
print('Posee una cilindrada de',c.cilindrada)