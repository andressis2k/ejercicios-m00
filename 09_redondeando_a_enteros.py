import math
from os import system

def limpiar_pantalla():
    system("clear||cls")

# Cuántos m2 se pueden pintar con un bote de 5 litros de pintura
RENDIMIENTO = 100

def introduce(medida):
    while True:
        entrada = input(f"Introduce el {medida} de la habitación ")
        try:
            if float(entrada)>0:
                return float(entrada)
            else:
                print("La medida debe ser positiva")
        except:
            print("Introduce un número")

def menu_forma():
    while True:
        print("¿Qué forma tiene la habitación?")
        print("1 - Rectangular")
        print("2 - Redonda")
        print("3 - Forma de L")
        valor = input("Seleccione una opción (0 para salir): ")
        if valor == "0":
            exit()
        if valor == "1":
            return "rectangular"
        elif valor == "2":
            return "redonda"
        elif valor == "3":
            return "formal"
        else:
            print("Opción incorrecta")

while True:
    limpiar_pantalla()
    forma = menu_forma()
    if forma == "rectangular":
        ancho = introduce("ancho")
        largo = introduce("largo")
        superficie = largo * ancho
    if forma == "redonda":
        diametro = introduce("diámetro")
        superficie = math.pi * (diametro/2)**2
    if forma == "formal":
        ancho1 = introduce("ancho del cuerpo principal")
        largo1 = introduce("largo del puerpo principal")
        ancho2 = introduce("ancho del saliente")
        largo2 = introduce("largo del saliente")
        superficie = ancho1 * largo1 + ancho2 * largo2
    litros = superficie * 5 / RENDIMIENTO
    botes = math.ceil(superficie / RENDIMIENTO)
    print(f"Necesitarás {round(litros,2)} litros para pintar {round(superficie,2)} metros cuadrados de techo")
    print(f"Tendrás que comprar {botes} botes de pintura")
    input("Presione enter para continuar")