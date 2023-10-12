from random import randint

inicio = [{
    '1': [0,1,2,3],
    '2': [4,5,6,7],
    '3': [8,9] #que luego se agreguen segun los resultaados de las anteriores
},{
    '1': [1,2,3,4],
    '2': [5,6,7,8],
    '3': [0,9] 
},{
    '1': [2,4,6,8],
    '2': [1,3,5,7],
    '3': [0,9] 
},{
    '1': [1,3,5,7],
    '2': [2,4,6,8],
    '3': [9,0] 
}]

ganar = False
num_dichos = []
numeros_fijos = [0,1,2,3,4,5,6,7,8,9] # núemros que se sabe que pueden ser

while ganar == False:
    list_pc = []
    while True: # o que haga un número aleatorio 
        i = randint(0,9) # se escoje un número del 0 al 9
        if i not in list_pc and i in numeros_fijos: # si no aparece en la lista hecha y aparece en los posibles numeros
                list_pc.append(i) # que se agrege, de otra forma que se repita el ciclo
        if len(list_pc) == 4: # hasta tener 4 dígitos diferentes
            break
    print(list_pc)
    
    while True:
        picas = int(input("Ingrese el número de picas: "))
        fijas = int(input("Ingrese el número de fijas: "))
        total = picas + fijas
        if total > 4:
            print("Has ingresado mas de 4 picas y fijas")
        else:
            break
    
    if total > 0:
        num_dichos.append({"numero": list_pc, "picas": picas, "fijas": fijas}) # diccionario para saber cuales numeros ha dicho
    print(num_dichos)

    # 

    if total == 0: # si no hay picas ni fijas, se eliminan esos núemros para futuras combinaciones
        for i in list_pc:
            numeros_fijos.remove(i)

    if fijas == 4: #si hay 4 fijas se gana xd
        ganar = True
print("He ganado :)")