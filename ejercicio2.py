nombre = input("¿Como te llamas?")
edad = int(input("¿Cuantos años tienes?"))

if edad < 18:
    print(f"Hola {nombre.capitalize()}, disculpa no puedes entrar a la fiesta.")
elif 18 <= edad < 21:
    print(f"Hola {nombre.capitalize()}, puedes entrar a la fiesta.")
else:
    print(f"Hola {nombre.capitalize()}, puedes entrar a la fiesta y tomar bebidas alcoholicas.")