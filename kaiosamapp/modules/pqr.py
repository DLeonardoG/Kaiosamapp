from modules.datos_pqr import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very,fecha
from modules.pqr_funciones import id_valido,tipo_pqr,contador_id

def create_pqr(datos):
    datos = dict(datos)
    pqr={}
    pqr["code"] = "0003"
    id = contador_id()
    pqr["id"] = id
    tipo_pqr(pqr)
    pqr["motivo"]=input("Ingrese el motivo: ")
    pqr["comentario"]=input("Ingrese el comentario: ")
    pqr["fecha"]= fecha
    pqr["repuesta"] = ""

    datos["pqr"].append(pqr)
    print( "El id de PQR es ", pqr["id"],"PQR registrada con exito!")
    return datos

def registrar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_PQR)
        datos = create_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_PQR)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        






def consultar_pqr(datos):
    try:
        pqr["id"]=id_valido(pqr)
        for i in range(len(datos["pqr"])):
            if datos["pqr"][i]["id"] == pqr["id"]:
                print (datos["pqr"][i]["id"],"ya se encuentra registrado!")
                return datos
    except Exception as e:
        reportar_error_a_txt(e)
        pqr["id"] = ""