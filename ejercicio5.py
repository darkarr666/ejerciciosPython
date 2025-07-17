def pedirEdad():
    try:
        entrada = input("Ingresa una edad o escribe 'fin' para imprimir todas las edades: ")
        if int(entrada) >= 0:
            return entrada
        else:
            print("No se aceptan edades negativas")
    except ValueError:
        if entrada.lower()  == "fin":
            return "fin"
        else:
            print("Entrada no valida, vuelva a intentar")

        
def mostrarResultados(lista):
    print("Las edades ingresadas fueron: ", ", ".join(str(numero)for numero in lista))

edades = []
while True:
    entrada = pedirEdad() # Llamada a pedirEdad
    if str(entrada) == "None":
        None
    else:
        if entrada == "fin":
            break
        edades.append(entrada) 

if edades: #Si el arreglo de edades no está vacío, imprimimos las edades
    mostrarResultados(edades) #Llamada a mostrarResultados
else: 
    print("No se ingresó ninguna edad :) ")