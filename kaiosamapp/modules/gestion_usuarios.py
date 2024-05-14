from modules.funciones_secundarias import reportar_error_a_txt,very,clear_screen,line,linen,print_
from modules.gestion_usuarios_funciones import telefono_valido,int_edad,sexo,int_documento
from modules.catalogo_productos import id_valido
#from modules.catalogo_productos_funciones import mostrar_productos,mostrar_tipos_productos
from modules.datos_users import *

def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    int_documento(usuarios)
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == usuarios["documento"]:
            print_ (datos["usuarios"][i]["documento"],"ya se encuentra registrado :)")
            return datos

    int_edad(usuarios)
    usuarios["nombre"]=input("Ingrese el nombre: ")
    usuarios["apellido"]=input("Ingrese el apellido: ")
    telefono_valido(usuarios)
    sexo(usuarios)
    usuarios["ciudad"]=input("Ingrese la ciudad: ")
    usuarios["direccion"]=input("Ingrese la direccion: ")
    usuarios["email"]=input("Ingrese el email: ")
    usuarios["categoria"]=("nuevo")
    usuarios["registro_servicios"]=[]
    usuarios["registro_productos"]=[]
    usuarios["registro_pqr"]=[]
    
    datos["usuarios"].append(usuarios)
    line()
    print_( usuarios["nombre"],usuarios["apellido"],"registrado con éxito!")
    line()
    return datos

def crear_usuario():
        while True:
            datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
            datos = registrar_user(datos)
            guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
            continuar = very()
            if continuar == "2": break
            else: clear_screen()

def eliminar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            user = (datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            datos["usuarios"].pop(i)
            separador = " "
            user = separador.join(map(str, user))
            print_(user,"eliminado...")
            return datos
    print_("Usuario no existente...")    
    return datos

def eliminar_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = eliminar_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

#eliminar_user(datos)

def actualizar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            user = str(datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            print_ ("Actualice la categoria: ")
            datos["usuarios"][i]["categoria"]=input("Ingrese la categoria: ")
            print_(user,"actualizado!")
            return datos
    print_("Usuario no existente...")    
    return datos


def actualizar_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = actualizar_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
#actualizar_user(datos)

def leer_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            print_(datos["usuarios"][i]["nombre"], datos["usuarios"][i]["apellido"])
            es()
            print_("Documento")
            print_(datos["usuarios"][i]["documento"],)
            es()
            print_(datos["usuarios"][i]["sexo"], "  -  Sexo")
            print_(str(datos["usuarios"][i]["edad"]), "  -  Edad")
            print_(datos["usuarios"][i]["ciudad"], "  -  Ciudad")
            print_(datos["usuarios"][i]["direccion"], "  -  Direccion")
            print_(str(datos["usuarios"][i]["telefono"]), "  -  Telefono")
            print_(datos["usuarios"][i]["email"],"  -  Email")
            print_(datos["usuarios"][i]["categoria"],"  -  Categoria")
            print_(i)
            print_(("---------          Registro de servicios          ---------"))
            for sn in range(len(datos["usuarios"][i]["registro_servicios"])):
                max_length_sn = max(len(datos["usuarios"][i]["registro_servicios"][sn]["referencia"] + " " + datos["usuarios"][i]["registro_servicios"][sn]["tipo_servicios"]) for sn_ in range(len(datos["usuarios"][i]["registro_servicios"])))
                print_("")
                print_(datos["usuarios"][i]["registro_servicios"][sn]["referencia"] + "   -  " + datos["usuarios"][i]["registro_servicios"][sn]["tipo_servicios"])
                print_(datos["usuarios"][i]["registro_servicios"][sn]["id"], "  -  id")
                print_(datos["usuarios"][i]["registro_servicios"][sn]["fecha"], "  -  fecha")
                print_(str(datos["usuarios"][i]["registro_servicios"][sn]["precio"]), "  -  precio")
                        
            print_(datos["usuarios"][i]["registro_productos"],"  -  Registro de productos")
            print_(datos["usuarios"][i]["registro_pqr"],"  -  Registro de PQR")
            return datos
    
    print_("Usuario no existente...")  
    return datos

def leer_usuario():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = leer_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
def new_compra_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    
    #mostrar_productos,mostrar_tipos_productos
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["registro_productos"].append(new_compra_user(datos))
            return datos
    print_("Usuario no existente...")    
    return datos

def buscando_producto(datos):
    datos = dict(datos)
    catalogo_productos={}
    try:
        catalogo_productos["id"]=id_valido(catalogo_productos)
        for i in range(len(datos["catalogo_productos"])):
            if datos["catalogo_productos"][i]["id"] == catalogo_productos["id"]:
                print_ (datos["catalogo_productos"][i]["id"],"ya se encuentra registrado!")
                
    except Exception as e:
        reportar_error_a_txt(e)
        catalogo_productos["id"] = ""
    for i in range(len(datos["catalogo_productos"])):
        if datos["catalogo_productos"][i]["id"] == id:
            producto = datos["catalogo_productos"][i]
            break
    return producto



def compra_producto(datos):
   
    
    buscando_producto(datos_catalogo)
    datos_catalogo = dict(datos_catalogo)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            #datos["usuarios"][i]["registro_productos"]=[]
            datos["usuarios"][i]["registro_productos"].append(buscando_producto(datos))
            print_(datos["usuarios"][i]["registro_productos"])
            guardar_datos(datos_catalogo, RUTA_BASE_DE_DATOS_USERS)
            break
    return datos



def nueva_compra_usuario_():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = compra_producto(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
    
def asignacion_producto(datos):
    datos = dict(datos)
    documento =("Ingrese el documento del participante: ")
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
    id =("Ingrese el id del Producto: ")
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
            
RUTA_BASE_DE_DATOS_CATALOGO ="kaiosamapp/json/catalogo.json"
DATOS_PRODUCTOS = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)

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
    documento =("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            #datos["usuarios"][i]["productos"]=[]
            datos["usuarios"][i]["productos"].append(buscando_producto(DATOS_PRODUCTOS))
            print(datos["usuarios"][i]["productos"])
            guardar_datos(datos["usuarios"][i]["productos"])
            break
    return datos

def nueva_compra_usuario (datos):
    datos = dict(datos)
    documento =("Ingrese el documento del usuario: ")
    datos = cargar_datos(datos)
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["registro_productos"].append(buscando_producto(DATOS_PRODUCTOS))
            print(datos["usuarios"][i]["registro_productos"])
            guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
            break
    guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
    return datos
#leer_user(datos)
#guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)


#Falta añadir estas dos funciones OJO
#def nueva_compra_user(datos):
#def nueva_compra():

#def recomendacion_user(datos):
#def recomendaciones():