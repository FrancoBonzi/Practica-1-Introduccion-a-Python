import random

numero_secreto = random.randint(1, 50)

cantidadDeIntentos = 0
maximoDeIntentos = 5
numeroEncontrado = False

print("Bienvenidos al juego")
print("Debe adivinar el número que va desde 1 al 50")
print(f"Tenés un máximo de {maximoDeIntentos} intentos.\n")

while cantidadDeIntentos < maximoDeIntentos and not numeroEncontrado:
    numero = int(input("Ingrese un número: "))

    
    if numero >= 1 and numero <= 50:
        cantidadDeIntentos = cantidadDeIntentos + 1  

        if numero == numero_secreto:
            print(f"Adivinaste el número secreto en el intento {cantidadDeIntentos}")
            numeroEncontrado = True
        elif numero < numero_secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

        print("Intentos restantes:", maximoDeIntentos - cantidadDeIntentos)
        print() 

    else:
        print("Error: el número válido es entre 1 y 50.\n")

if not numeroEncontrado:
    print("¡Perdiste! El número secreto era:", numero_secreto)
