#Este programa te indica si eres mayor o menor de edad con un if

nombre = input("¿Como te llamas?") #Primero pedimos el nombre con input, le asignamos ese input a una variable, obviamente uwu.
edad = int(input("¿Cuantos años tienes?")) #Ahora pedimos la edad, usamos int(input()) para que la entrada sea un numero entero.

if edad >= 18: #if básico
    print(f"Hola {nombre.capitalize()}, eres mayor de edad.") #Usamos f-string como buena práctica de python, solo debemos poner 
else:
    print(f"Hola {nombre.capitalize()}, eres menor de edad.")
