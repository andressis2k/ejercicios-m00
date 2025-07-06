from os import system

def limpiar_pantalla():
    system("clear||cls")
    
meses = {
    1: {"es": "enero",      "en": "January",   "fr": "janvier"},
    2: {"es": "febrero",    "en": "February",  "fr": "février"},
    3: {"es": "marzo",      "en": "March",     "fr": "mars"},
    4: {"es": "abril",      "en": "April",     "fr": "avril"},
    5: {"es": "mayo",       "en": "May",       "fr": "mai"},
    6: {"es": "junio",      "en": "June",      "fr": "juin"},
    7: {"es": "julio",      "en": "July",      "fr": "juillet"},
    8: {"es": "agosto",     "en": "August",    "fr": "août"},
    9: {"es": "septiembre", "en": "September", "fr": "septembre"},
    10: {"es": "octubre",   "en": "October",   "fr": "octobre"},
    11: {"es": "noviembre", "en": "November",  "fr": "novembre"},
    12: {"es": "diciembre", "en": "December",  "fr": "décembre"},
}

idiomas = {"es": "español", "en": "inglés", "fr": "francés"}

def elegir_idioma():
    iniciales = list(idiomas.keys())
    while True:
        limpiar_pantalla()
        for index,idioma in enumerate(idiomas.values(),1):
            print(f"{index} - {idioma.capitalize()}")
        cadena = input("Elija un idioma (0 para salir): ")
        if cadena == "0":
            print("Hasta luego Lucas")
            exit()
        try:
            eleccion = int(cadena)
            if eleccion >=0 and eleccion < len(idiomas)+1:
                return iniciales[eleccion-1]
            else:
                print("Idioma no válido")
                input("Pulse enter para continuar")
        except:
            print("Introduzca un número")
            input("Pulse enter para continuar")

def introducir_mes():
    while True:
        limpiar_pantalla()
        cadena = input(f"Introduzca el mes: ")
        try:
            valor = int(cadena)
            if valor > 0 and valor <=12:
                return valor
            else:
                print("Introduzca un mes válido (1-12)")
                input("Pulse enter para continuar")

        except:
            print("Introduzca un número entero")
            input("Pulse enter para continuar")

while True:
    limpiar_pantalla()
    idioma = elegir_idioma()
    mes = introducir_mes()
    print(f"El mes {mes} en {idiomas[idioma]} es {meses[mes][idioma]}")
    input("Pulse enter para continuar")
