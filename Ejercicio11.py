diccionario={}
desicion=True

x=int(input("¿Cuantas palabras desea Ingresar?: "))

for x in range(x):
    fraseespañol=input("Ingrese una palabra en español: ")
    fraseingles=input("Ingrese la traduccion de la palabra anterior: ")
    diccionario[fraseespañol]=fraseingles

while(desicion):
    traducir=input("Ingrese una plabra para saber su traduccion en ingles: ")

    if traducir in diccionario:
        print("La Traduccion de "+ traducir +" es: "+ " "+ diccionario[traducir])
        print(" ")
        y=input("¿Desea Traducir otra palabra? (y/n)")
        if y=='n':
            desicion=False     
    else:
        print("Ha ocurrido un error, no se ha podido traducir")
        print (traducir)
        desicion=False

