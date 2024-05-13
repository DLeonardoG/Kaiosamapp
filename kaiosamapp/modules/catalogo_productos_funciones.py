from modules.funciones_secundarias import reportar_error_a_txt

def int_id(catalogo_productos):
    while True:
        try:
            catalogo_productos["id"] = int(input("Ingrese el id: "))
            if isinstance(catalogo_productos["id"], int): return catalogo_productos["id"]
            else: raise ValueError("id ", catalogo_productos["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print("Ingrese un id valido")
            
def id_valido(catalogo_productos):    
    while True:
        int_id(catalogo_productos)
        cad = str(catalogo_productos["id"])
        if len(cad) == 5: return str(catalogo_productos["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print("El numero de id debe tener 5 digitos")
            catalogo_productos["id"] = ""
            
def tipo_productos(catalogo_productos):    
    while True:
        op = input("Ingrese el tipo de Kame producto: \n    1. Kame celular\n    2. kame tv\n    3. kame computador\n    4. Combo Dragon\n>>    ")
        if op == "1": 
            catalogo_productos["tipo_productos"] = "kame_celular"                    
            break
        elif op == "2":
            catalogo_productos["tipo_productos"] = "kame_tv"                    
            break
        elif op == "3":
            catalogo_productos["tipo_productos"] = "kame_computador"                    
            break
        else:
            dm = "Error al registrar tipo_productos"
            reportar_error_a_txt(dm)
            print("El tipo_productos no es valido")
            catalogo_productos["tipo_productos"] = ""  
            
def int_precio(catalogo_productos):
    while True:
        try:
            catalogo_productos["precio"] = int(input("Ingrese el precio: "))
            if isinstance(catalogo_productos["precio"], int): 
                catalogo_productos["precio"] = catalogo_productos["precio"]
                break
            else: raise ValueError("precio ", catalogo_productos["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print("Ingrese un precio valido")
            
def int_nuevo(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(catalogo_productos["descuento"]["nuevo"], int): 
                catalogo_productos["descuento"]["nuevo"] = catalogo_productos["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", catalogo_productos["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios nuevos valido")
            
def int_regular(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(catalogo_productos["descuento"]["regular"], int): 
                catalogo_productos["descuento"]["regular"] = catalogo_productos["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", catalogo_productos["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios regulares valido")
            
def int_leal(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(catalogo_productos["descuento"]["leal"], int): 
                catalogo_productos["descuento"]["leal"] = catalogo_productos["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", catalogo_productos["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios leales valido")
            
def int_cantidad_total(catalogo_productos):
    while True:
        try:
            catalogo_productos["cantidad_total"] = int(input("Ingrese la catidad total: "))
            if isinstance(catalogo_productos["cantidad_total"], int): 
                catalogo_productos["cantidad_total"] = catalogo_productos["cantidad_total"]
                break
            else: raise ValueError("La cantidad total ", catalogo_productos["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print("Ingrese una cantidad total valida")
            
def mod_int_precio(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["precio"] = int(input("Ingrese el precio nuevo: "))
            if isinstance(datos["catalogo_productos"][i]["precio"], int): 
                datos["catalogo_productos"][i]["precio"] = datos["catalogo_productos"][i]["precio"]
                return datos                    
            else: raise ValueError("precio ", datos["catalogo_productos"][i]["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print("Ingrese un precio valido")
            
def mod_int_cantidad_total(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["cantidad_total"] = int(input("Ingrese la catidad total nueva: "))
            if isinstance(datos["catalogo_productos"][i]["cantidad_total"], int): 
                datos["catalogo_productos"][i]["cantidad_total"] = datos["catalogo_productos"][i]["cantidad_total"]
                return datos                    
            else: raise ValueError("La cantidad total ", datos["catalogo_productos"][i]["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print("Ingrese una cantidad total valida")
            
def mod_int_cantidad_vendida(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["cantidad_vendida"] = int(input("Ingrese la catidad vendida nueva: "))
            if isinstance(datos["catalogo_productos"][i]["cantidad_vendida"], int): 
                datos["catalogo_productos"][i]["cantidad_vendida"] = datos["catalogo_productos"][i]["cantidad_vendida"]
                return datos                    
            else: raise ValueError("La cantidad vendida ", datos["catalogo_productos"][i]["cantidad_vendida"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad vendida"
            reportar_error_a_txt(e)
            print("Ingrese una cantidad vendida valida")
            
def mod_int_nuevo(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(datos["catalogo_productos"][i]["descuento"]["nuevo"], int): 
                datos["catalogo_productos"][i]["descuento"]["nuevo"] = datos["catalogo_productos"][i]["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", datos["catalogo_productos"][i]["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios nuevos valido")
            
def mod_int_regular(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(datos["catalogo_productos"][i]["descuento"]["regular"], int): 
                datos["catalogo_productos"][i]["descuento"]["regular"] = datos["catalogo_productos"][i]["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", datos["catalogo_productos"][i]["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios regulares valido")
            
def mod_int_leal(datos,i):
    while True:
        try:
            datos["catalogo_productos"][i]["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(datos["catalogo_productos"][i]["descuento"]["leal"], int): 
                datos["catalogo_productos"][i]["descuento"]["leal"] = datos["catalogo_productos"][i]["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", datos["catalogo_productos"][i]["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios leales valido")
            
def mod_int_descuento(datos,i):    
    while True:
        op = input("Ingrese el descuento:\n     0. Salir\n     1. Nuevo\n     2. Regular\n     3. Leal\n>>")
        if op == "1": 
            mod_int_nuevo(datos,i)
            print(datos["catalogo_productos"][i]["descuento"]["nuevo"],"modificado con éxito!")         
        elif op == "2":
            mod_int_regular(datos,i) 
            print(datos["catalogo_productos"][i]["descuento"]["regular"],"modificado con éxito!")
        elif op == "3":
            mod_int_leal(datos,i)
            print(datos["catalogo_productos"][i]["descuento"]["leal"],"modificado con éxito!")
        elif op == "0": return datos
        else:
            dm = "Error al registrar descuento"
            reportar_error_a_txt(dm)
            print("El descuento no es valido")
            
def modificar(datos,i):    
    while True:
        op = input("Ingrese una opcion:\n    0. Salir \n    1. Referencia\n    2. Plan\n    3. Precio\n    4. Duracion\n    5. Descripcion\n    6. Cantidad Total\n    7. Cantidad Vendida\n    8. Descuento \n\n>>  ")
        if op == "1": 
            datos["catalogo_productos"][i]["referencia"] = input("Ingrese la referencia nueva: ")
            print(datos["catalogo_productos"][i]["referencia"],"modificada con éxito!")                
        elif op == "2":
            datos["catalogo_productos"][i]["plan"] = input("Ingrese el plan nuevo: ")                    
            print(datos["catalogo_productos"][i]["plan"],"modificado con éxito!")                
        elif op == "3":
            mod_int_precio(datos,i)
            print(datos["catalogo_productos"][i]["precio"],"modificado con éxito!")                   
        elif op == "4":
            datos["catalogo_productos"][i]["duracion"] = input("Ingrese la duracion nueva: ")
            print(datos["catalogo_productos"][i]["duracion"],"modificado con éxito!")         
        elif op == "5": 
            datos["catalogo_productos"][i]["descripcion"] = input("Ingrese la descripcion nueva: ")
            print(datos["catalogo_productos"][i]["descripcion"],"modificado con éxito!")         
        elif op == "6":
            mod_int_cantidad_total(datos,i)
            print(datos["catalogo_productos"][i]["cantidad_total"],"modificado con éxito!")         
        elif op == "7":
            mod_int_cantidad_vendida(datos,i)
            print(datos["catalogo_productos"][i]["cantidad_vendida"],"modificado con éxito!")         
        elif op == "8": mod_int_descuento(datos,i)
        elif op == "0": return datos        
        else:
            dm = "Error al registrar tipo_productos"
            reportar_error_a_txt(dm)
            print("Opcion no valida")
