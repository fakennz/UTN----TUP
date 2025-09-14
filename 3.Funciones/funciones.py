#1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.


def ingresar_entero():
    numero_int = int(input("Ingrese un numero entero: "))
    return numero_int


#2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.


def ingresar_flotante():
    numero_float = float(input("Ingrese un numero flotante: "))
    return numero_float


#3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 


def ingresar_cadena():
    cadena = str(input("Ingrese una cadena de texto: "))
    return cadena


#4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 


def calcular_area_triangulo(base, altura):
    area = base * altura
    return area


#5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.


def calcular_area_circulo(radio):
    pi =  3.14159  
    area = (radio ^ 2) * pi
    return area 



#6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.


def verificar_par(numero):
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print("no es par")


#7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.


def verificar_par_t_o_f(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
        
        


#8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.


def maximo_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        maximo = n1
    elif n2 > n1 and n2 > n3:
        maximo = n2
    else:
        maximo = n3
    print(maximo)


#9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.


def calcular_potencia(base, exponente):
    calculo = base ** exponente
    print(calculo)


#10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.


def verificar_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
        else:
            return True


#11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for),
#muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro.
#La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.


def verificar_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def contador_primos(numero):
    contador_de_primos = 0
    for i in range(2, numero + 1):
        bandera = verificar_primo(i)
        if bandera:
            contador_de_primos += 1
    return contador_de_primos

def cant_primos(numero):
    contador = contador_primos(numero)
    return contador





#12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
#La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.


def tabla_multiplicadora(numero, inicio = 1, fin = 10 ):
    for i in range(inicio, fin + 1):
        print(f"{numero} X {i} = {numero * i}") 


#13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

def pedir_dato_y_tipo(dato:int|float|str, tipo: type) -> float|int|str:
    resultado = None
    if type(dato) == tipo:
        resultado = dato
    return resultado

pedir_datos = pedir_dato_y_tipo("Hola",str)
print(pedir_datos)