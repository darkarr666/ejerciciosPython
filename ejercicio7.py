lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17] # Definimos listas
pares = []
for numero in lista: # Recorremos la lista principal
    if numero % 2 == 0: # Si el modulo de la división de cada numero entre 2, agrega el numero a la liasta vacía 
        pares.append(numero)
print("Lista de pares: ", ", ".join(str(numero)for numero in pares)) # Imprimimos la lista de pares

