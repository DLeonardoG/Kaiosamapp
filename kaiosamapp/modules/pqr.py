from modules.datos_pqr import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very,_fecha_
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
    pqr["fecha"]= _fecha_
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
        


def consult_pqr(datos):
    datos = dict(datos)
    id =input("Ingrese el id del PQR: ")
    for i in range(len(datos["pqr"])):
        if datos["pqr"][i]["id"] == id:
            max_length = max(len(datos["pqr"][i]["tipo_pqr"] + " " + datos["pqr"][i]["motivo"]) for i in range(len(datos["pqr"])))
            print("----------------------------------------------------------------------------")
            print(datos["pqr"][i]["tipo_pqr"]).title().rjust(max_length)
            print("----------------------------------------------------------------------------")
            print(datos["pqr"][i]["id"].rjust(max_length), "  -  id")
            print(datos["pqr"][i]["motivo"].rjust(max_length), "  -  motivo")
            print(datos["pqr"][i]["comentario"].rjust(max_length), "  -  comentario")
            print(datos["pqr"][i]["fecha"].rjust(max_length), "  -  fecha")
            print(datos["pqr"][i]["repuesta"].rjust(max_length), "  -  repuesta")
            print("----------------------------------------------------------------------------")
            return datos
    print("PQR no existente...")
    return datos

def consultar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_PQR)
        datos = consult_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_PQR)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()