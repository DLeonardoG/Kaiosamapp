from modules.funciones_secundarias import reportar_error_a_txt

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
                if len(cad)>= 8 and len(cad)<= 10: return usuarios["documento"]
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