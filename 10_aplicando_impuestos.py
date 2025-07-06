from tabulate import tabulate

TAX = 5.5

def introdu_nombre(articulo):
    cadena = input(f"Introduce el nombre del artículo {articulo}: ")
    return cadena

def introdu_precio(articulo):
    while True:
        cadena = input(f"Introduce el precio del artículo {articulo}: ")
        try:
            precio = float(cadena)
            if precio < 0:
                print("El precio no puede ser negativo")
            else:
                return precio
        except:
            print("Introduce un precio válido")

def introdu_cantidad(articulo):
    while True:
        cadena = input(f"Introduce la cantidad del artículo {articulo}: ")
        try:
            cantidad = int(cadena)
            if cantidad < 0:
                print("La cantidad no puede ser negativa")
            elif cantidad == 0:
                print("La cantidad no puede ser 0")
            else:
                return cantidad
        except:
            print("Introduce una cantidad entera")

def menu_seguir():
    while True:
        entrada = input("¿Desea introducir otro artículo? Responda s o n: ")
        if entrada == "n":
            return False
        elif entrada == "s" or entrada == "y":
            return True
        else:
            print("Opción incorrecta")

articulos = []
seguir = True
articulo = 1
while seguir:
    nombre = introdu_nombre(articulo)
    cantidad = introdu_cantidad(articulo)
    precio = round(introdu_precio(articulo),2)
    impuesto = round((precio * TAX/100),2)
    articulos.append({"Nombre": nombre, "Cantidad": cantidad, "Precio": precio, "Impuesto": impuesto})
    seguir = menu_seguir()
    articulo += 1
albaran=[]
subtotal = 0
total = 0
for articulo in articulos:
    subtotallinea = (articulo["Cantidad"]*articulo["Precio"])
    totallinea = articulo["Cantidad"]*(articulo["Precio"]+articulo["Impuesto"])
    albaran.append({"Nombre": (articulo["Nombre"].capitalize()), "Cantidad": articulo["Cantidad"], "Precio": articulo["Precio"], "Impuesto": articulo["Impuesto"], "Subtotal": subtotallinea, "Total": totallinea})
    subtotal += subtotallinea
    total += totallinea
albaran.append({"Nombre": "Total", "Subtotal": subtotal, "Total": total})
print (tabulate(albaran,headers="keys"))
print ("Gracias por su compra")