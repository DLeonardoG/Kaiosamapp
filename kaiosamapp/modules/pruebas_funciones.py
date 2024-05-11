from datetime import datetime
from funciones_secundarias import *

fecha_y_hora = datetime.now()
fecha_y_hora = fecha_y_hora.replace(microsecond=0)
print(fecha)

def reportar_error_a_txt(excepcion):
    ruta_errores = os.path.join("kayosaimapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: {excepcion}" 
        f.write(mensaje_error + '\n')

