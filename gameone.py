# Juego de adivinazas mejorado
import random
intento = 0 
var = random.randint(1,10)
while intento < 4:  
    var1 = int(input("ingrese un numero entre 1 y 10: "))
    intento = intento + 1
    if var1 + 1 == var or var1 - 1 == var:
        print("casi lo atinas, CALIENTE!")
    if var1 != var and (var - 1) > var1 or (var + 1) < var1:
        print("estas FRIO!")
    if var1 == var:
        print("adivinastes el numero")
        break
print("el numero era ", var)
