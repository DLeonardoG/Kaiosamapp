from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida
#from modules.catalogo_productos_funciones import mostrar_productos,mostrar_tipos_productos
from modules.catalogo_productos_funciones import id_valido

def int_edad(usuarios):
    while True:
        try:
            usuarios["edad"] = int(input("Ingrese la edad: "))
            if usuarios["edad"] >= 18: return usuarios["edad"]
            else: raise ValueError("Edad ", usuarios["edad"]," es menor a 18")
        except Exception as e:
            e = e,"Error al registrar edad"
            reportar_error_a_txt(e)
            print("Usuario debe ser mayor de edad")
            
def int_documento(usuarios):
    while True:
        try:
            usuarios["documento"] = int(input("Ingrese el documento: "))
            if isinstance(usuarios["documento"], int):
                cad = str(usuarios["documento"])  
                if len(cad)>= 8 and len(cad)<= 10: 
                    usuarios["documento"] = cad
                    return usuarios["documento"]
                else: raise ValueError("documento", usuarios["documento"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar documento"
            reportar_error_a_txt(e)
            print("Ingrese un documento valido")
            


def int_telefono(usuarios):
    while True:
        try:
            usuarios["telefono"] = int(input("Ingrese el telefono: "))
            if isinstance(usuarios["telefono"], int): return usuarios["telefono"]
            else: raise ValueError("telefono ", usuarios["telefono"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar telefono"
            reportar_error_a_txt(e)
            print("Ingrese un telefono valido")

def telefono_valido(usuarios):    
    while True:
        int_telefono(usuarios)
        cad = str(usuarios["telefono"])
        if len(cad) == 10: break
        else:
            dm = "Error al registrar telefono"
            reportar_error_a_txt(dm)
            print("El numero de telefono debe tener 10 digitos")
            usuarios["telefono"] = ""
            
def sexo(usuarios):    
    while True:
        op = input("Ingrese el sexo: \n 1. Masculino \n 2. Femenino \n 3. Otro\n>>>")
        if op == "1": 
            usuarios["sexo"] = "Masculino"                    
            break
        elif op == "2":
            usuarios["sexo"] = "Femenino"                    
            break
        elif op == "3":
            usuarios["sexo"] = "Otro"                    
            break
        else:
            dm = "Error al registrar sexo"
            reportar_error_a_txt(dm)
            print("El sexo no es valido")
            usuarios["sexo"] = ""   

def compra(usuarios):    
    while True:
        op = input("Compra de... \n 1. Masculino \n 2. Femenino \n 3. Otro\n>>>")
        if op == "1": 
            usuarios["sexo"] = "Masculino"                    
            break
        elif op == "2":
            while True:
                op_l = input("Lectura de... \n 0. Salir\n 1. Todos los servicios \n 2. Sercicio especifico\n>>>")
                if op_l == "1": 
                    mostrar_productos()
                    while True:
                        op_l_2 = input("¿Realizar compra? \n 1. Si \n 2. No")
                        if op_l_2 == "1":
                            id_valido()
                            cantidad = int(input("Ingrese la cantidad a comprar: "))
                            #se suma la cantidad a vendido y se le quita a total
                            #le paso los valores como id, referencia,precio,cantidad, y la fecha de la compra
                            #al terminar la compra le dice compra conn exito a la vez que se añade a facturas con el id y el id unico y code
                            
                            
                        elif op_l_2 == "2": break
                        elif op_l_2 == "0":
                            print("menu_anterior")
                            break
                        else: opcion_no_valida()                    
                elif op_l == "2":
                    mostrar_tipos_productos()         
                    break
                elif op_l == "0":
                    print("menu_anterior")
                    break
                else:
                    dm = "Error al registrar sexo"
                    reportar_error_a_txt(dm)
                    print("El sexo no es valido")
                    usuarios["sexo"] = ""                   
            
        elif op == "3":
            usuarios["sexo"] = "Otro"                    
            break
        else:
            dm = "Error al registrar sexo"
            reportar_error_a_txt(dm)
            print("El sexo no es valido")
            usuarios["sexo"] = ""   