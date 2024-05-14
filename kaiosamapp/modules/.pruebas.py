import json
from datetime import datetime


def time_now():
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    return fecha
fecha = time_now()
print (fecha)
def datetime_to_json(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')
_fecha_ = datetime_to_json(fecha)


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

RUTA_BASE_DE_DATOS_CATALOGO ="kaiosamapp/json/catalogo.json"
RUTA_BASE_DE_DATOS_USERS ="kaiosamapp/json/users.json"
def registrar_servicio(datos):
    datos = dict(datos)
    service={}
    for i in range(len(datos["catalogo_servicios"])):
        id =input("Ingrese el id del Servicio: ")
        if datos["catalogo_servicios"][i]["id"] == id:
            service = datos["catalogo_servicios"][i]
            return service
    print("Servicio no existente...")
    return 

m = registrar_servicio(datos)

datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
datos = registrar_servicio(datos)
guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)

#registrar_servicio(datos)
def asignar_servicio(datos,service):
    documento =input("Ingrese el documento del usuario: ")
    for j in range(len(datos["usuarios"])):
        if datos["usuarios"][j]["documento"] == documento:
            print(datos["usuarios"][j]["nombre"], datos["usuarios"][j]["apellido"])
        for sn in range(len(datos["usuarios"][j]["registro_servicios"])):
            datos["usuarios"][j]["registro_servicios"][sn]["tipo_servicios"] = service["tipo_servicios"]
            datos["usuarios"][j]["registro_servicios"][sn]["referencia"] = service["referencia"] 
            datos["usuarios"][j]["registro_servicios"][sn]["id"] = service["id"]
            datos["usuarios"][j]["registro_servicios"][sn]["fecha"] =  _fecha_
            datos["usuarios"][j]["registro_servicios"][sn]["code"] = service["code"] 
            datos["usuarios"][j]["registro_servicios"][sn]["code_unico"] = service["code_unico"] 
            print ("Compra de " + service["referencia"]+" exitosa" )
            return datos

asignar_servicio(datos,registrar_servicio(datos))

def asigna (datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["eventos"]=[]
            datos["usuarios"][i]["eventos"].append(registrar_servicio(datos))
            print(datos["usuarios"][i]["eventos"])
            break
    return datos

asigna (datos)

RUTA_BASE_DE_DATOS_USER = "kaiosamapp/json/users.json"
def asignacion (datos,):
    datos = cargar_datos(RUTA_BASE_DE_DATOS_USER)
    datos = asignar_servicio(datos)
    guardar_datos(datos, RUTA_BASE_DE_DATOS_USER)

