## Función para evaluar si un numero entero es primo o no

def nprimo(num):  
    if num > 1:
        for a in range(2,num+1):
            if num == 2:
                print('Es un número primo')
                break
            elif num % a == 0:
                print('No es un número primo')
                break
            else:
                print('Es un número primo')
                break
    else:
        print('El número',num,'no es número primo, debido a que estos son mayores a 1')

print('Función para evaluar si un numero entero es primo o no')
print('Introduce el número a evaluar (Debe ser entero)')
nprimo(int(input()))