from os import system

def limpiar_pantalla():
    system("clear||cls")

def introducir_cantidad():
    while True:
        limpiar_pantalla()
        entrada = input("Introduzca la cantidad invertida: ")
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
        entrada = input("Introduzca el tipo de interés: ")
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

       

aportacion=introducir_cantidad()
interes=introducir_interes()
years=introducir_tiempo()

for i in range(1,years+1):
    beneficio = interes/100*aportacion*i
    total = "{:.2f}".format(aportacion + beneficio)
    print(f"Tras {i} {"año" if i == 1 else "años"} de inversión al {interes}%, su cantidad debe ser {total}€")
