#este ejercicio pide edades hasta ingresar "fin", luego imprime métricas, como la menor edad, mayor, promedio y la cantidad de menores

def pedirEdad(): # Aquí vamos a crear la función que pide la edad
    try: #Usaremos el try para verificar que ingrese un número, y en caso de que sea un número, igual verificamos que no sea negativo, si es positivo retornamos la entrada
        #con "return int(entrada)" esto para que se retorne un entero, y no una cadena
        entrada = input("Ingresa una edad o escribe 'fin' para imprimir todas las edades: ") #pedimos la entrada normal con input, porque 
        # lo convertimos a int o a cadena después como nos convenga
        if int(entrada) >= 0: #si la entrada (en entero) es mayor o igual que cero, retornamos int(entrada)
            return int(entrada) #retornamos la edad, como ya mencioné convertido a entero 
        else:
            print("No se aceptan edades negativas") #Si no es un número entero, imprimimos que no se aceptan edades negativas, en este caso retorna None, que vemos en 
            #la parte de if str(entrada) == "none", en la linea 38
            return None
    except ValueError: #en caso de que no sea número, verificamos que la cadena sea Fin, FIN o fin, en ese caso, retornamos la cadena "fin"
        if entrada.lower()  == "fin":
            return "fin"
        else:
            print("Entrada no valida, vuelva a intentar") #si la cadena no es fin, imprimimos eso
            return None #Igual retornamos none, para la misma comparación en la linea 38

        
def mostrarResultados(lista): #definimos la función para mostrar resultados, que no es más que imprimir la lista con un for, usando el join para que no se impriman los
    #[], y solo se imprima cada uno seguido de una coma
    print("Las edades ingresadas fueron: ", ", ".join(str(numero)for numero in lista)) #esto lo podemos ver en el ejercicio 4

def metricas(lista): #Se definen e imprimen variables necesarias con funciones para listas
    minima = min(lista)
    maxima = max(lista)
    promedio = sum(lista)/len(lista)
    print(f"Edad mínima ingresada: {minima}")
    print(f"Edad máxima ingresada: {maxima}")
    print(f"Promedio de las edades ingresadas: {round(promedio, 2)}")


contador = 0
edades = [] #definimos nuestro arreglo edades, obviamente vacío
menores = 0
while True: #Creamos un ciclo while, que se rompe hasta que entrada es igual a fin
    entrada = pedirEdad() # Llamada a pedirEdad
    if entrada == None: # Si la función nos retornó none, vamos a usar continue para omitir  esa iteración, o saltarnos esa parte, para que no se nos llene nuestra lista 
        # de "None" en caso de que ingresen un número negativo
        continue #sentencia continue, para  for y while
    else:
        if entrada == "fin": #ahora, si entrada es fin, rompemos 
            break
    edades.append(entrada) # SI no aplica ninguna condición, agrega entrada a edades
    if entrada < 18: #Si la entrada es menor que 18 aumenta el contador a 1, podría hacerse dentro de una función tipo def menores()
        contador += 1 #aumentamos contador uwu

if edades: #Si el arreglo de edades no está vacío, imprimimos las edades
    mostrarResultados(edades) #Llamada a mostrarResultados ordenados (con .sort)
    metricas(edades) #mostramos edades 
    print(f"La cantidad de menores de edad es: {contador}") #Imprimios el número de contador, el cual aumenta cuando la edad es menor a 18

else: 
    print("No se ingresó ninguna edad :) ")