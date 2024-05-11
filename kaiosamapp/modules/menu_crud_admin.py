from menu_crud_admin_funciones import *
from datos_users import *
from funciones_secundarias import *
#from menu_1 import *


    

def menu_admin_crud_users():
    clear_screen()
    #diseño_logo()
    print ("1. Crear usuario 📁")
    print ("2. Eliminar usuario 🗑️")
    print ("3. Actualizar usuario")
    print ("4. Leer usuario")
    print ("0. Salir")
    print("     *************************************")

def pedir_opcion_1_1():
    
    op = 0
    while True:
        try:
            op = int(input("Escoja una opcion: "))
            print("***************************************")
            if op == 1 or op == 2 or op == 3 or op == 4 or op == 0:
                clear_screen()
                break
            else:
                clear_screen()
                main_1()
                print("Valor inválido")
                print("***************************************")
                raise ValueError("Error al elegir menu opcion 1")
        except Exception as e:
            reportar_error_a_txt(e)
            clear_screen()
            menu_admin_crud_users()
            print("Valor inválido")
            print("***************************************")
            
    return op

menu_admin_crud_users()
op = pedir_opcion_1_1()
def menu_1_1(op):
    if op == 1:
        clear_screen()
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = registrar_user(datos)
        datos = guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
    elif op == 2:
        clear_screen()
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = eliminar_user(datos)
        datos = guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
    elif op == 3:
        clear_screen()
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = actualizar_user(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
    elif op == 4:
        clear_screen()
        datos = cargar_datos(RUTA_BASE_DE_DATOS_USERS)
        datos = leer_user(datos)
        datos = guardar_datos(datos, RUTA_BASE_DE_DATOS_USERS)
    elif op == 0:
        clear_screen()
        menu_admin_crud_users
menu_1_1(op)




