import os
import platform
from datetime import datetime



    
def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha

fecha = time_now()

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
ARCHIVO = "errores.txt"
def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')



def opcion_no_valida():
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: Opcion de menu no valida" 
        f.write(mensaje_error + '\n')
#opcion_no_valida()


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
        
def very():
    while True:
        continuar = input("Desea continuar?\n1 . S i\n2 . N o\n��  ")
        if continuar == "1": 
            return True
        elif continuar == "2":
            return False
        else:
            opcion_no_valida()
#v = very()
#print(v) 