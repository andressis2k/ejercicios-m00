import math
# Cuántos m2 se pueden pintar con un bote de 5 litros de pintura
RENDIMIENTO = 100

def introduce(medida):
    while True:
        entrada = input(f"Introduce el {medida} de la habitación ")
        if entrada == "0":
            exit()
        try:
            if float(entrada)>0:
                return float(entrada)
            else:
                print("La medida debe ser positiva")
        except:
            print("Introduce un número")

while True:
    ancho = introduce("ancho")
    largo = introduce("largo")
    superficie = largo * ancho
    litros = superficie * 5 / RENDIMIENTO
    botes = math.ceil(superficie / RENDIMIENTO)
    print(f"Necesitarás {litros} litros para pintar {superficie} metros cuadrados de techo")
    print(f"Tendrás que comprar {botes} botes de pintura")