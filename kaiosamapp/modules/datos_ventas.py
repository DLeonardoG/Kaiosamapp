import json
#from modules.funciones_secundarias import tipo_,line,print_,clear_screen,_fecha_
#from modules.datos_ventas import contador_id


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

#datos = cargar_datos(RUTA_BASE_DE_DATOS_VENTAS)

#def create_venta(datos):
#    datos = dict(datos)
#    venta={}
#    venta["code"] = "0007"
#    id = contador_id()
#    venta["id"] = id
#    line()
#    venta["tipo_venta"]= 
#    line()
#    venta["referencia"]=
#    venta["precio"]= 
#    venta["nombre"]= 
#    venta["documento"]= 
#    venta["fecha"]= 
#    line()
#    venta["fecha"]= _fecha_
#    venta["repuesta"] = ""
#    datos["venta"].append(venta)
#    clear_screen()
#    line()
#    print_( "La venta ha sido sido recibida con el id ", venta["id"])
#    print_( "con este podra hacerle seguimiento a la venta")      
#    line()
#    return datos

