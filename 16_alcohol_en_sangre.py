from os import system

def pausa():
    input("Pulse enter para continuar")

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

def introducir_dato(texto):
    while True:
        limpiar_pantalla()
        cadena = input(f"{texto}: ")
        try:
            valor = int(cadena)
            if valor > 0:
                return valor
            else:
                impripausa("Introduzca un número positivo")
        except:
            impripausa("Introduzca un número entero")

def otramas():
    while True:
        limpiar_pantalla()
        cadena = input(f"¿Introducir otra bebida? (S/N): ")
        if cadena == "s" or cadena == "S" or cadena == "y" or cadena == "Y":
            return True
        elif cadena == "n" or cadena == "N":
            return False
        else:
            impripausa("Introduzca una respuesta válida")

def introducir_bebida():
    bebidas = introducir_dato("Numero de bebidas")
    volumen = introducir_dato("Volumen tomado en cc")
    grado = introducir_dato("Grado alcohólico")
    return bebidas, volumen, grado

while True:
    lista = []
    alcohol = 0
    continuar = True
    while continuar:
        bebidas, volumen, grado = introducir_bebida()
        lista.append([bebidas,volumen,grado])
        continuar = otramas()
    horas = introducir_dato("¿Horas transcurridas?")
    for bebida in lista:
        alcohol += bebida[0] * bebida[1] * bebida[2] * 0.8 / 100
    ube = alcohol / 10
    ai = ube * 0.3
    ar = round((ai - 0.15 * horas),2)
    print(f"Alcohol en sangre: {ar} g/l")
    print(f"{"No puede conducir" if ar >= 0.5 else "Puede conducir"}")
    entrada = input("Pulse enter para continuar. q para salir: ")
    if entrada == "q" or entrada == "Q":
        print("Hasta luego Lucas")
        exit()
