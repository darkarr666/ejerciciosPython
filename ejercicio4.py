#este programa nos pide edades hasta que escribamos fin, en ese momento imprime todas las edades ingresadas (almacenadas en un arreglo)
# las imprime, nos dice cuantas son (con len(arreglo)) y saca el promedio de todas.

arreglo = []

while True:
    entrada = input("Ingresa una edad o escribe 'fin' para terminar: ")
    try:
        numero = int(entrada)
        if numero >= 0:
            print("Edad registrada!")
            arreglo.append(numero)
        else:
            print("Ingrese un número positivo")
    except ValueError:
        if entrada.lower() == "fin":
            break
        else: 
            print("Entrada invalida")

# Este for imprime correctamente las edades, pero con un salto de linea
"""
print("Edades registradas: ")
for numero in arreglo:
    print(numero)
    """
 #este otro caso convierte el arreglo de enteros, en uno de cadenas, pero va a imprimir igual los corchetes [1, 2, 3] y no se ve bien
"""arreglostr = str(arreglo)
print("Edades registradas: ", " ".join(arreglostr)) """


#para este caso es mejor usar:
print("Las edades ingresadas fueron:",", ".join(str(numero)for numero in arreglo))
#el .join está ligado al ", ", entonces, lo que hacemos es que .join
#concatena los elementos de nuestro arreglo (sobre el que iteramos) en una nueva cadena, entonces, primero iteramos sobre nuestro arreglo con el
#for, luego lo convertimos a cadena y lo imprimimos antes de una coma y espacio.

#sintaxis .join => ", ".join(mi_lista) (pero en este caso vamos a iterar sobre cada elemento del arreglo, para no convertir todo nuestro arreglo en cadenas)

print(f"Total de edades: {len(arreglo)}")

promedio = sum(arreglo)/len(arreglo) #algo normal, hacemos el promedio

print(f"El promedio de las esades es: {promedio:.2f}") #Ponemos dos decimales al promedio
#también podemos usar "print(f"El promedio es: {round(promedio, 2)}")" para que por ejemplo 14.0 se quede como 14.0 y no como 14.00
