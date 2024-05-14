from modules.funciones_secundarias import reportar_error_a_txt,very,clear_screen
from modules.gestion_usuarios_funciones import telefono_valido,int_edad,sexo,int_documento
#from modules.catalogo_productos_funciones import mostrar_productos,mostrar_tipos_productos
from modules.datos_users import *

def registrar_user(datos):
    datos = dict(datos)
    usuarios={}
    int_documento(usuarios)
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
            continuar = very()
            if continuar == "2": break
            else: clear_screen()
#crear_usuario()

def eliminar_user(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            user = (datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            datos["usuarios"].pop(i)
            separador = " "
            user = separador.join(map(str, user))
            print(user,"eliminado...")
            return datos
    print("Usuario no existente...")    
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
            user = (datos["usuarios"][i]["nombre"],datos["usuarios"][i]["apellido"])
            print ("Actulice el nombre:")
            datos["usuarios"][i]["nombre"]=input("Ingrese el nombre nuevo: ")
            print(user,"actualizado!")
            return datos
    print("Usuario no existente...")    
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
            max_length = max(len(datos["usuarios"][i]["nombre"] + " " + datos["usuarios"][i]["apellido"]) for i in range(len(datos["usuarios"])))
            print(datos["usuarios"][i]["nombre"], datos["usuarios"][i]["apellido"])
            print(datos["usuarios"][i]["documento"].rjust(max_length), "  -  Documento")
            print(datos["usuarios"][i]["sexo"].rjust(max_length), "  -  Sexo")
            print(str(datos["usuarios"][i]["edad"]).rjust(max_length), "  -  Edad")
            print(datos["usuarios"][i]["ciudad"].rjust(max_length), "  -  Ciudad")
            print(datos["usuarios"][i]["direccion"].rjust(max_length), "  -  Direccion")
            print(str(datos["usuarios"][i]["telefono"]).rjust(max_length), "  -  Telefono")
            print(datos["usuarios"][i]["email"].rjust(max_length), "  -  Email")
            print(datos["usuarios"][i]["categoria"].rjust(max_length), "  -  Categoria")
            print(i)
            print(("---------          Registro de servicios          ---------"))
            for sn in range(len(datos["usuarios"][i]["registro_servicios"])):
                max_length_sn = max(len(datos["usuarios"][i]["registro_servicios"][sn]["referencia"] + " " + datos["usuarios"][i]["registro_servicios"][sn]["tipo_servicios"]) for sn_ in range(len(datos["usuarios"][i]["registro_servicios"])))
                print("")
                print(datos["usuarios"][i]["registro_servicios"][sn]["referencia"].rjust(max_length_sn) + "   -  " + datos["usuarios"][i]["registro_servicios"][sn]["tipo_servicios"])
                print(datos["usuarios"][i]["registro_servicios"][sn]["id"].rjust(max_length_sn), "  -  id")
                print(datos["usuarios"][i]["registro_servicios"][sn]["fecha"].rjust(max_length_sn), "  -  fecha")
                print(str(datos["usuarios"][i]["registro_servicios"][sn]["precio"]).rjust(max_length_sn), "  -  precio")
                        
            print(datos["usuarios"][i]["registro_productos"],"  -  Registro de productos")
            print(datos["usuarios"][i]["registro_pqr"],"  -  Registro de PQR")
            return datos
    
    print("Usuario no existente...")  
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
    print("Usuario no existente...")    
    return datos
    
#leer_user(datos)
#guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)


#Falta añadir estas dos funciones OJO
#def nueva_compra_user(datos):
#def nueva_compra():

#def recomendacion_user(datos):
#def recomendaciones():