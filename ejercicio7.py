lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
print("Lista de pares: ", ", ".join(str(numero)for numero in pares))

