from os import system

def limpiar_pantalla():
    system("clear||cls")

def introducir_cantidad(cadena):
    while True:
        limpiar_pantalla()
        entrada = input(f"Introduzca la cantidad {cadena}: ")
        try:
            cantidad = float(entrada)
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor que 0")
        except:
            print("Introduzca una cantidad válida")
        input("Pulse enter para continuar")

def introducir_interes():
    while True:
        limpiar_pantalla()
        entrada = input("Introduzca el tipo de interés anual: ")
        try:
            interes = float(entrada)
            return interes
        except:
            print("Introduzca un tipo de interés válido")
        input("Pulse enter para continuar")

def introducir_tiempo():
    while True:
        limpiar_pantalla()
        entrada = input("Introduzca la duración de la inversión en años: ")
        try:
            years = int(entrada)
            if years > 0:
                return years
            else:
                print("La duración debe ser superior a 1 año")
        except:
            print("Introduzca una duración válida")
        input("Pulse enter para continuar")

def introducir_veces():
    while True:
        limpiar_pantalla()
        entrada = input("¿Cuántas veces se acumula el interés en el año?: ")
        try:
            veces = int(entrada)
            if veces > 0:
                return veces
            else:
                print("Se debe introducir una cantidad mayor que 1")
        except:
            print("Introduzca una cantidad de veces válida")
        input("Pulse enter para continuar")       

def imprimir_menu():
    limpiar_pantalla()
    print("1 - Calcular rentabilidad dado el plazo")
    print("2 - Calcular el plazo dada la cantidad deseada")
    print("0 - Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Hasta luego lucas")
        exit()
    elif opcion == "1":
        return "cantidad"
    elif opcion == "2":
        return "plazo"
    else:
        print("Introduzca una opción válida")
        input("Pulse enter para continuar")

while True:
    limpiar_pantalla()
    opcion = imprimir_menu()

    if opcion =="cantidad":
        inversion=introducir_cantidad("invertida")
        interes=introducir_interes()
        years=introducir_tiempo()
        veces=introducir_veces()
        factor = (1 + interes / 100 / veces) ** (veces * years)
        total = inversion * factor        
        total = "{:.2f}".format(total)
        print(f"{inversion}€ invertidos al {interes}% durante {years} años con {veces} periodos de imposición por año se transforman en {total}€")
        input("Pulse enter para continuar")

    if opcion == "plazo":
        final=introducir_cantidad("deseada")
        interes=introducir_interes()
        years=introducir_tiempo()
        veces=introducir_veces()
        factor = (1 + interes / 100 / veces) ** (veces * years)
        inversion = final / factor
        inversion = "{:.2f}".format(inversion)
        print(f"Para obtener {final}€ invirtiendo al {interes}% durante {years} años con {veces} periodos de imposición por año se debe invertir la cantidad de {inversion}€")
        input("Pulse enter para continuar")