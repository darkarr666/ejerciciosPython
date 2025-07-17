#este programa nos pregunta la edad, y verifica que la edad sea un número positivo, además de que también verifica que sea un número entero 
# y no una cadena u otro tipo de dato

while True: #usamos while True para hacer un ciclo hasta que se ingrese una edad valida 
    edad = int(input("¿Cual es tu edad?"))
    try: # Usamos try para manejar errores o exepciones, como el caso ValueError, en caso de que 
        
        if edad > 0: 
            print(f"Edad ingresada: {edad}")
            break
        else:
            print("La edad debe ser un número positivo")
    except ValueError:
        print("Entrada invalida")
        