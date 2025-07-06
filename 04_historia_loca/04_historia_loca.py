nombre = input("Introduce un nombre: ")
verbo = input("Introduce un verbo: ")
adverbio = input("Introduce un adverbio: ")
adjetivo = input("Introduce un adjetivo: ")

print("1 - Al parque de atracciones")
print("2 - A la playa")
eleccion = input("¿A donde quiéres que vaya nuestro protagonista? ")
if eleccion == "1":
    texto = "{} decidió ir al parque de atracciones y una vez allí empezó a {} {}. De repente, todo el mundo se fue del parque y él se quedó {}"
elif eleccion == "2":
    texto = "{} fue a la playa abarrotada y decidió {} muy {}. La gente pensaba que era muy {} y todos se le quedaron mirando"
else:
    texto = "{} no quiso ir a ningún sitio ese día, por lo que decidió quedarse en casa a {} {}. Muy {} por su parte."

historia = texto.format(nombre, verbo, adverbio, adjetivo)

print(historia)