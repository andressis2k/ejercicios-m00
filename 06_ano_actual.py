from datetime import date,datetime

edad = int(input("¿Cuántos años tienes?: "))
jubilacion = int(input("¿A qué edad te jubilarás?: "))
fecha_actual = datetime.now()
year = fecha_actual.year
if jubilacion == edad:
    print (f"¡Enhorabuena! Te jubilas en este año {year},")
if jubilacion > edad:
    print (f"Te quedan {jubilacion-edad} años para jubilarte")
    print (f"Estamos en {year}, por lo que te jubilarás en {year+jubilacion-edad}")
if edad > jubilacion:
    print (f"Podrías haberte jubilado hace {edad-jubilacion} años, en el {year-edad+jubilacion}. Anda y tira para el SEPE...")
