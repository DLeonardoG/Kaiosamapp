import os
import platform
from datetime import datetime

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

def very():
    while True:
        continuar = input("""------------------------------------       
        ¿Repetir operacion?
            1 .Si
            2 .No
------------------------------------
        ��  """)
        if continuar == "1": return "1"
        elif continuar == "2": return "2"
        else: opcion_no_valida()