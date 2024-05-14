import json
from funciones_secundarias import reportar_error_a_txt
from modules.datos_catalogo import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very,print_,_fecha_
from modules.catalogo_productos_funciones import id_valido,tipo_productos,int_precio
from modules.catalogo_productos_funciones import int_nuevo,int_regular,int_leal,int_cantidad_total
from modules.catalogo_productos_funciones import modificar,mostrar_tipo_productos
from modules.catalogo_productos_funciones import kame_celular, kame_computador,kame_tv

def int_id(catalogo_productos):
    while True:
        try:
            catalogo_productos["id"] = int(input("Ingrese el id: "))
            if isinstance(catalogo_productos["id"], int) and catalogo_productos["id"] > -1: 
                return catalogo_productos["id"]
            else: raise ValueError("id ", catalogo_productos["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print_("Ingrese un id valido")
            
def id_valido(catalogo_productos):    
    while True:
        int_id(catalogo_productos)
        cad = str(catalogo_productos["id"])
        if len(cad) == 5: return str(catalogo_productos["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print_("El numero de id debe tener 5 digitos")
            catalogo_productos["id"] = ""


    
def asignacion_producto(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del participante: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["productos"]=[]
            datos["usuarios"][i]["productos"].append(buscando_producto(datos))
            print(datos["usuarios"][i]["productos"])
            break
    return datos
def busqueda(datos):
    datos = dict(datos)
    producto = {}
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            datos["catalogo_productos"][i]["code"] = producto["code"]
            datos["catalogo_productos"][i]["id"] = producto["id"]
            datos["catalogo_productos"][i]["tipo_de_servicio"] = producto["tipo_de_servicio"]
            datos["catalogo_productos"][i]["referencia"] = producto["referencia"]
            datos["catalogo_productos"][i]["precio"] = producto["precio"]
            producto["fecha"] = _fecha_ 
            print(producto)
    return producto
            
print (producto)

def buscando_producto(datos):
    datos = dict(datos)
    id =input("id del producto: ")
    producto={}
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            producto=datos["catalogo_productos"][i]
            break
    return producto
    
def asignacion_producto(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            #datos["usuarios"][i]["productos"]=[]
            datos["usuarios"][i]["productos"].append(buscando_producto(datos))
            print(datos["usuarios"][i]["productos"])
            break
    return datos