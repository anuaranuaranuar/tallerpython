
frutas={
    "Manzana":[1.35],
    "Platano":[0.80],
    "Pera":[0.85],
    "Naranja":[0.70]
    }

frut=input("¿Que fruta dese comprar? ")

if frut in frutas:
    print("El kilo de esta fruta cuesta",frutas.get(frut))
else:
    print ("No se encuentra esta fruta")
