
lista=[]
num=0
control=0
prom=0
for k in range (0,10):
    datos=int(input("Ingrese un valor: "))
    lista.append(datos)
    prom=prom+lista[k]
    if lista[k]==5:
        num+=1
    if lista[k]>control:
        control=lista[k]
    

print (lista)
print ("Hay",num," veces 5")
print ("El numero mayor es: ",control)
print ("El promedio es: ",prom/10)

