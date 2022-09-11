# Juego Geografos no tengo tildes. Version 2.0

import random

P = [["¿ Oceano mas grande del Mundo ?: ", "Pacifico"], ["¿ Cual es la capital de Francia ?: ", "Paris"], ["¿ Cual es el pais que tiene Berlin como su capital ?: ", "Alemania"], ["¿ Cual es la selva mas grande del mundo ?: ", "La Amazonia"], ["¿ Capital de Irlanda del Norte?: ", "Belfast"]]
random.shuffle(P)
a = 0
b = 0
for i in range(0, len(P), 1):
    user_input = input(P[i][0])
    if user_input.lower() == P[i][1].lower():
        print("¡ CORRECTO !")
        a = a + 1
    elif user_input.lower() != P[i][1].lower():
        print("Respuesta incorrecta")
        b = b + 1
    print(str(a) + " buena[s] respuesta[s] y " + str(b) + " mala[s]" )

    








