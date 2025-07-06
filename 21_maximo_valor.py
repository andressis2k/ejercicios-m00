from os import system

def limpiar_pantalla():
    system("clear||cls")

def pausa():
    input("Pulse enter para continuar")

def introducir_numero():
    while True:
        limpiar_pantalla()
        cadena = input(f"Introduzca un número (enter para ejecutar): ")
        if cadena == "":
            return ""
        try:
            valor = int(cadena)
            if valor in numeros:
                print(f"El número {valor} ya ha sido introducido. Introduzca uno diferente")
                pausa()
            else:
                return valor
        except:
            print("Introduzca un número entero")
            pausa()

# Esta función se puede sustituir por "max(numeros)"
def maximo(numeros):
    numanterior = float("-inf")
    for numero in numeros:
        if numero > numanterior:
            maximo = numero
        numanterior = numero
    return maximo

numeros = []

while True:
    numero = introducir_numero()
    if numero == "":
        if numeros==[]:
            print("No hay números. Saliendo")
            exit()
        else:
            texto = ""
            if len(numeros)==1:
                print("Sólo hay un número. No se puede calcular el máximo")
                pausa()
                continue
            for index, numero in enumerate(numeros):
                if index == 0:
                    texto = str(numero)
                elif index < (len(numeros)-1):
                    texto += ", "+str(numero)
                else:
                    texto += " y " + str(numero)
            print(f"El mayor de {texto} es {maximo(numeros)}")
            numeros = []
            pausa()
    else:
        numeros.append(numero)

