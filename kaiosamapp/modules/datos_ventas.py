import json
from modules.venta_funciones import id_valido,tipo_,contador_id



def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    

#Constants
RUTA_BASE_DE_DATOS_VENTAS ="kaiosamapp/modules/datos_ventas.py"

datos = cargar_datos(RUTA_BASE_DE_DATOS_VENTAS)

def create_venta(datos):
    datos = dict(datos)
    venta={}
    venta["code"] = "0007"
    id = contador_id()
    venta["id"] = id
    line()
    tipo_(venta)
    line()
    venta["motivo"]=input("Ingrese el motivo: ")
    venta["comentario"]=input("Ingrese el comentario: ")
    line()
    venta["fecha"]= _fecha_
    venta["repuesta"] = ""

    datos["venta"].append(venta)
    clear_screen()
    line()
    print( "           La solicitud ha sido sido recibida bajo el numero ", venta["id"],"\ncon este podra hacerle seguimiento a su solicitud")
    line()
    return datos

