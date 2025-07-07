from os import system

PROVINCIAS = {
    "A":  {"provincia": "Alicante",                 "impuesto": 0},
    "AB": {"provincia": "Albacete",                 "impuesto": 0},
    "AL": {"provincia": "Almería",                  "impuesto": 0},
    "AV": {"provincia": "Ávila",                    "impuesto": 0},
    "B":  {"provincia": "Barcelona",                "impuesto": 0},
    "BA": {"provincia": "Badajoz",                  "impuesto": 0},
    "BI": {"provincia": "Bizkaia",                  "impuesto": 0},
    "BU": {"provincia": "Burgos",                   "impuesto": 0},
    "C":  {"provincia": "A Coruña",                 "impuesto": 0},
    "CA": {"provincia": "Cádiz",                    "impuesto": 0},
    "CC": {"provincia": "Cáceres",                  "impuesto": 0},
    "CE": {"provincia": "Ceuta",                    "impuesto": 0},
    "CO": {"provincia": "Córdoba",                  "impuesto": 0},
    "CR": {"provincia": "Ciudad Real",              "impuesto": 0},
    "CS": {"provincia": "Castellón",                "impuesto": 0},
    "CU": {"provincia": "Cuenca",                   "impuesto": 0},
    "GC": {"provincia": "Las Palmas",               "impuesto": 0},
    "GI": {"provincia": "Girona",                   "impuesto": 0},
    "GR": {"provincia": "Granada",                  "impuesto": 0},
    "GU": {"provincia": "Guadalajara",              "impuesto": 0},
    "H":  {"provincia": "Huelva",                   "impuesto": 0},
    "HU": {"provincia": "Huesca",                   "impuesto": 0},
    "J":  {"provincia": "Jaén",                     "impuesto": 0},
    "L":  {"provincia": "Lleida",                   "impuesto": 0},
    "LE": {"provincia": "León",                     "impuesto": 0},
    "LO": {"provincia": "La Rioja",                 "impuesto": 0},
    "LU": {"provincia": "Lugo",                     "impuesto": 0},
    "M":  {"provincia": "Madrid",                   "impuesto": 0},
    "MA": {"provincia": "Málaga",                   "impuesto": 0},
    "ML": {"provincia": "Melilla",                  "impuesto": 0},
    "MU": {"provincia": "Murcia",                   "impuesto": 0},
    "NA": {"provincia": "Navarra",                  "impuesto": 0},
    "O":  {"provincia": "Asturias",                 "impuesto": 0},
    "OR": {"provincia": "Ourense",                  "impuesto": 0},
    "P":  {"provincia": "Palencia",                 "impuesto": 0},
    "PM": {"provincia": "Illes Balears",            "impuesto": 0},
    "PO": {"provincia": "Pontevedra",               "impuesto": 0},
    "S":  {"provincia": "Cantabria",                "impuesto": 0},
    "SA": {"provincia": "Salamanca",                "impuesto": 0},
    "SE": {"provincia": "Sevilla",                  "impuesto": 0},
    "SG": {"provincia": "Segovia",                  "impuesto": 0},
    "SO": {"provincia": "Soria",                    "impuesto": 0},
    "SS": {"provincia": "Gipuzkoa",                 "impuesto": 0},
    "T":  {"provincia": "Tarragona",                "impuesto": 0},
    "TE": {"provincia": "Teruel",                   "impuesto": 0},
    "TF": {"provincia": "Santa Cruz de Tenerife",   "impuesto": 0},
    "TO": {"provincia": "Toledo",                   "impuesto": 0},
    "V":  {"provincia": "Valencia",                 "impuesto": 5.5},
    "VA": {"provincia": "Valladolid",               "impuesto": 0},
    "VI": {"provincia": "Álava",                    "impuesto": 0},
    "Z":  {"provincia": "Zaragoza",                 "impuesto": 0},
    "ZA": {"provincia": "Zamora",                   "impuesto": 0}
}

def pausa():
    input("Pulse enter para continuar")

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

def imprimir_menu():
    while True:
        limpiar_pantalla()
        print("1 - Buscar provincia")
        print("2 - Introducir iniciales de provincia")
        print("0 - Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("Hasta luego lucas")
            exit()
        elif opcion == "1":
            return "buscar"
        elif opcion == "2":
            return "iniciales"
        else:
            impripausa("Introduzca una opción válida")

def introduce(dato, letras=15):
    while True:
        limpiar_pantalla()
        entrada = input(f"Introduzca {dato}: ")
        if len(entrada) > letras:
            impripausa (f"{dato.capitalize()} debe tener {letras} letras como máximo")
        else:
            return entrada
 
def buscar_por_iniciales():
    iniciales = introduce("iniciales de provincia",2).upper()
    try:
        provincia = PROVINCIAS[iniciales]["provincia"]
        impuesto = PROVINCIAS[iniciales]["impuesto"]
        return provincia,impuesto
    except:
        return None, None
    
def buscar_por_provincia():
    cadena = introduce("nombre de provincia").lower()
    for item in PROVINCIAS.values():
        if cadena in item["provincia"].lower():
            provincia = item["provincia"]
            impuesto = item["impuesto"]
            return provincia,impuesto
    else:
        return None, None

def introdu_importe():
    while True:
        limpiar_pantalla()
        cadena = input(f"Introduce el importe: ")
        try:
            importe = float(cadena)
            if importe < 0:
                impripausa("El importe no puede ser negativo")
            else:
                return round(importe,2)
        except:
            impripausa("Introduce un importe válido")

while True:
    opcion = imprimir_menu()
    if opcion == "buscar":
        provincia,impuesto = buscar_por_provincia()
    if opcion == "iniciales":
        provincia,impuesto = buscar_por_iniciales()
    if not provincia:
        impripausa(f"No se ha encontrado la provincia")        
    if provincia:
        importe = introdu_importe()
        if impuesto > 0:
            impripausa(f"Para la provincia {provincia} el impuesto es {impuesto}%\n"
                f"El subtotal es de {importe:.2f}€\n"
                f"La tasa es {importe * impuesto / 100:.2f}€\n"
                f"El total es {importe + importe * (impuesto / 100):.2f}€")
        if impuesto == 0:
            impripausa(f"Para la provincia {provincia} el impuesto es {impuesto}%\n"
                f"El total es de {importe:.2f}€")
