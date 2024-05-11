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
        
def menu_txt(archivo)
    with open(nombre_archivo, 'r') as archivo:
    menu = archivo.read()
    print(menu)

archivo = "kaiosamapp/txt/menus_plantillas/principal"
menu_txt(archivo)
        
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
    
    
def diseño_logo():
    print ("     **************************************")
    print('''\033[1;33m

 __    __   ______   ______   ______    ______    ______   __       __   ______   _______   _______  
|  \  /  \ /      \ |      \ /      \  /      \  /      \ |  \     /  \ /      \ |       \ |       \ 
| $$ /  $$|  $$$$$$\ \$$$$$$|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$\   /  $$|  $$$$$$\| $$$$$$$\| $$$$$$$\
| $$/  $$ | $$__| $$  | $$  | $$  | $$| $$___\$$| $$__| $$| $$$\ /  $$$| $$__| $$| $$__/ $$| $$__/ $$
| $$  $$  | $$    $$  | $$  | $$  | $$ \$$    \ | $$    $$| $$$$\  $$$$| $$    $$| $$    $$| $$    $$
| $$$$$\  | $$$$$$$$  | $$  | $$  | $$ _\$$$$$$\| $$$$$$$$| $$\$$ $$ $$| $$$$$$$$| $$$$$$$ | $$$$$$$ 
| $$ \$$\ | $$  | $$ _| $$_ | $$__/ $$|  \__| $$| $$  | $$| $$ \$$$| $$| $$  | $$| $$      | $$      
| $$  \$$\| $$  | $$|   $$ \ \$$    $$ \$$    $$| $$  | $$| $$  \$ | $$| $$  | $$| $$      | $$      
 \$$   \$$ \$$   \$$ \$$$$$$  \$$$$$$   \$$$$$$  \$$   \$$ \$$      \$$ \$$   \$$ \$$       \$$      
                                                                                                     
                                                                                                     
                                                                                                     
            
    \033[0m''')
    print ("     ***************************************")
        


#ef dragon_ball():


