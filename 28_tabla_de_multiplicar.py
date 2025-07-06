from os import system
from tabulate import tabulate

def limpiar_pantalla():
    system("clear||cls")

def introducir_numero():
    while True:
        limpiar_pantalla()
        cadena = input(f"Introduzca un número (0 para salir): ")
        if cadena == "0":
            print("Hasta luego Lucas")
            exit()
        try:
            valor = int(cadena)
            if valor > 0:
                return valor
            else:
                print("Introduzca un número positivo")
                input("Pulse enter para continuar")
        except:
            print("Introduzca un número entero")
            input("Pulse enter para continuar")

def seleccionar_modo():
      while True:
        limpiar_pantalla()
        print("1 - Usando bucle for")
        print("2 - Usando bucle while")
        cadena = input(f"Introduzca cómo desea operar: ")
        if cadena == "1":
            return "for"
        elif cadena == "2":
            return "while"
        else:
            print("Escoja una de las opciones")
            input("Pulse enter para continuar")

while True:
    limpiar_pantalla()
    num = introducir_numero()
    modo = seleccionar_modo()
    tabla = []
    if modo == "for":
        for i in range(11):
            tabla.append([num, "x", i, "=", num*i])
    if modo == "while":
        i = 0
        while i <= 10:
            tabla.append([num, "x", i, "=", num*i])
            i += 1
    limpiar_pantalla()
    print(f"Tabla de multiplicar del {num}:")
    print(tabulate(tabla,tablefmt="plain"))
    input("Pulse enter para continuar")
