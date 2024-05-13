from modules.datos_catalogo import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very
from modules.catalogo_servicios_funciones import id_valido,tipo_servicios,int_precio
from modules.catalogo_servicios_funciones import int_nuevo,int_regular,int_leal,int_cantidad_total

def crear_servicie(datos):
    datos = dict(datos)
    catalogo_servicios={}
    catalogo_servicios["code"] = "0001"
    try:
        catalogo_servicios["id"]=id_valido(catalogo_servicios)
        for i in range(len(datos["catalogo_servicios"])):
            if datos["catalogo_servicios"][i]["id"] == catalogo_servicios["id"]:
                print (datos["catalogo_servicios"][i]["id"],"ya se encuentra registrado!")
                return datos
    except Exception as e:
        reportar_error_a_txt(e)
        catalogo_servicios["id"] = ""
    tipo_servicios(catalogo_servicios)
    catalogo_servicios["referencia"]=input("Ingrese la referencia: ")
    catalogo_servicios["plan"]=input("Ingrese el plan: ")
    int_precio(catalogo_servicios)
    catalogo_servicios["duracion"]=input("Ingrese la duracion: ")
    catalogo_servicios["descripcion"]=input("Ingrese la descripcion: ")
    int_cantidad_total(catalogo_servicios)
    catalogo_servicios["cantidad_vendida"]=0
    catalogo_servicios["descuento"]={"nuevo": 0,"regular":0,"leal":0}
    int_nuevo(catalogo_servicios)
    int_regular(catalogo_servicios)
    int_leal(catalogo_servicios)
    
    datos["catalogo_servicios"].append(catalogo_servicios)
    print( catalogo_servicios["referencia"],catalogo_servicios["plan"],"registrado con éxito!")
    return datos
    
def crear_servicio():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = crear_servicie(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def eliminar_service(datos):
    datos = dict(datos)
    id =input("Ingrese el id del servicio: ")
    for i in range(len(datos["catalogo_servicios"])):
        if datos["catalogo_servicios"][i]["id"] == id:
            #plan = (datos["catalogo_servicios"][i]["referencia"],datos["catalogo_servicios"][i]["plan"])
            datos["catalogo_servicios"].pop(i)
            #print(plan,"eliminado...")
            print("Servicio eliminado!")
            return datos
    print("Servicio no existente...")    
    return datos

def eliminar_servicio():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = eliminar_service(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
    
    

