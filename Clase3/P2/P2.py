# Calculadora IMC
# IMC = peso [kg]/ estatura [m2]

peso = float(input('¿Ingrese su peso en Kg?'))

estatura = float(input('¿Ingrese su estatura en metros?'))

imc = round(peso / estatura**2, 2)
print('Tu índice de masa corporal es '+str(imc))
