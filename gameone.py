# Juego de adivinasas
import random
intento = 0 
var = random.randint(1,10)
while intento < 4:  
    var1 = int(input("ingrese un numero entre 1 y 10: "))
    intento = intento + 1
    if var1 != var:
        print("nada sigue")
    if var1 == var:
        print("adivinastes el numero")
        break
print("el numero era ", var)
