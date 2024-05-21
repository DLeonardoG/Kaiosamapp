import json



#def cargar_datos(archivo):
#    datos = {}
#    with open(archivo,"r") as file:
#        datos=json.load(file)
#    return datos

def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo, "r", encoding='utf-8') as file:
            datos = json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo}' no contiene un JSON válido.")
    except Exception as e:
        print(f"Se produjo un error al intentar leer el archivo: {e}")
    return datos

        
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    

#Constants
RUTA_BASE_DE_DATOS ="prueba/j.son/datos.json"

datos = cargar_datos(RUTA_BASE_DE_DATOS)

