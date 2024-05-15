from datos import *
from funciones_secundarias import reportar_error_a_txt,opcion_no_valida,line
from funciones_secundarias import clear_screen,very,_fecha_,print_
from pqr_funciones import id_valido,tipo_pqr,contador_id

def create_pqr(datos):
    datos = dict(datos)
    pqr={}
    pqr["code"] = "0003"
    id = contador_id()
    pqr["id"] = id
    line()
    tipo_pqr(pqr)
    line()
    pqr["motivo"]=input("Ingrese el motivo: ")
    pqr["comentario"]=input("Ingrese el comentario: ")
    line()
    pqr["fecha"]= _fecha_
    pqr["repuesta"] = ""

    datos["pqr"].append(pqr)
    clear_screen()
    line()
    print( "           La solicitud ha sido sido recibida bajo el numero ", pqr["id"],"\ncon este podra hacerle seguimiento a su solicitud")
    line()
    return datos

def registrar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = create_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        


def consult_pqr(datos):
    datos = dict(datos)
    line()
    id =input("                       Ingrese el numero del PQR: ")
    line()
    clear_screen()
    for i in range(len(datos["pqr"])):
        if datos["pqr"][i]["id"] == id:
            line()
            print_("Tipo de PQR")
            print_(datos["pqr"][i]["tipo_pqr"])
            line()
            print_("Id")
            print_(datos["pqr"][i]["id"])
            line()
            print_("Motivo de PQR")
            print(datos["pqr"][i]["motivo"])
            line()
            print_("Comentario")
            print(datos["pqr"][i]["comentario"])
            line()
            print_("Fecha")
            print(datos["pqr"][i]["fecha"])
            line()
            print_("Repuesta")
            print(datos["pqr"][i]["repuesta"])
            line()
            return datos
    clear_screen()
    line()    
    print("                        PQR",id,"no existente...")
    line()
    return datos

def consultar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = consult_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def eliminate_pqr(datos):
    datos = dict(datos)
    line()
    id =input("                   Ingrese el numero de PQR 💀: ")
    line()
    for i in range(len(datos["pqr"])):
        if datos["pqr"][i]["id"] == id:
            plan = (datos["pqr"][i]["tipo_pqr"]," - ",datos["pqr"][i]["motivo"])
            datos["pqr"].pop(i)
            separador = " "
            plan = separador.join(map(str, plan))
            line()
            print(                       plan," - eliminado...")
            line()
            return datos
    clear_screen()
    line()    
    print("                          ",id,"no existe...")    
    line()
    return datos

def eliminar_pqr():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = eliminate_pqr(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        