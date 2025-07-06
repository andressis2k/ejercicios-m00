from os import system

YARD = 0.9144

def limpiar_pantalla():
    system("clear||cls")

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

def pedir_unidad():
    while True:
        limpiar_pantalla()
        print("¿Qué unidad deseas introducir?\n1 - Metros cuadrados\n2 - Yardas cuadradas\n0 - Salir")
        entrada = input("Seleccione una opción: ")
        if entrada == "0":
            print("Hasta luego lucas")
            exit()
        if entrada == "1":
            return "m2"
        elif entrada == "2":
            return "y2"
        else:
            print("Opción no válida")
            input("Pulse enter para continuar")
while True:
    unidad = pedir_unidad()
    ancho = introduce("ancho")
    largo = introduce("largo")
    if unidad == "y2":
        ancho = ancho * YARD
        largo = largo * YARD

    superficiem2 = ancho * largo
    superficieyardas = round(superficiem2 / (YARD**2), 2)
    print(f"La habitacíon mide {superficiem2} metros cuadrados, o lo que es lo mismo, {superficieyardas} yardas cuadradas")
    input("Pulse enter para continuar")
