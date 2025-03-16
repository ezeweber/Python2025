cant = int(input("Ingrese la cantidad de numeros de su lista: "))
lista = [int(input(f"Ingrese numero {i+1}:")) for i in range(cant)]
for num in lista:
    if num < 0:
      print("Se encontro un numero Negativo")
      break
    print(num)