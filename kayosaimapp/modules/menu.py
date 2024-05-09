import platform
import os
from datetime import datetime



def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha

time = time_now()

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    


NAME = "Kaiosamapp"
def main_1():
    clear_screen()
    print("***************************************")
    print ("Bienvenido a",NAME)
    print ("1. Usuario")
    print ("2. Administrador")
    print ("0. Salir")
    print("***************************************")

def pedir_opcion():
    op = 0
    while True:
        try:
            op = int(input("Escoja una opcion: "))
            print("***************************************")
            if op == 1 or op == 2 or op == 0:
                clear_screen()
                break
            else:
                clear_screen()
                main_1()
                print("Valor inválido")
                print("***************************************")
            
        except Exception:
            clear_screen()
            main_1()
            print("Valor inválido")
            print("***************************************")
            
    return op
            
            
def validar_password():
    while True:
        password = input("Ingrese la contraseña admin: ")
        if password == "password":
            validar = 1
            print("Puedes pasar guerrero Z")
            break
        elif password == "0":
            validar = 0
            break
        elif password != "password":
            clear_screen()
            print("Contraseña incorrecta")
            print("Si no eres admin oprime 0")
            print("***************************************")
            
    return validar


def asignacion(op):
    if op == 1:
        print ("Usuario puedes pasar a", NAME)
        print("Si no eres user oprime 0")
        op = 1
    elif op == 2:
        validar = validar_password() 
        clear_screen()
        if validar == 0:
            print("Adios guerrero Z")
            op = 0
        else:
            print ("Admin puedes pasar a", NAME)
            op = 2
    elif op == 0:
        print("Adios guerrero Z")
        op = 0
    
main_1()
op = pedir_opcion()
asignacion(op)


    

    
