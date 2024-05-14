from modules.datos_catalogo import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very,print_
from modules.catalogo_productos_funciones import id_valido,tipo_productos,int_precio
from modules.catalogo_productos_funciones import int_nuevo,int_regular,int_leal,int_cantidad_total
from modules.catalogo_productos_funciones import modificar,mostrar_tipo_productos
from modules.catalogo_productos_funciones import kame_celular, kame_computador,kame_tv

def crear_product(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    catalogo_productos={}
    catalogo_productos["code"] = "0002"
    try:
        catalogo_productos["id"]=id_valido(catalogo_productos)
        for i in range(len(datos_catalogo["catalogo_productos"])):
            if datos_catalogo["catalogo_productos"][i]["id"] == catalogo_productos["id"]:
                print (datos_catalogo["catalogo_productos"][i]["id"],"ya se encuentra registrado!")
                return datos_catalogo
    except Exception as e:
        reportar_error_a_txt(e)
        catalogo_productos["id"] = ""
    catalogo_productos["referencia"]=input("Ingrese la referencia: ")
    catalogo_productos["marca"]=input("Ingrese el marca: ")
    tipo_productos(catalogo_productos)
    int_precio(catalogo_productos)
    catalogo_productos["garantia"]=input("Ingrese la garantia: ")
    catalogo_productos["descripcion"]=input("Ingrese la descripcion: ")
    int_cantidad_total(catalogo_productos)
    catalogo_productos["cantidad_vendida"]=0
    catalogo_productos["descuento"]={"nuevo": 0,"regular":0,"leal":0}
    int_nuevo(catalogo_productos)
    int_regular(catalogo_productos)
    int_leal(catalogo_productos)
    
    datos_catalogo["catalogo_productos"].append(catalogo_productos)
    print( catalogo_productos["referencia"],catalogo_productos["marca"],"registrado con éxito!")
    return datos_catalogo
    
def crear_producto():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = crear_product(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def eliminar_product(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["id"] == id:
            marca = (datos_catalogo["catalogo_productos"][i]["referencia"],datos_catalogo["catalogo_productos"][i]["marca"])
            datos_catalogo["catalogo_productos"].pop(i)
            separador = " "
            marca = separador.join(map(str, marca))
            print(marca,"eliminado...")
            #print("Producto eliminado!")
            return datos_catalogo
    print("Producto no existente...")    
    return datos_catalogo

def eliminar_producto():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = eliminar_product(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
    

def modificar_product(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["id"] == id:
            modificar(datos_catalogo,i)
            return datos_catalogo
    print("Producto no existente...")     
    return datos_catalogo

def modificar_producto():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = modificar_product(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def consultar_product(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["id"] == id:
            print(datos_catalogo["catalogo_productos"][i])
            return datos_catalogo
    print("Producto no existente...")    
    return datos_catalogo

def consultar_producto():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = consultar_product(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def listar_service(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    kame_celular(datos_catalogo)
    kame_tv(datos_catalogo)
    kame_computador(datos_catalogo)
    return datos_catalogo

def mostrar_productos():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = listar_service(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def mostrar_types_productos(datos_catalogo):
    datos_catalogo = dict(datos_catalogo)
    datos_catalogo["catalogo_productos"]
    for i in range(len(datos_catalogo["catalogo_productos"])):
        mostrar_tipo_productos(datos_catalogo)
        return datos_catalogo
    
def mostrar_tipos_productos():
    while True:
        datos_catalogo = cargar_datos_catalogo(RUTA_BASE_DE_DATOS_CATALOGO)
        datos_catalogo = mostrar_types_productos(datos_catalogo)
        guardar_datos_catalogo(datos_catalogo, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
