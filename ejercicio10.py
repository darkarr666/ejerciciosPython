import re

def limpiar_texto(texto):
    nuevo_texto = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', texto).lower() #en esa parte, r es para eliminar \n o \t cosas así, tipo saltos de linea
                                                        # luego sigue la expresión regular, el ^es una negación, es decir, esta parte elimina todo
                                            # lo que NO está en ese conjunto, entonces deja a-z, A-Z, y todas las acentuadas y ñ Ñ
                            # .sub es "substitute" o "sustituír" 
                            # sintaxis re.sub("a", "X", "casa")  ➜  "cXsX" \s representa espacios en blancos, para que los deje, es de space

    return nuevo_texto
    

def contar_palabras(texto):
    palabras = texto.split()
    return palabras

def imprimir_reporte(diccionario):
    print("")
   

def main():
    texto = input("Ingresa una frase, luego se contarán cuantas veces aparece cada palabra de esta misma: ")
    nuevo_texto = limpiar_texto(texto)
    print(contar_palabras(nuevo_texto))
    


if __name__ == "__main__": 
    main()