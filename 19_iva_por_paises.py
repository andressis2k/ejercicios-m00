from os import system
import unicodedata

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def limpiar_pantalla():
    system("clear||cls")

IMPUESTOS = {
    "Hungria": 27,
    "Croacia": 25,
    "Dinamarca": 25,
    "Suecia": 25,
    "Finlandia": 24,
    "Rumaía": 24,
    "Grecia": 23,
    "Irlanda": 23,
    "Polonia": 23,
    "Portugal": 23,
    "Eslovenia": 22,
    "Italia": 22,
    "España": 21,
    "Bélgica": 21,
    "Letonia": 21,
    "Lituania": 21,
    "Paises Bajos": 21,
    "República Checa": 21,
    "Austria": 20,
    "Bulgaria": 20,
    "Eslovaquia": 20,
    "Estonia": 20,
    "Francia": 20,
    "Reino Unido": 20,
    "Alemania": 19,
    "Chipre": 19,
    "Malta": 18,
    "Luxemburgo": 15
}

def pausa():
    input("Pulse enter para continuar")

def buscar_pais():
    while True:
        limpiar_pantalla()
        cadena = input("Introduzca un país (enter para salir): ")
        if cadena == "":
            print("Hasta luego lucas")
            exit()
        seleccion = ""
        for pais in IMPUESTOS.keys():
            if elimina_tildes(cadena.lower()) in elimina_tildes(pais.lower()):
                seleccion = pais
        if seleccion == "":
            print("No se ha encontrado el país")
            pausa()
        else:
            return seleccion
        
def introduce_importe():
    while True:
        limpiar_pantalla()
        entrada = input("Introduzca el importe: ")
        try:
            importe = float(entrada)
            if importe > 0:
                return round(importe,2)
            else:
                print("El importe debe ser mayor que 0")
        except:
            print("Introduzca un importe válido")
        pausa()

def redondeo(cantidad):
    if cantidad == int(cantidad):
        return int(cantidad)
    else:
        return round(cantidad,2
                     )

while True:
    pais = buscar_pais()
    importe = redondeo(introduce_importe())
    iva = IMPUESTOS[pais]
    importeiva = redondeo(importe * iva / 100)
    preciofinal = redondeo(importe + importeiva)
    limpiar_pantalla()
    print (f"El IVA en {pais} es del {iva}%\nPara {importe}€ el IVA son {importeiva}€, por lo que el precio final será {preciofinal}€")
    pausa()