# Este programa pide una frase y cuenta cuantas veces aparece cada palabra dentro de esta frase

def imprimir_palabras(texto):    
    print("el texto contiene algo.")
   

def main():
    while True:
        texto = input("Ingrese un texto, posteriomente se indicará cuantas veces se usó cada palabra en él: ")
        if texto:
            imprimir_palabras(texto)  
            break 
        else:
            print("el texto está vacío")
            continue

if __name__ == "__main__":
    main()