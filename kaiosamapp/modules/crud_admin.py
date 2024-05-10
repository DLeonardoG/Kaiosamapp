from funciones_secundarias import *
from datos import *



def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    try:
        usuarios["edad"] = int(input("Ingrese la edad: "))
        
    except Exception as e:
        reportar_error_a_txt(e)
        usuarios["edad"] = 18
    usuarios["documento"]=input("Ingrese el documento: ")
    usuarios["nombre"]=input("Ingrese el nombre: ")
    usuarios["apellido"]=input("Ingrese el apellido: ")


    
    datos["usuarios"].append(usuarios)
    print("usuarios registrado con éxito!")
    return datos

registrar_user(datos)


def eliminar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("usuario eliminado!")
    return datos

#eliminar_user(datos)

def actualizar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del participante: ")
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
guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)