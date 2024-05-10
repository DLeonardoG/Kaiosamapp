import json



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
RUTA_BASE_DE_DATOS_USERS ="kaiosamapp/json/users.json"

datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)

