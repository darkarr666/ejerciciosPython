import re

def limpiar_texto(texto):
    nuevo_texto = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', texto).lower() #en esa parte, r es para eliminar \n o \t cosas así, tipo saltos de linea
                                                        # luego sigue la expresión regular, el ^es una negación, es decir, esta parte elimina todo
                                            # lo que NO está en ese conjunto, entonces deja a-z, A-Z, y todas las acentuadas y ñ Ñ
                            # .sub es "substitute" o "sustituír" 
                            # sintaxis re.sub("a", "X", "casa")  ➜  "cXsX" \s representa espacios en blancos, para que los deje, es de space

    return nuevo_texto
    

def contar_palabras(texto):
    palabras = texto.split() # Divide el texto por espacios, o sea, retorna un arreglo que contiene todas las palabras 
    conteo = {} # definimos nuestro diccionario vacío

    for palabra in palabras:
        if palabra in conteo: # aquí decimos "si la palabra está en el conteo, le sumamos uno al valor"
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1 # Si no está en el diccionario conteo, la agregamos con el valor 1
    return conteo

def imprimir_reporte(diccionario):
    print("Palabras encontradas")
    for palabra in sorted(diccionario): #sorted ordena alfabeticamente el arreglo o tupla o lo que sea
        print(f"Palabra {palabra} se encontró -> {diccionario[palabra]} veces ") 
   

def main():
    texto = input("Ingresa una frase, luego se contarán cuantas veces aparece cada palabra de esta misma: ")
    nuevo_texto = limpiar_texto(texto)
    conteo = contar_palabras(nuevo_texto)
    imprimir_reporte(conteo)
    


if __name__ == "__main__": 
    main()