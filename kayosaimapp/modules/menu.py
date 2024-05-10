from funciones_secundarias import * 
from datos import *


def pedir_opcion():
    op = 0
    while True:
        try:
            op = int(input("Escoja una opcion: "))
            print("***************************************")
            if op == 1 or op == 2 or op == 0:
                clear_screen()
                break
            else:
                clear_screen()
                main_1()
                print("Valor inválido")
                print("***************************************")
                raise ValueError("Error al elesgir menu opcion 1")
        except Exception as e:
            reportar_error_a_txt(e)
            clear_screen()
            main_1()
            print("Valor inválido")
            print("***************************************")
            
    return op
            
            
def validar_password():
    while True:
        try:
            password = input("Ingrese la contraseña admin: ")
            if password == "password":
                validar = 1
                print("Puedes pasar guerrero Z")
                break
            else:
                raise ValueError("Error al ingresar conraseña de admin")
        except Exception as e:
            reportar_error_a_txt(e)
            if password == "0":
                validar = 0
                break
            else:
                clear_screen()
                print("Contraseña incorrecta")
                print("Si no eres admin oprime 0")
                print("***************************************")
                
    return validar


def asignacion(op):
    try:
        if op == 1:
            print ("Usuario puedes pasar a", NAME)
            print("Si no eres user oprime 0")
            op = 1
        elif op == 2:
            validar = validar_password() 
            clear_screen()
            if validar == 0:
                print("Adios guerrero Z")
                op = 0
            else:
                print ("Admin puedes pasar a", NAME)
                op = 2
        elif op == 0:
            print("Adios guerrero Z")
            op = 0
        else:
            raise ValueError("Error al ingresar opcion menu 1")
    except Exception as e:
        reportar_error_a_txt(e)


    
    
    
    
main_1()
op = pedir_opcion()
asignacion(op)

def menu_admin_crud_users():
    print ("1. crear usuario")



def acceso(op):
    menu_admin_crud_users()
    try: 
        if op == 1:
            
        
    


    

    
