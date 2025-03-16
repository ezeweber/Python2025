print ("Lista de numeros, a imprimir solo los pares")
lista = [1,4,5,7,14,25,58,-1,67,109]
for i in (lista):
    if (i%2 != 0):
        continue
    print(i)