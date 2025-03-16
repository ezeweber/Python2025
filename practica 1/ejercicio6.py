lista = [1,4,5,7,14,25,58,-1,67,109]
listaImpar = []
listaPar = []
for i in (lista):
    if (i%2 != 0):
        listaImpar += [i]
    else:    
        listaPar += [i]
print ("Lista de numeros IMPARES")
print(listaImpar)
print ("Lista de numeros PARES")
print(listaPar)