from os import system

def limpiar_pantalla():
    system("clear||cls")

def introducir_numero():
    while True:
        limpiar_pantalla()
        cadena = input(f"Introduzca un número (0 para ejecutar): ")
        try:
            valor = int(cadena)
            return valor
        except:
            print("Introduzca un número entero")
            input("Pulse enter para continuar")

numeros = []
while True:
    numero = introducir_numero()
    if numero == 0:
        if numeros == []:
            print("No hay números para calcular. Saliendo")
            exit()
        else:
            total = 0
            texto = ""
            for index, numero in enumerate(numeros):
                if index < (len(numeros)-1):
                    texto += str(numero)+", "
                else:
                    texto += "y " + str(numero)
                total += numero
            media = round(total / len(numeros),2)
            if media == int(media): media = int(media)
            print(f"La media de {texto} es {media}")
            numeros=[]
            input("Presione enter para comenzar de nuevo")
    else:
        numeros.append(numero)