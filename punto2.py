contador = 10
diccionarios = []

while(contador > 0):
        diccionario = {}
        diccionario['nombre'] = input('Escriba el nombre de la fruta: ')
        diccionario['color'] = input('Escriba el color de la fruta: ')
        diccionario['precio'] = input('Escriba el precio de la fruta: ')
        diccionarios.append(diccionario)        
        contador = contador - 1
        if(contador > 0):
            print('Agrega otra fruta')
else:
    print('Ya inscribio todas las frutas posibles')
    print('Estas son sus frutas: ')
    for i,e in reversed(list(enumerate(diccionarios))):
        print(i,e)