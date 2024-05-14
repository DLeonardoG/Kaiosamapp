from modules.datos_catalogo import *
from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
from modules.funciones_secundarias import clear_screen,very,print_
from modules.catalogo_productos_funciones import id_valido,tipo_productos,int_precio
from modules.catalogo_productos_funciones import int_nuevo,int_regular,int_leal,int_cantidad_total
from modules.catalogo_productos_funciones import modificar,mostrar_tipo_productos
from modules.catalogo_productos_funciones import kame_celular, kame_computador,kame_tv

def crear_product(datos):
    datos = dict(datos)
    catalogo_productos={}
    catalogo_productos["code"] = "0002"
    try:
        catalogo_productos["id"]=id_valido(catalogo_productos)
        for i in range(len(datos["catalogo_productos"])):
            if datos["catalogo_productos"][i]["id"] == catalogo_productos["id"]:
                print (datos["catalogo_productos"][i]["id"],"ya se encuentra registrado!")
                return datos
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
    
    datos["catalogo_productos"].append(catalogo_productos)
    print( catalogo_productos["referencia"],catalogo_productos["marca"],"registrado con éxito!")
    return datos
    
def crear_producto():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = crear_product(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def eliminar_product(datos):
    datos = dict(datos)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            marca = (datos["catalogo_productos"][i]["referencia"],datos["catalogo_productos"][i]["marca"])
            datos["catalogo_productos"].pop(i)
            separador = " "
            marca = separador.join(map(str, marca))
            print(marca,"eliminado...")
            #print("Producto eliminado!")
            return datos
    print("Producto no existente...")    
    return datos

def eliminar_producto():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = eliminar_product(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
    

def modificar_product(datos):
    datos = dict(datos)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            modificar(datos,i)
            return datos
    print("Producto no existente...")     
    return datos

def modificar_producto():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = modificar_product(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def consultar_product(datos):
    datos = dict(datos)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            print(datos["catalogo_productos"][i])
            return datos
    print("Producto no existente...")    
    return datos

def consultar_producto():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = consultar_product(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def listar_service(datos):
    datos = dict(datos)
    kame_celular(datos)
    kame_tv(datos)
    kame_computador(datos)
    return datos

def mostrar_productos():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = listar_service(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def mostrar_types_productos(datos):
    datos = dict(datos)
    datos["catalogo_productos"]
    mostrar_tipo_productos(datos)
    return datos


    
def mostrar_tipos_productos():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
        datos = mostrar_types_productos(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def agregar_producto(datos):
    datos = dict(datos)
    id =input("Ingrese el id del Producto: ")
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            product = datos["catalogo_productos"][i]
            
            return product
    print("Producto no existente...")    
    return datos

