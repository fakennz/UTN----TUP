# 1 - Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

"""num_as = 0
while num_as < 10:
    num_as += 1
    print(num_as)"""

# 2 Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

"""num_des = 10
while num_des > 0:
    print(num_des)
    num_des -= 1"""

# 3 - Mostrar la suma de los números desde el 1 hasta el 10.

"""i = 0
suma = 0
while i <= 10:
    suma += i
    i += 1
print(suma)"""

# 4 - Mostrar la suma de los números pares desde el 1 hasta el 10.

"""i = 0
sum_par = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        sum_par += i
print(sum_par)"""

# 5 - Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

"""i = 0
suma = 0
while i < 5:
    num = int(input("Ingrese un numero: "))
    suma += num
    i += 1
promedio = suma / i
print(f"La suma es: {suma} y el Promedio es {promedio}")"""

# 6 - Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

"""i = 0
suma = 0
continuar = 1
while continuar == 1:
    ingresar_numero = int(input(f"Ingrese el {i + 1}° numero: "))
    suma += ingresar_numero
    i += 1
    print(f"Suma de los numeros: {suma}")
    promedio = suma / i
    print(f"Promedio de los numeros: {promedio})")
    print("Desea continuar?")
    continuar = int(input("Ingrese 1 para continuar: "))"""

# 7 - Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

"""i = 0
suma = 0
continuar = 1
producto = 1
while continuar == 1:
    ingresar_numero = int(input(f"Ingrese el {i + 1}° numero: "))
    if ingresar_numero > 0:
        suma += ingresar_numero
    elif ingresar_numero < 0:
        producto *= ingresar_numero
        i += 1
    else:
        print("Ingrese un numero correcto")
        continuar == 0
    
    print("Desea continuar?")
    continuar = int(input("Ingrese 1 para continuar: "))


print(f"Suma de los numeros positivos: {suma}")
print(f"Producto de los numeros negativos: {producto}")
"""

# 8 - Ingresar 10 números enteros. Determinar el máximo y el mínimo.

"""i = 0
bandera = False

while i < 10:
    numero = int(input("Ingrese un numero entero: "))
    if i == 0:
        maximo = numero
        minimo = numero
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    i += 1
print(f'Numero max: {maximo}')
print(f'Numero minimo: {minimo}')"""

# 9 - Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

"""i = 0
continuar = 1
suma = 0
while i < 5 or continuar == 1:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    i += 1
    if i >= 5:
        print("Desea continuar?")
        continuar = int(input("Ingrese 1 para continuar: "))
promedio = suma / i
print(f"La suma de los numeros es: {suma} y el promedio es: {promedio}")"""

# 10 - Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

"""i = 0
continuar = 1
suma = 0
while i < 5 or continuar == 1 and i < 10:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    i += 1
    if i >= 5:
        print("Desea continuar?")
        continuar = int(input("Ingrese 1 para continuar: "))
promedio = suma / i
print(f"La suma de los numeros es: {suma} y el promedio es: {promedio}")

"""

# Integrador While

# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

"""i = 0
continuar = 1
suma_neg = 0
suma_pos = 0
cant_neg = 0
cant_pos = 0
while continuar == 1:
    numero = int(input(f"Ingrese el {i + 1}° numero: "))
    if numero < 0:
        suma_neg += numero
        i += 1
        cant_neg += 1
    elif numero > 0:
        suma_pos += numero
        i += 1
        cant_pos += 1
        if cant_pos == 1:        
            maximo_pos = numero
        elif numero > maximo_pos: 
            maximo_pos = numero
    else:
        print("ingrese un numero valido")
        continuar = 0
    print("Desea continuar?")
    continuar = int(input("Ingrese 1 para continuar: "))

if cant_pos > 0:
    promedio_pos = suma_pos / cant_pos
else:
    promedio_pos = 0

if (cant_pos + cant_neg) > 0:
    porcentaje_neg = cant_neg * 100 / (cant_pos + cant_neg)
else:
    porcentaje_neg = 0

print(f"La suma acumulada de los números negativos es: {suma_neg}")
print(f"La suma acumulada de los números positivos es: {suma_pos}")
print(f"La cantidad de números negativos ingresados es: {cant_neg}")
print(f"El promedio de los números positivos es: {promedio_pos}")
print(f"El número positivo más grande es: {maximo_pos}")
print(f"El porcentaje de números negativos ingresados, respecto del total de ingresos es: {porcentaje_neg}")"""