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
print("***************************************")
print ("Bienvenido a",NAME,"escoje una opcion: ")
print ("1. Usuario")
print ("2. Administrador")
print("***************************************")

def pedir_opcion():
    op = 0
    while True:
        try:
            op = int(input("Ingrese su cargo: "))
            print("***************************************")
            if op == 1 or op == 2:
                clear_screen()
                break
            
        except Exception:
            print("Valor inválido")
            print("***************************************")
    return op
            
        
op = pedir_opcion()

if op == 1:
    print ("Bienvenido usuario a", NAME)
else:
    print ("Bienvenido admin a", NAME)
