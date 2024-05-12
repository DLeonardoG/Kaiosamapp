from modules.funciones_secundarias import reportar_error_a_txt,telefono_valido,int_edad
from modules.datos_users import *




def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    try:
        usuarios["documento"]=input("Ingrese el documento: ")
        for i in range(len(datos["usuarios"])):
            if datos["usuarios"][i]["documento"] == usuarios["documento"]:
                print (datos["usuarios"][i]["documento"],"ya se encuentra registrado!")
                return datos
                
    except Exception as e:
        reportar_error_a_txt(e)
        usuarios["documento"] = ""
    
    int_edad(usuarios)
    usuarios["nombre"]=input("Ingrese el nombre: ")
    usuarios["apellido"]=input("Ingrese el apellido: ")
    telefono_valido(usuarios)

    usuarios["sexo"]=input("Ingrese el sexo (masculino, femenino, otro): ")
    usuarios["ciudad"]=input("Ingrese la ciudad: ")
    usuarios["direccion"]=input("Ingrese la direccion: ")
    usuarios["email"]=input("Ingrese el email: ")
    usuarios["categoria"]=input("Ingrese la categoria: ")
    usuarios["registro_servicios"]=[]
    usuarios["registro_productos"]=[]
    usuarios["registro_pqr"]=[]
    
    datos["usuarios"].append(usuarios)
    print( usuarios["nombre"],usuarios["apellido"],"registrado con éxito!")
    return datos

def crear_usuario():
        while True:
            datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
            datos = registrar_user(datos)
            guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
            break
#crear_usuario()

def eliminar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            user = (datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            datos["usuarios"].pop(i)
            print(user,"eliminado!")
            break
    return datos

def eliminar_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = eliminar_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        break

#eliminar_user(datos)

def actualizar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            user = (datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            print ("Actulice el nombre:")
            datos["usuarios"][i]["nombre"]=input("Ingrese el nombre nuevo: ")
            print(user,"actualizado!")
            return datos
    return datos
        
            
def actualizar_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = actualizar_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        break
#actualizar_user(datos)

def leer_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            print(datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            print(datos["usuarios"][i]["documento"],"  -  Documento")
            print(datos["usuarios"][i]["sexo"],"  -  Sexo")
            print(datos["usuarios"][i]["edad"],"  -  Edad")
            print(datos["usuarios"][i]["ciudad"],"  -  Ciudad")
            print(datos["usuarios"][i]["direccion"],"  -  Direccion")
            print(datos["usuarios"][i]["email"],"  -  Email")
            print(datos["usuarios"][i]["categoria"],"  -  Categoria")
            print(datos["usuarios"][i]["registro_servicios"],"  -  Registro de servicios")
            print(datos["usuarios"][i]["registro_productos"],"  -  Registro de productos")
            print(datos["usuarios"][i]["registro_pqr"],"  -  Registro de PQR")
    return datos

def leer_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = leer_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        break
    
#leer_user(datos)
#guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)