from os import system

def limpiar_pantalla():
    system("clear||cls")

def entrada(valor):
    while True:
        cadena = input(f"Introduzca el número de {valor}: ")
        try:
            valor = int(cadena)
            if valor >= 0:
                return valor
        except:
            print("Introduzca un número entero positivo")

while True:
    limpiar_pantalla()
    personas = entrada("personas")
    pizzas = entrada("pizzas")
    if personas == 0:
        print("No hay nadie para comer, así que nos vamos")
        exit()
    if pizzas == 0:
        print("No hay pizzas para repartir, así que haced unos macarrones")
        exit()
    print(f"{personas} personas con {pizzas} pizzas")
    if personas%2:
        porciones = personas + 1
    else:
        porciones = personas
    print(f"Cada pizza debe dividirse en {porciones} porciones, por lo que tendremos un total de {porciones * pizzas} porciones")
     
    print(f"Cada persona tomará {pizzas} porciones y sobrarán {porciones*pizzas-pizzas*personas} porciones")
    input("Presione enter para continuar")