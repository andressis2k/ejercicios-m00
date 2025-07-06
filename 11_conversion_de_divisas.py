from tabulate import tabulate
from os import system

def limpiar_pantalla():
    system("clear||cls")
"""
dolares = float(input("Introduzca la cantidad en dólares: "))
tasa = float(input("Introduzca la tasa de cambio (cuantos euros vale un dólar): "))
total = round((dolares/tasa),2)
print (f"{dolares} dólares a una tasa de cambio de {tasa}\nTotal {total} €")
"""

TASAS = [
    {'moneda': 'GBP', 'pais': 'Reino Unido', 'tasa': 0.86240174},
    {'moneda': 'USD', 'pais': 'Estados Unidos', 'tasa': 1.1771787},
    {'moneda': 'IDR', 'pais': 'Indonesia', 'tasa': 19078.59},
    {'moneda': 'VND', 'pais': 'Vietnam', 'tasa': 30934.628},
    {'moneda': 'THB', 'pais': 'Tailandia', 'tasa': 38.073994},
    {'moneda': 'SGD', 'pais': 'Singapur', 'tasa': 1.5003142}
    ]

lista = []
for index, tasa in enumerate(TASAS, start=1):
    lista.append([index,tasa["moneda"],tasa["pais"],tasa["tasa"]])


def imprimir_lista():
    print(tabulate(lista,headers=["Índice","Moneda","País","Tasa"]))

def elegir_moneda():
    while True:
        limpiar_pantalla()
        imprimir_lista()
        entrada = input("Escoja una moneda. 0 para salir: ")
        if entrada == "0":
            print("Hasta luego lucas")
            exit()
        try:
            opcion = int(entrada)
            if opcion < 1 or opcion > len(lista):
                print (f"Introduzca una opción del 1 al {len(lista)}")
            else:
                return(opcion)
        except:
            print("Introduzca un número")
        input("Presione enter para continuar")

def entrar_cantidad():
    while True:
        limpiar_pantalla()
        entrada = input("Introduzca una cantidad: ")
        try:
            euros = round(float(entrada), 2)
            if euros < 0:
                print("Introduzca una cantidad positiva")
            else:
                return euros
        except:
            print("Introduzca un importe numérico")
        input("Presione enter para continuar")


while True:
    opcion = elegir_moneda()
    limpiar_pantalla()
    print (f"Ha seleccionado {lista[opcion-1][2]}")
    tasa = lista[opcion-1][3]
    moneda = lista[opcion-1][1]
    euros = entrar_cantidad()
    print (f"{euros} euros son {tasa * euros} {moneda}")
    print ("¡Buen viaje!")
    input("Presione enter para continuar")