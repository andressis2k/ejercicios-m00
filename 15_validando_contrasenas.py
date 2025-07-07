import hashlib
from os import system
import getpass

def pausa():
    input("Pulse enter para continuar")

def limpiar_pantalla():
    system("clear||cls")

def impripausa(cadena):
    print(cadena)
    input("Pulse enter para continuar")

usuarios={}

def alta_usuario():
    while True:
        limpiar_pantalla()
        print("Crear nuevo usuario")
        usuario = input("Introduzca el nombre de usuario: ")
        if usuario in usuarios.keys():
            impripausa(f"El usuario {usuario} ya existe. Escoja un nombre diferente o bórrelo antes")
        else:
            password = getpass.getpass("Introduzca la contraseña: ")
            passmd5 = (hashlib.md5(password.encode())).hexdigest()
            usuarios.update({usuario:passmd5})
            return

def login_usuario():
    limpiar_pantalla()
    usuario = input("Introduzca el nombre de usuario: ")
    password = getpass.getpass("Introduzca la contraseña: ")
    passmd5 = (hashlib.md5(password.encode())).hexdigest()
    if passmd5 == usuarios.get(usuario):
        impripausa(f"Entró al sistema como el usuario {usuario}")
    else:
        impripausa("No te conozco, no pasas")

def borrar_usuario():
    limpiar_pantalla()
    usuario = input("Introduzca el nombre de usuario que desea borrar: ")
    try:
        usuarios.pop(usuario)
        impripausa(f"Se ha borrado el usuario {usuario}")
    except KeyError:
        impripausa(f"No se ha encontrado el usuario {usuario}")
    return

def imprimir_menu():
    while True:
        limpiar_pantalla()
        print("Bienvenido al sistema de gestión de usuarios")
        print("1 - Añadir usuario")
        print("2 - Eliminar usuario")
        print("3 - Acceder al sistema")
        print("0 - Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            return 1
        elif opcion == "2":
            return 2
        elif opcion == "3":
            return 3
        elif opcion == "0":
            exit()
        else:
            impripausa("Escoja una opción válida")

while True:
    opcion = imprimir_menu()
    if opcion == 1:
        alta_usuario()
    if opcion == 2:
        borrar_usuario()
    if opcion == 3:
        login_usuario()
