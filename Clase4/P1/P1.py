# Calculo de si una persona es mayor de edad o no

info = '## Programa para calcular si la edad ingresada cumple con la mayoria de Edad de 18 años ##'
print (info)
print()
edad = int(input('Hola, Usuario. ¿Ingrese su edad? '))
print()
if edad >= 18:
    print('- La Edad ingresada de',edad,'por el usuario, cumple con la mayoria de Edad.')
elif edad < 18:
    print('- La Edad ingresada de',edad,'por el usuario, no cumple con la mayoria de Edad.')