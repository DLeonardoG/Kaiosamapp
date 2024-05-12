from datos_catalogo import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very

def registrar_servicio(datos):
    datos = dict(datos)
    catalogo_servicios={}
    catalogo_servicios["code"] = "0001"
    try:
        catalogo_servicios["id"]=input("Ingrese el id: ")
        for i in range(len(datos["catalogo_servicios"])):
            if datos["catalogo_servicios"][i]["id"] == catalogo_servicios["id"]:
                print (datos["catalogo_servicios"][i]["id"],"ya se encuentra registrado!")
                return datos
    except Exception as e:
        reportar_error_a_txt(e)
        catalogo_servicios["id"] = ""
    catalogo_servicios["tipo_servicios"]=input("Ingrese el tipo de servicio: ")
    catalogo_servicios["referencia"]=input("Ingrese la referencia: ")
    catalogo_servicios["plan"]=input("Ingrese el plan: ")
    catalogo_servicios["precio"]=input("Ingrese el precio: ")
    catalogo_servicios["duracion"]=input("Ingrese la duracion: ")
    catalogo_servicios["descripcion"]=input("Ingrese la descripcion: ")
    catalogo_servicios["descuento"]=[]
    descuento = {}
    descuento["nuevo"]=input("Ingrese el descuento para usuarios nuevos: ")
    descuento["regular"]=input("Ingrese el descuento para usuarios regulares: ")
    descuento["leal"]=input("Ingrese el descuento para usuarios leales: ")
    
    
    
    catalogo_servicios["descuento"]=input("Ingrese el descuento: ")
    catalogo_servicios["descuento"]=input("Ingrese el descuento: ")
    datos["catalogo_servicios"].append(catalogo_servicios)
    print( catalogo_servicios["referencia"],catalogo_servicios["plan"],"registrado con éxito!")
    return datos
    
def crear_servicio():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = registrar_servicio(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        break

def eliminar_service():
    
    

