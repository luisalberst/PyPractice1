# Calculo de numeros impares leyendo valores de inicio y final ingresados por el usuario

# Se pide ingresar los numeros a calcular
nstart = int(input('¿Ingresa el número inicial? '))
nend = int(input('¿Ingresa el número final? '))

# Se define lista como una lista o array [] para almacenar los valores
lista = []

# Se inicia el calculo de números

for number in range(nstart, nend+1):
    if (number % 2 != 0):
        lista.append(number)

print('La cantidad de números impares que existen entre',nstart,'y',nend,'es:')
print(lista)