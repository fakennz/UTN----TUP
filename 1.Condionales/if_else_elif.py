#1- A partir del ingreso de la altura en centímetros
#  de un jugador de baloncesto, el programa deberá determinar
#  la posición del jugador en la cancha, considerando los siguientes
#  parámetros:

ingresar_altura = int(input("Ingrese su altura en Centimetros: "))

if ingresar_altura < 160:
    print("Tu posicion para la cancha es: Base")
elif ingresar_altura < 180 and ingresar_altura > 159:
    print("Tu posicion para la cancha es: Escolta")
elif ingresar_altura < 200 and ingresar_altura > 179:
    print("Tu posicion para la cancha es: Alero")
elif ingresar_altura > 199:
    print("Tu posicion para la cancha es: Ala-Pivot o Pivot")

#2-Calcular una nota aleatoria entre el 1 y el 10 inclusive,
#  para luego mostrar un mensaje según el valor:

ingresar_nota = int(input("Ingrese tu nota (1-10): "))

if ingresar_nota > 10:
    print("Ingrese una nota valida")
elif ingresar_nota > 5:
    print(f"Promoción directa, la nota es {ingresar_nota}")
elif ingresar_nota > 3:
    print(f"Aprobado, la nota es {ingresar_nota}")
else:
    print(f"Desaprobado, la nota es: {ingresar_nota}")

