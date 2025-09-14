# 1 - Mostrar los números ascendentes desde el 1 al 10


"""for i in range(1,11):
    print(i)
"""

# 2 - Mostrar los números descendentes desde el 10 al 1


"""for i in range(10,0,-1):
    print(i)
"""

# 3 - Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.


"""numero = int(input("Ingrese un numero: "))

for i in range(0,numero + 1):
    print(i)
"""

# 4 - Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:


"""numero = int(input("Ingrese un numero: "))

for i in range(0,11):
    print(f" {numero} x {i} = {numero * i}")"""


#	5 x 0 = 0
#	5 x 1  = 5
#	5 x 2 = 10
#	5 x 3  = 15 …

# 5 - Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

"""contador = 0
suma = 0
for i in range(10):
    numero = int(input("Ingresar un numero: "))
    if numero == 0:
        break
    else:
        suma += numero
        contador += 1

if contador > 0:
    promedio_numeros = (suma/contador)
    print(f"La suma de todos los numeros es: {suma} y el promedio es: {promedio_numeros}")
else:
    print("no se ingresaron numeros!!")"""

# 6 - Imprimir los números múltiplos de 3 entre el 1 y el 10.

"""for i in range(1,11):
    if i % 3 == 0:
        print(i)"""



# 7 - Mostrar los números pares que hay desde la unidad hasta el número 50.


"""for i in range(1,51):
    if i % 2 == 0:
        print(i)"""


# 8 - Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# 1
# 12
# 123
# 1234
# 12345

"""numero = int(input("Ingrese un numero: "))

for i in range(1,numero + 1):
    for j in range(i):
        print(f"{j + 1}", end="")
    print("")
"""
# 9 - Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

"""numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)"""

# 10 - Ingresar un número. Determinar si el número es primo o no.

"""
es_primo = True
numero = int(input("Ingrese un numero: "))
7
for i in range(2, numero + 1):
    if numero % i == 0:
        es_primo: False
        break

if es_primo:
    print(f"El numero: {numero} es primo. ")
else:
    print(f"El numero: {numero} no es primo. ")"""

    




# 11 - Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

contador_primo = 0
numero_ingresado = int(input("Ingrese un numero: "))

for i in range(2,numero_ingresado+1):
    es_primo = True

    for j in range(2,i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El numero {i} es primo")
        contador_primo += 1

print(f"Total numeros primos: {contador_primo}")
