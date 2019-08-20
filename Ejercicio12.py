Nombre=""
Direccion=""
Telefono=""
NIF=0
Correo=""
Preferencia=False

def menu():
    print("-----------------")
    print("[1] Añadir Cliente")
    print("[2] Eliminar Cliente")
    print("[3] Mostrar Cliente")
    print("[4] Lista Todos los Clientes")
    print("[5] Lista Cliente Preferentes")
    print("[6] Terminar")
    opcion=int(input("Seleccione una opcion: "))

    return opcion
    




def Ingreso():
    Nombre=input("Ingrese Nombre: ")
    Direccion=input("Ingrese Direccion: ")
    Correo=input("Ingrese Correo: ")
    Telefono=input("Ingrese su Telefono: ")
    Preferencia=input("Ingrese Su estado de preferencia: ")
    Cliente[NIF]={"Nombre":Nombre, "Direccion": Direccion, "Telefono":Telefono, "Correo":Correo, "Preferencia":Preferencia}
    return True


Cliente={

}

op2=True





while(op2):
    dato=menu()
    
    if(dato==1):
        op3=True

        while(op3):
            op=True
            while(op):
                NIF=int(input("Ingrese NIF: "))
                if NIF in Cliente:
                    print("Este NIF ya existe!!!!!")
                    op=True
                else:
                    op=False

            if op ==False:
                res=Ingreso()
                if(res):
                    print("Ingreso Exitoso!!")
                    print(" ")
                    Decicion=input("Quieres Ingresar Otro si/no: ")
                    if(Decicion=="no"):
                        op3=False                    
                else:
                    print("Algo Fallo")
                     print(" ")
    
    if(dato==2):
        op3=True
        while(op3):
            op=True
            while(op):
                NIF=int(input("Ingrese NIF: "))
                if NIF in Cliente:
                    op=False
                else:
                    print("Este NIF no existe!!!")
                    print(" ")
                    op=True

            if op==False:
      
                del Cliente[NIF]
                print("Se elimino con Exito!!!!!!!!")
   
                Decicion=input("Quieres Eliminar Otro si/no: ")
                
                if(Decicion=="no"):
                    op3=False 
                
    if(dato==3):
        op3=True
        while(op3):
            op=True
            while(op):
                NIF=int(input("Ingrese NIF: "))
                if NIF in Cliente:
                    op=False
                else:
                    print("Este NIF no existe!!!")
                    print(" ")
                    op=True

            if op==False:
                print("Nombre: "+ Cliente[NIF]["Nombre"])
                print("Direccion: "+ Cliente[NIF]["Direccion"])
                print("Telefono: "+ Cliente[NIF]["Telefono"])
                print("Correo: "+ Cliente[NIF]["Correo"])
                print("Preferencia: "+ Cliente[NIF]["Preferencia"])
                
                 
                Decicion=input("Quieres Buscar Otro si/no: ")
                if(Decicion=="no"):
                    op3=False
                    print(" ")


    if(dato==4):
        print("NIF"+ "\t"+" Nombre")
        for traer in Cliente:
            print(traer , "\t" + Cliente[traer]["Nombre"])
        
        print(" ")


    if(dato==5):

        for traer in Cliente:
            if Cliente[traer]["Preferencia"] == "True":
                print(traer , "\t" + Cliente[traer]["Nombre"])
        print(" ")

    if(dato==6):
       op2=False

    if(dato>6):
        op2=True

    



    
