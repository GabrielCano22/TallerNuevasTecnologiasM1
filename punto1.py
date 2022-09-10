#OPCION 1
numeros=int(input("Digite la cantidad de numeros que usted desea consultar: "))
multiplo2=0
multiplo3=0
for i in range(numeros):
    contenedor=int(input('Digite un numero para almacenar'))
    if contenedor%2==0:
       multiplo2+=1
    elif contenedor%3==0:
        multiplo3+=1;
print(f"La cantidad de multiplos de 2 es: {multiplo2} y de 3 es: {multiplo3}")

#OPCION 2
numeros = []

cantidad = int(input('Digite la cantidad de numeros que desea ingresar: '))
if(cantidad == 0):
    print('La cantidad debe ser mayor a 0')
else:
    while(cantidad > 0):
        numero = int(input('Digite el numero: '))
        numeros.append(numero)
        cantidad = cantidad - 1
    else:
        for i in numeros:
            validacion2 = i % 2 
            validacion3 = i % 3 

            if(validacion2 == 0):
                print(f"El numero ",i,"Es multiplo de 2")
            elif(validacion3 == 0):
               print(f"El numero ",i,"Es multiplo de 3")
            else:
              print(f"El numero ",i,"No es multiplo de 2 ni de 3")