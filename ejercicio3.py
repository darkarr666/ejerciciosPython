#este programa nos pregunta la edad, y verifica que la edad sea un número positivo, además de que también verifica que sea un número entero 
# y no una cadena u otro tipo de dato

while True: #usamos while True para hacer un ciclo hasta que se ingrese una edad valida 
    try: # Usamos try para manejar errores o exepciones, como el caso ValueError, en caso de que la edad ingresada no sea un int 
        #y sea otro tipo de dato
        edad = int(input("¿Cual es tu edad?")) #aquí la edad espera un int, si no es un int, manda al except
        if edad > 0: #if para verificar que la edad sea mayor que cero
            print(f"Edad ingresada: {edad}") #Formateamos con f"" para imprimir la edad
            break # Con esto salimos del while
        else:
            print("La edad debe ser un número positivo")
    except ValueError: #excepción en caso de no recibir un int
        print("Entrada invalida") # EN caso de no recibir un int imprimimos "entrada invalida"
        