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
    print("----------------------------------------------------------------")
    tipo_pqr(pqr)
    print("----------------------------------------------------------------")
    pqr["motivo"]=input("                   Ingrese el motivo: ")
    pqr["comentario"]=input("                   Ingrese el comentario: ")
    print("----------------------------------------------------------------")
    pqr["fecha"]= _fecha_
    pqr["repuesta"] = ""

    datos["pqr"].append(pqr)
    clear_screen()
    print("----------------------------------------------------------------------------------------")
    print( "           La solicitud ha sido sido recibida bajo el numero ", pqr["id"],"\ncon este podra hacerle seguimiento a su solicitud")
    print("----------------------------------------------------------------------------------------")
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
    print("----------------------------------------------------------------------------")
    id =input("                       Ingrese el numero del PQR: ")
    print("----------------------------------------------------------------------------")
    clear_screen()
    for i in range(len(datos["pqr"])):
        if datos["pqr"][i]["id"] == id:
            max_length = max(len(datos["pqr"][i]["tipo_pqr"] + " " + datos["pqr"][i]["motivo"]) for i in range(len(datos["pqr"])))
            print("----------------------------------------------------------------------------")
            print(((datos["pqr"][i]["tipo_pqr"]).title()).rjust(max_length), "  -   Tipo de PQR")
            print("----------------------------------------------------------------------------")
            print(datos["pqr"][i]["id"].rjust(max_length), "  -   Id")
            print(datos["pqr"][i]["motivo"].rjust(max_length), "  -   Motivo")
            print(datos["pqr"][i]["comentario"].rjust(max_length), "  -   Comentario")
            print(datos["pqr"][i]["fecha"].rjust(max_length), "  -   Fecha")
            print(datos["pqr"][i]["repuesta"].rjust(max_length), "  -   Repuesta")
            print("----------------------------------------------------------------------------")
            return datos
    clear_screen()
    print("----------------------------------------------------------------------------")    
    print("                        PQR",id,"no existente...")
    print("----------------------------------------------------------------------------")
    return datos

def consultar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_PQR)
        datos = consult_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_PQR)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def eliminate_pqr(datos):
    datos = dict(datos)
    print("----------------------------------------------------------------------------")
    id =input("                   Ingrese el numero de PQR 💀: ")
    print("----------------------------------------------------------------------------")
    for i in range(len(datos["pqr"])):
        if datos["pqr"][i]["id"] == id:
            plan = (datos["pqr"][i]["tipo_pqr"]," - ",datos["pqr"][i]["motivo"])
            datos["pqr"].pop(i)
            separador = " "
            plan = separador.join(map(str, plan))
            print("----------------------------------------------------------------------------")
            print(                       plan," - eliminado...")
            print("----------------------------------------------------------------------------")
            return datos
    clear_screen()
    print("----------------------------------------------------------------------------")    
    print("                          ",id,"no existe...")    
    print("----------------------------------------------------------------------------")
    return datos

def eliminar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_PQR)
        datos = eliminate_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_PQR)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        