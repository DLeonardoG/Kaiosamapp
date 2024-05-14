import os
import platform
from datetime import datetime
import shutil

def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha
fecha = time_now()
print (fecha)
def datetime_to_json(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')
_fecha_ = datetime_to_json(fecha)

def clear_screen():
    if platform.system() == 'Windows': os.system('cls')
    else: os.system('clear')

ARCHIVO = "errores.txt"
def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')

#def doc_existe(usuarios,datos): 
def opcion_no_valida():
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: Opcion de menu no valida" 
        f.write(mensaje_error + '\n')
#opcion_no_valida()

        


def print_(*args, **kwargs):
    ancho_consola = shutil.get_terminal_size().columns
    texto = ' '.join(map(str, args))
    ancho_espacios = kwargs.get('ancho_espacios', 1)
    espacio_blancos = (ancho_consola - len(texto)) // 2
    print(' ' * espacio_blancos + texto.center(ancho_consola - 2 * espacio_blancos))

def line():
    ancho_consola = shutil.get_terminal_size().columns
    return print("-" * ancho_consola)

def linen():
    ancho_consola = shutil.get_terminal_size().columns
    return print("." * ancho_consola)

def very():
    while True:
        linen()
        print_("¿Repetir operacion?")
        print_("1 .Si")
        print_("2 .No")
        continuar = input("                     >>>")
        linen()
        if continuar == "1": return "1"
        elif continuar == "2": 
            clear_screen()
            return "2"
        else: opcion_no_valida()