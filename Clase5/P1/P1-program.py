from math import pi

## Menu ##

menu = '''
*** Seleccione el Area a Calcular ***
******                         ******
****** 1. Area de un triangulo ******
****** 2. Area de un circulo   ******
****** 3. Salir                ******
******                         ******
*** Seleccione el Area a Calcular ***
'''

# Area de un triangulo
def areat(base,altura):
    areat = base * altura // 2
    return areat
# Area de un circulo
def areac(radio):
    areac = pi * radio ** 2
    return round(areac,2)
## Menú y Operaciones
def main():
    option=0
    while option != 3:
        print(menu)
        print('Introduce la opción que desea seleccionar')
        option = int(input())
        if option == 1:
            print('Usted selecciono la opción para calcular el Area de un Triangulo')
            print('Introduzca los datos requeridos para calcular')
            print('-- Introduce la base del triangulo --')
            base = int(input())
            print('-- Introduce la altura del triangulo --')
            altura = int(input())
            print()
            print('El area del triangulo es:',areat(base,altura))
            print()
            input('Presione la Tecla Entrar para continuar')
        elif option == 2:
            print('Usted selecciono la opción para calcular el Area de un Circulo')
            print('Introduzca los datos requeridos para calcular')
            print('-- Introduce el radio del circulo en cm --')
            radio = int(input())
            print()
            print('El área de un circulo de radio,',radio,'cm es de',areac(radio),'cm2')
            print()
            input('Presione la Tecla Entrar para continuar')
        elif option == 3:
            print('Se ha finalizado el programa a petición del usuario')
            print()
        else:
            print()
            print('La opción seleccionada no se encuentra en el menú')

main()