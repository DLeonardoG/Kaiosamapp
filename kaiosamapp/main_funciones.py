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




def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')



def diseño_logo():
    print ("********************************************************************************************************************")
    print('''\033[1;33m
         /$$   /$$  /$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$  /$$$$$$  /$$$$$$$  /$$$$$$$ 
        | $$  /$$/ /$$__  $$|_  $$_/ /$$__  $$ /$$__  $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$__  $$| $$__  $$
        | $$ /$$/ | $$  \ $$  | $$  | $$  \ $$| $$  \__/| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$  \ $$| $$  \ $$
        | $$$$$/  | $$$$$$$$  | $$  | $$  | $$|  $$$$$$ | $$$$$$$$| $$ $$/$$ $$| $$$$$$$$| $$$$$$$/| $$$$$$$/
        | $$  $$  | $$__  $$  | $$  | $$  | $$ \____  $$| $$__  $$| $$  $$$| $$| $$__  $$| $$____/ | $$____/ 
        | $$\  $$ | $$  | $$  | $$  | $$  | $$ /$$  \ $$| $$  | $$| $$\  $ | $$| $$  | $$| $$      | $$      
        | $$ \  $$| $$  | $$ /$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$| $$ \/  | $$| $$  | $$| $$      | $$      
        |__/  \__/|__/  |__/|______/ \______/  \______/ |__/  |__/|__/     |__/|__/  |__/|__/      |__/      
  \033[0m''')
    print ("*********************************************************************************************************************")

#diseño_logo()
     
def diseño_base():
    print ("     **************************************")
    print('''\033[1;33m
      /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$ 
     /$$__  $$| $$__  $$| $$  | $$| $$__  $$
    | $$  \__/| $$  \ $$| $$  | $$| $$  \ $$
    | $$      | $$$$$$$/| $$  | $$| $$  | $$
    | $$      | $$__  $$| $$  | $$| $$  | $$
    | $$    $$| $$  \ $$| $$  | $$| $$  | $$
    |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/
     \______/ |__/  |__/ \______/ |_______/                 
    \033[0m''')
    print ("     ***************************************")

#diseño_base()

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)