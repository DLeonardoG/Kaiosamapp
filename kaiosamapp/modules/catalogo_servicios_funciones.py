from modules.funciones_secundarias import reportar_error_a_txt


def int_id(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["id"] = int(input("Ingrese el id: "))
            if isinstance(catalogo_servicios["id"], int): return catalogo_servicios["id"]
            else: raise ValueError("id ", catalogo_servicios["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print("Ingrese un id valido")
            
def id_valido(catalogo_servicios):    
    while True:
        int_id(catalogo_servicios)
        cad = str(catalogo_servicios["id"])
        if len(cad) == 5: return str(catalogo_servicios["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print("El numero de id debe tener 5 digitos")
            catalogo_servicios["id"] = ""
            
def tipo_servicios(catalogo_servicios):    
    while True:
        op = input("Ingrese el tipo_servicios: \n    1. Fibra optica Namekusei\n    2. Pospago Roshi\n    3. Prepago Krillin\n    4. Combo Dragon\n>>    ")
        if op == "1": 
            catalogo_servicios["tipo_servicios"] = "fibra_optica_namekusei"                    
            break
        elif op == "2":
            catalogo_servicios["tipo_servicios"] = "pospago_roshi"                    
            break
        elif op == "3":
            catalogo_servicios["tipo_servicios"] = "prepago_Krilin"                    
            break
        elif op == "4":
            catalogo_servicios["tipo_servicios"] = "combo_dragon"                    
            break
        else:
            dm = "Error al registrar tipo_servicios"
            reportar_error_a_txt(dm)
            print("El tipo_servicios no es valido")
            catalogo_servicios["tipo_servicios"] = ""  
            
def int_precio(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["precio"] = int(input("Ingrese el precio: "))
            if isinstance(catalogo_servicios["precio"], int): 
                catalogo_servicios["precio"] = catalogo_servicios["precio"]
                break
            else: raise ValueError("precio ", catalogo_servicios["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print("Ingrese un precio valido")
            
def int_nuevo(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(catalogo_servicios["descuento"]["nuevo"], int): 
                catalogo_servicios["descuento"]["nuevo"] = catalogo_servicios["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", catalogo_servicios["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios nuevos valido")
            
def int_regular(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(catalogo_servicios["descuento"]["regular"], int): 
                catalogo_servicios["descuento"]["regular"] = catalogo_servicios["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", catalogo_servicios["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios regulares valido")
            
def int_leal(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(catalogo_servicios["descuento"]["leal"], int): 
                catalogo_servicios["descuento"]["leal"] = catalogo_servicios["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", catalogo_servicios["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print("Ingrese un descuento para usuarios leales valido")
            
def int_cantidad_total(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["cantidad_total"] = int(input("Ingrese la catidad total: "))
            if isinstance(catalogo_servicios["cantidad_total"], int): 
                catalogo_servicios["cantidad_total"] = catalogo_servicios["cantidad_total"]
                break
            else: raise ValueError("La cantidad total ", catalogo_servicios["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print("Ingrese una cantidad total valida")
