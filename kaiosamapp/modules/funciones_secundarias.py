import platform
import os
from datetime import datetime

ARCHIVO = "errores.txt"

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

def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')
        


#ef dragon_ball():

