class Vehiculo:
    Color = 'Negro'
    Ruedas = '4'
    Puertas = '4'

class Coche(Vehiculo):
    Velocidad = '100 Km/h'
    cilindrada = '0'

c = Coche()

print('El color es',c.Color)
print('Tiene',c.Ruedas,'ruedas')
print('Tiene',c.Puertas,'puertas')
print('Alcanza una velocidad de',c.Velocidad)
print('Posee una cilindrada de',c.cilindrada)