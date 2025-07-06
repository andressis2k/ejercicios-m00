from os import system

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

def entrada(pregunta):
    while True:
        limpiar_pantalla()
        cadena=input(pregunta+" S/N: ")
        if cadena == "q" or cadena == "Q":
            print("Hasta luego lucas")
            exit()
        elif cadena == "s" or cadena == "S" or cadena == "y" or cadena == "Y":
            return True
        elif cadena == "n" or cadena == "N":
            return False
        else:
            impripausa("Introduzca una respuesta válida")

while True:
    limpiar_pantalla()
    print("Bienvenido al sistema de diagnóstico")
    impripausa("Pulse q en cualquier pregunta para salir")
    if entrada("¿Arranca?"):
        if entrada("¿Suena un clic-clic?"):
            impripausa("Reemplaza la batería")
        else:
            if entrada("¿Se enciende el coche pero no arranca?"):
                impripausa("Revisa las bujías")
            else:
                if entrada("¿Arranca el coche y luego se cala?"):
                    if entrada("¿Tiene el coche inyección de combustible?"):
                        impripausa("Lleve el coche al taller")
                    else:
                        impripausa("Abre y cierra el starter")
                else:
                    impripausa("Pues no sé qué hacer. No me han programado para eso")
    else:
        if entrada("¿Están los bornes de la batería corroidos?"):
            impripausa("Limpia los bornes y arranca de nuevo")
        else:
            impripausa("Reemplaza los cables y arranca de nuevo")
                    