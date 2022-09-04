# Juego para los geógrafos

a = 0
x = input("¿ Cual es la capital de Francia ?: ")
if x == "Paris" or x == "paris":
    print("¡ CORRECTO !")
    a = a + 1
elif x != "Paris" or x != "paris":
    print("Respuesta incorrecta")
montaña = input("¿ Cual es el pais que tiene Berlin como su capital ?: ")
if montaña == "Alemania" or montaña == "alemania":
    print("¡ CORRECTO !")
    a = a + 1
elif montaña != "Alemania" or montaña != "alemania":
    print("Respuesta incorecta")
amazonas = input("¿ Cual es la selva mas grande del mundo ?: ")
if amazonas == "La Amazonia" or amazonas == "la Amazonia":
    print("¡ CORRECTO !")
    a = a + 1 
elif amazonas != "La Amazonia" or amazonas != "la Amazonia":
    print("Respuesta incorrecta")
print("Tuvistes " + str(a) + " buena[s] respuesta[s]")

    








