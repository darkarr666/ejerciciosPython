nombre = input("¿Como te llamas?") #Primero pedimos el nombre con input, le asignamos ese input a una variable, obviamente uwu.
edad = int(input("¿Cuantos años tienes?")) #Ahora pedimos la edad, usamos int(input()) para que la entrada sea un numero entero.

if edad >= 18: #if básico
    print(f"Hola {nombre.capitalize()}, eres mayor de edad")
else:
    print(f"Hola {nombre.capitalize()}, eres menor de edad")



