from os import system

IMC = [
    [0, "Delgadez Severa"],
    [16, "Desgadez Moderada"],
    [17, "Delgadez Leve"],
    [18.5, "Normal"],
    [25.01, "Preobeso"],
    [30, "Obesidad leve"],
    [35, "Obesidad media"],
    [40, "Obesidad mórbida"]
]

def pausa():
    input("Pulse enter para continuar")

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

def imprimir_menu():
    limpiar_pantalla()
    print("1 - Sistema métrico decimal")
    print("2 - Sistema anglosajón de unidades")
    print("0 - Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Hasta luego lucas")
        exit()
    elif opcion == "1":
        return "metrico"
    elif opcion == "2":
        return "anglosajon"
    else:
        impripausa("Introduzca una opción válida")

def introduce(dato):
    while True:
        limpiar_pantalla()
        entrada = input(f"Introduzca {dato}: ")
        try:
            valor = float(entrada)
            if valor > 0:
                return round(valor,2)
            else:
                print(f"{dato.capitalize()} debe ser mayor que 0")
        except:
            print("Introduzca una cifra válida")
        pausa()

while True:
    unidad = imprimir_menu()
    if unidad == "metrico":
        peso = introduce("peso en kg")
        altura = introduce("altura en cm")
    if unidad == "anglosajon":
        peso = introduce("peso en libras")*0.4535923699993531
        altura = introduce("altura en pies")*30.48
    imc=round((peso/(altura/100)**2),2)
    for i in IMC:
        if imc >= i[0]:
            resultado = i[1]
    impripausa(f"El IMC es de {imc}, es decir, {resultado}")