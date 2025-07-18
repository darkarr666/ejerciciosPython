#Este programa pide nombre y edad, y nos indica si podemos entrar a una fiesta si somos mayores de 18, además de que si somos mayores de 21
#podemos consumir bebidas alcoholicas

nombre = input("¿Como te llamas?") #ingresamos el nombre en un input
edad = int(input("¿Cuantos años tienes?")) #ingresamos la edad en un input tipo int

if edad < 18: #If, elif y else para considerar todos los casos
    print(f"Hola {nombre.capitalize()}, disculpa no puedes entrar a la fiesta.")
elif 18 <= edad < 21:
    print(f"Hola {nombre.capitalize()}, puedes entrar a la fiesta.")
else:
    print(f"Hola {nombre.capitalize()}, puedes entrar a la fiesta y tomar bebidas alcoholicas.")