#imports
from datos import *
from menu import *
from participantes import *
from eventos import *


#Constants
RUTA_BASE_DE_DATOS ="Python/eventos.json"

datos = cargar_datos(RUTA_BASE_DE_DATOS)

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        datos = registrar_participante(datos)
    elif opc == 2:
        datos = eliminar_participante(datos)
    elif opc == 3:
        datos = pagar_participante(datos)
    elif opc == 4:
        registrar_evento(datos)
    elif opc == 5:
        eliminar_evento(datos)
    elif opc == 6:
        asignacion_evento(datos)
    elif opc == 7:
        cuales_participantes_sin_pagar(datos)
    elif opc == 8:
        cuantos_participantes_sin_pagar(datos)
    elif opc == 9:
        print("opcion 9")
    elif opc == 10:
        participantes_del_mes(datos)
    elif opc == 11:
        print("Salió!!")
        break

guardar_datos(datos, RUTA_BASE_DE_DATOS)