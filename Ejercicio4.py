import math

def area(radio):
    areacir=(math.pi*math.pow(radio,2))
    return areacir

par=float(input("Ingrese el radio "))
total=area(par)

print("El area del circulo es: ",total)
