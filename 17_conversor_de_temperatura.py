from os import system

def pausa():
    input("Pulse enter para continuar")

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

def menu_unidad():
    limpiar_pantalla()
    while True:
        print("a - Grados centígrados\nb - Grados Fahrenheit\nc - Grados Kelvin\nq - Salir")
        opcion = input("¿Qué unidad desea introducir?: ")
        if opcion == "q" or opcion == "Q":
            exit()
        elif opcion == "a" or opcion =="A":
            return "celsius"
        elif opcion == "b" or opcion =="B":
            return "fahrenheit"
        elif opcion == "c" or opcion =="C":
            return "kelvin"
        else:
            impripausa("Por favor, seleccione una opción válida")

def introducir_cantidad(cadena):
    while True:
        limpiar_pantalla()
        entrada = input(f"Introduzca la temperatura en grados {cadena}: ")
        try:
            grados = float(entrada)
            if (grados >= 0 and cadena == "kelvin") or (grados >= -273.15 and cadena == "celsius") or (grados >= -459.67 and cadena == "fahrenheit"):
                return grados
            else:
                impripausa("La temperatura no puede ser inferior al 0 absoluto")
        except:
            impripausa("Introduzca una temperatura válida")

while True:
    opcion = menu_unidad()
    grados = introducir_cantidad(opcion)
    if opcion == "celsius":
        celsius = grados
        fahrenheit = (celsius * 9 / 5) + 32
        kelvin = celsius + 273.15
    if opcion == "kelvin":
        kelvin = grados
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9 / 5) + 32
    if opcion == "fahrenheit":
        fahrenheit = grados
        celsius = (fahrenheit - 32) * 5 / 9
        kelvin = celsius + 273.15
    impripausa(f"El resultado son:\n{celsius} grados Celsius\n{kelvin} grados Kelvin\n{fahrenheit} grados Fahrenheit")

        
