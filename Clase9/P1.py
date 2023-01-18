print("Introduce países separados por comas")
print("Paises repetidos no se tomaran en cuenta una segunda vez")
items = input("-> ")

paises = [pais for pais in items.split(",")]

print("Los paises que has introducido alfabeticamente son: ")
print(",".join(sorted(list(set(paises)))))