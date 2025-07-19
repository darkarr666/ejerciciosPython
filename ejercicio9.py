#este programa pide palabras hasta que se ingrese "fin", para luego separarlas en 3 listas diferentes dependiendo de su longitud

def pedirpalabras():
    try:
        palabra = input("Ingresa una palabra: ")
        if palabra.lower() == "fin":
            return "fin" #Si ingresamos FIN, fin o Fin, retornamos "fin"
        else:
            if len(palabra) >= 1: # Si la palabra es de lóngitud mínima 1, se retorna, si no, retornamos None
                return palabra
            else: # Si la cadena tiene longitud 0, no retornamos nada, para que no se agreguen cadenas vacías a nuestra lista
                print("No puedes ingresar cadenas vacías")
                return None
    except ValueError:
        print("Eso no es una cadena")
        return None

    
def imprimirlistas(lista, string): #pasamos la lista y la string (chicas, medianas o grandes)
    print(f"Se encontraron {len(lista)} palabras {string}: {", ".join(lista)}") #aquí, a diferencia de casos pasados, no se usa el for porque no vamos
    # a convertir int a string, ya es string entonces solo usamos .join(lista)
    print("")


def main():
    cortas = [] #definimos 3 listas vacías para llenarlas 
    medianas = []
    largas = []
    while True:
        entrada = pedirpalabras()
        if entrada == None:
            continue
        else:
            if entrada == "fin":
                break
        if len(entrada) < 5:
            cortas.append(entrada)
        elif 5 <= len(entrada) <= 8:
            medianas.append(entrada)
        else: 
            largas.append(entrada)

    print("")
    imprimirlistas(cortas, "cortas") #en este caso, pasamos dos parametros a nuestra función, la lista y una cadena con el tipo, para imprimir conforme cada lista
    imprimirlistas(medianas, "medianas")
    imprimirlistas(largas, "largas")

if  __name__ == "__main__":
    main()

