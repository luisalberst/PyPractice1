## Función para saber si un año es bisiesto

def nyear(year):  
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print('El año',year,'es bisiesto')
    else:
        print('El año',year,'no es bisiesto')


print('Función para evaluar si un año es bisiesto o no')
print('Introduce el año a evaluar (Esta funcion solo leera los primeros 4 caracteres númericos ingresados)')
nyear(int(input()[:4]))