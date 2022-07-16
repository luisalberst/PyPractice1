from math import pi

# Area de un triangulo
def areat(base,altura):
    areat = base * altura // 2
    return areat
# Area de un circulo
def areac(radio):
    areac = pi * radio ** 2
    return round(areac,2)

print('Área de un triangulo:',areat(7,9))
print('Área de un círculo:',areac(6),'cm2')