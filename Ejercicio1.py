def prod(num1,num2):
    tot=num1*num2
    return tot

a=int(input ("Ingrese un numero "))
b=int (input("Ingrese otro numero "))

total=prod(a,b)

suma=a+b

if total>1000:
    print(total," Y la suma es: ",suma)
else:
    print(suma)

