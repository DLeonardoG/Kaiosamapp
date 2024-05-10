from funciones_secundarias import *
from datos import *



def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    try:
        usuarios["edad"] = int(input("Ingrese la edad: "))
        
    except Exception as e:
        reportar_error_a_txt(e)
        usuarios["edad"] = 0
    usuarios["nombre"]=input("Ingrese el nombre: ")
    usuarios["apellido"]=input("Ingrese el apellido: ")
    usuarios["documento"]=input("Ingrese el documento: ")


    
    datos["usuarios"].append(usuarios)
    print("usuarios registrado con éxito!")
    return datos

registrar_user(datos)