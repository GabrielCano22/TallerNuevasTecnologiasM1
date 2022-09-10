from itertools import product
from turtle import clear

print("***MENU***")
print("0. SALIR")
print("1. INGRESAR PRODUCTO")
print("2. VER PRODUCTOS INGRESADOS")
print("3. LEER CODIGO Y EDITAR PRECIO")
print("4. LEER CODIGO Y ELIMINAR PRODUCTO")
eleccion=100
seleccion=""
#Codigo
#Nombre
#Precio

productos=[]
while(eleccion!=5):
    producto={}
    eleccion=int(input("Elija una opción: "))
    if(eleccion==1):
            producto['codigo']=int(input("Digite el codigo del producto: "))
            producto['nombre']=input("Digite el nombre de ese producto: ")
            producto['precio']=int(input("Digite el precio del producto: "))
            print("Agregando producto")
            productos.append(producto)
    elif(eleccion==2):
        print(productos)
    elif(eleccion==3):
        cod=int(input("Digite el codigo del producto que le desea cambiar el precio: "))
        for i in productos:
            if(i['codigo']==cod):
                prenuevo=int(input("Digite el nuevo precio del producto: "))
                i['precio']=prenuevo
                print("El precio del producto se ha modificado exitosamente")
            else:print(f"El codigo ingresado no se encuentra registrado")

    elif(eleccion==4):
         cod=int(input("Digite el codigo del producto que desea eliminar de los registros: "))
         for i in productos:
            if(i['codigo']==cod):
                productos.remove(i)
                print(f"Registro eliminado exitosamente")
            else:
                print(f"Este codigo no existe")
    elif(eleccion==0):
        break
    else:print("La opcion ingresada no es válida")