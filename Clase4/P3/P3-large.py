# Números del 1 al 100 en orden inverso

# Creacion de la lista o array para almacenar numeros
n100 = []
# Funcion para almacenar números en la lista o array
for number in range(1,101):
    n100.append(number)

n = sorted(n100, reverse=True)

for i in n:
    print(i) 