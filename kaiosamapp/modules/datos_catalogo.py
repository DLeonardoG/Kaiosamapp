import json

def cargar_datos_catalogo(archivo):
    datos_catalogo = {}
    with open(archivo,"r") as file:
        datos_catalogo=json.load(file)
    return datos_catalogo

def guardar_datos_catalogo(datos_catalogo, archivo):
    datos_catalogo = dict(datos_catalogo)
    
    diccionario=json.dumps(datos_catalogo, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()

RUTA_BASE_DE_DATOS_CATALOGO ="kaiosamapp/json/catalogo.json"
datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)


