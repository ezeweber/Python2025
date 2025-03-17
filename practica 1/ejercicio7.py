cant_numeros = int(input("Ingrese la cantidad de numeros de su lista "))
lista_numeros = [int(input(f"Ingrese el {i+1}° numero: ")) for i in range(cant_numeros)]
cadena_string = " - "
for num in lista_numeros:
    if (num % 3 == 0):
        continue
    else:
        cadena_string = cadena_string + str(num) + " - "

if (cadena_string == " - "):
    print("Todos los numeros eran multiplos de 3")
else:
    print(cadena_string)
