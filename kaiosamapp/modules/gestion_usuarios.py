from modules.funciones_secundarias import reportar_error_a_txt,documento_valido,telefono_valido,int_edad,sexo,int_documento,int_telefono,str_sexo
from modules.datos_users import *



def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    documento_valido(usuarios)
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == usuarios["documento"]:
            print (datos["usuarios"][i]["documento"],"ya se encuentra registrado!")
            return datos
    
    int_edad(usuarios)
    usuarios["nombre"]=input("Ingrese el nombre: ")
    usuarios["apellido"]=input("Ingrese el apellido: ")
    telefono_valido(usuarios)
    sexo(usuarios)
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

#eliminar_user(datos)

def actualizar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            print ("Actulice el nombre:")
            datos["usuarios"][i]["nombre"]=input("Ingrese el nombre nuevo: ")
#actualizar_user(datos)

def leer_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            print("nombre - ",datos["usuarios"][i]["nombre"])
            print("apellido - ",datos["usuarios"][i]["apellido"])
            print("documento - ",datos["usuarios"][i]["documento"])
            print("edad - ",datos["usuarios"][i]["edad"])
    return datos

#leer_user(datos)
#guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)