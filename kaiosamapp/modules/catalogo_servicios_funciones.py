from modules.funciones_secundarias import print_,reportar_error_a_txt

def int_id(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["id"] = int(input("Ingrese el id: "))
            if isinstance(catalogo_servicios["id"], int) and catalogo_servicios["id"] > -1: 
                return catalogo_servicios["id"]
            else: raise ValueError("id ", catalogo_servicios["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print_("Ingrese un id valido")
            
def id_valido(catalogo_servicios):    
    while True:
        int_id(catalogo_servicios)
        cad = str(catalogo_servicios["id"])
        if len(cad) == 5: return str(catalogo_servicios["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print_("El numero de id debe tener 5 digitos")
            catalogo_servicios["id"] = ""
            
def tipo_servicios(catalogo_servicios):    
    while True:
        op = input("Ingrese el tipo de servicios: \n    1. Fibra optica Namekusei\n    2. Pospago Roshi\n    3. Prepago Krillin\n    4. Combo Dragon\n>>    ")
        if op == "1": 
            catalogo_servicios["tipo_servicios"] = "fibra_optica_namekusei"
            catalogo_servicios["code_unico"] = "0011"             
            break
        elif op == "2":
            catalogo_servicios["tipo_servicios"] = "pospago_roshi"
            catalogo_servicios["code_unico"] = "0021" 
            break
        elif op == "3":
            catalogo_servicios["tipo_servicios"] = "prepago_Krilin"
            catalogo_servicios["code_unico"] = "0031" 
            break
        elif op == "4":
            catalogo_servicios["tipo_servicios"] = "combo_dragon"
            catalogo_servicios["code_unico"] = "0041"                     
            break
        else:
            dm = "Error al registrar tipo_servicios"
            reportar_error_a_txt(dm)
            print_("El tipo_servicios no es valido")
            catalogo_servicios["tipo_servicios"] = ""  
            
def mostrar_tipo_servicios(datos):    
    while True:
        op = input("Ingrese el tipo de servicios: \n    0. Salir\n    1. Fibra optica Namekusei\n    2. Pospago Roshi\n    3. Prepago Krillin\n    4. Combo Dragon\n>>    ")
        if op == "1": 
            for i in range(len(datos["catalogo_servicios"])):
                if datos["catalogo_servicios"][i]["code_unico"] == "0011":
                    print_(datos["catalogo_servicios"][i]["tipo_servicios"], "  -   Tipo de catalogo_servicios")
                    print_(datos["catalogo_servicios"][i]["id"] + "  -   Id")
                    print_(datos["catalogo_servicios"][i]["referencia"], "  -   Referencia")
                    print_(datos["catalogo_servicios"][i]["plan"], "  -   Plan")
                    print_(datos["catalogo_servicios"][i]["precio"], "  -   Precio")
                    print_(datos["catalogo_servicios"][i]["duracion"], "  -   Duracion")
                    print_(datos["catalogo_servicios"][i]["descripcion"], " - Descripcion")
                    print_(datos["catalogo_servicios"][i]["cantidad_total"], "  -   Cantidad Total")
                    print_(datos["catalogo_servicios"][i]["cantidad_vendida"], "  -   Cantidad vendida")
            return datos
        elif op == "2":
            for i in range(len(datos["catalogo_servicios"])):
                if datos["catalogo_servicios"][i]["code_unico"] == "0021":
                    print_(datos["catalogo_servicios"][i]["tipo_servicios"], "  -   Tipo de catalogo_servicios")
                    print_(datos["catalogo_servicios"][i]["id"] + "  -   Id")
                    print_(datos["catalogo_servicios"][i]["referencia"], "  -   Referencia")
                    print_(datos["catalogo_servicios"][i]["plan"], "  -   Plan")
                    print_(datos["catalogo_servicios"][i]["precio"], "  -   Precio")
                    print_(datos["catalogo_servicios"][i]["duracion"], "  -   Duracion")
                    print_(datos["catalogo_servicios"][i]["descripcion"], " - Descripcion")
                    print_(datos["catalogo_servicios"][i]["cantidad_total"], "  -   Cantidad Total")
                    print_(datos["catalogo_servicios"][i]["cantidad_vendida"], "  -   Cantidad vendida")
            return datos
        elif op == "3":
            for i in range(len(datos["catalogo_servicios"])):
                if datos["catalogo_servicios"][i]["code_unico"] == "0031":
                    print_(datos["catalogo_servicios"][i]["tipo_servicios"], "  -   Tipo de catalogo_servicios")
                    print_(datos["catalogo_servicios"][i]["id"] + "  -   Id")
                    print_(datos["catalogo_servicios"][i]["referencia"], "  -   Referencia")
                    print_(datos["catalogo_servicios"][i]["plan"], "  -   Plan")
                    print_(datos["catalogo_servicios"][i]["precio"], "  -   Precio")
                    print_(datos["catalogo_servicios"][i]["duracion"], "  -   Duracion")
                    print_(datos["catalogo_servicios"][i]["descripcion"], " - Descripcion")
                    print_(datos["catalogo_servicios"][i]["cantidad_total"], "  -   Cantidad Total")
                    print_(datos["catalogo_servicios"][i]["cantidad_vendida"], "  -   Cantidad vendida")
            return datos
        elif op == "4":
            for i in range(len(datos["catalogo_servicios"])):
                if datos["catalogo_servicios"][i]["code_unico"] == "0041":
                    print_(datos["catalogo_servicios"][i]["tipo_servicios"], "  -   Tipo de catalogo_servicios")
                    print_(datos["catalogo_servicios"][i]["id"] + "  -   Id")
                    print_(datos["catalogo_servicios"][i]["referencia"], "  -   Referencia")
                    print_(datos["catalogo_servicios"][i]["plan"], "  -   Plan")
                    print_(datos["catalogo_servicios"][i]["precio"], "  -   Precio")
                    print_(datos["catalogo_servicios"][i]["duracion"], "  -   Duracion")
                    print_(datos["catalogo_servicios"][i]["descripcion"], " - Descripcion")
                    print_(datos["catalogo_servicios"][i]["cantidad_total"], "  -   Cantidad Total")
                    print_(datos["catalogo_servicios"][i]["cantidad_vendida"], "  -   Cantidad vendida")
            return datos
        elif op == "0":
            print_("Regresando...")
            return datos
        else:
            dm = "Error al registrar tipo_servicios"
            reportar_error_a_txt(dm)
            print_("El tipo de servicio no es valido")
            
def int_precio(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["precio"] = int(input("Ingrese el precio: "))
            if isinstance(catalogo_servicios["precio"], int) and catalogo_servicios["precio"] > 1000: 
                catalogo_servicios["precio"] = catalogo_servicios["precio"]
                break
            else: raise ValueError("precio ", catalogo_servicios["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print_("Ingrese un precio valido")
            
def int_nuevo(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(catalogo_servicios["descuento"]["nuevo"], int) and catalogo_servicios["descuento"]["nuevo"] >= 0:
                catalogo_servicios["descuento"]["nuevo"] = catalogo_servicios["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", catalogo_servicios["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios nuevos valido")
            
def int_regular(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(catalogo_servicios["descuento"]["regular"], int) and catalogo_servicios["descuento"]["regular"] >= 0:
                catalogo_servicios["descuento"]["regular"] = catalogo_servicios["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", catalogo_servicios["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios regulares valido")
            
def int_leal(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(catalogo_servicios["descuento"]["leal"], int) and catalogo_servicios["descuento"]["leal"] >= 0: 
                catalogo_servicios["descuento"]["leal"] = catalogo_servicios["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", catalogo_servicios["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios leales valido")
            
def int_cantidad_total(catalogo_servicios):
    while True:
        try:
            catalogo_servicios["cantidad_total"] = int(input("Ingrese la catidad total: "))
            if isinstance(catalogo_servicios["cantidad_total"], int) and catalogo_servicios["cantidad_total"] > 0:
                catalogo_servicios["cantidad_total"] = catalogo_servicios["cantidad_total"]
                break
            else: raise ValueError("La cantidad total ", catalogo_servicios["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad total valida")
            
def mod_int_precio(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["precio"] = int(input("Ingrese el precio nuevo: "))
            if isinstance(datos["catalogo_servicios"][i]["precio"], int) and datos["catalogo_servicios"][i]["precio"] > 1000: 
                datos["catalogo_servicios"][i]["precio"] = datos["catalogo_servicios"][i]["precio"]
                return datos                    
            else: raise ValueError("precio ", datos["catalogo_servicios"][i]["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print_("Ingrese un precio valido")
            
def mod_int_cantidad_total(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["cantidad_total"] = int(input("Ingrese la catidad total nueva: "))
            if isinstance(datos["catalogo_servicios"][i]["cantidad_total"], int) and datos["catalogo_servicios"][i]["cantidad_total"] >= 0: 
                datos["catalogo_servicios"][i]["cantidad_total"] = datos["catalogo_servicios"][i]["cantidad_total"]
                return datos                    
            else: raise ValueError("La cantidad total ", datos["catalogo_servicios"][i]["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad total valida")
            
def mod_int_cantidad_vendida(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["cantidad_vendida"] = int(input("Ingrese la catidad vendida nueva: "))
            if isinstance(datos["catalogo_servicios"][i]["cantidad_vendida"], int) and datos["catalogo_servicios"][i]["cantidad_vendida"] >= 0:
                datos["catalogo_servicios"][i]["cantidad_vendida"] = datos["catalogo_servicios"][i]["cantidad_vendida"]
                return datos
            else: raise ValueError("La cantidad vendida ", datos["catalogo_servicios"][i]["cantidad_vendida"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad vendida"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad vendida valida")
            
def mod_int_nuevo(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(datos["catalogo_servicios"][i]["descuento"]["nuevo"], int) and datos["catalogo_servicios"][i]["descuento"]["nuevo"] >= 0:
                datos["catalogo_servicios"][i]["descuento"]["nuevo"] = datos["catalogo_servicios"][i]["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", datos["catalogo_servicios"][i]["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios nuevos valido")
            
def mod_int_regular(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(datos["catalogo_servicios"][i]["descuento"]["regular"], int) and datos["catalogo_servicios"][i]["descuento"]["regular"] >= 0:
                datos["catalogo_servicios"][i]["descuento"]["regular"] = datos["catalogo_servicios"][i]["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", datos["catalogo_servicios"][i]["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios regulares valido")
            
def mod_int_leal(datos,i):
    while True:
        try:
            datos["catalogo_servicios"][i]["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(datos["catalogo_servicios"][i]["descuento"]["leal"], int) and datos["catalogo_servicios"][i]["descuento"]["leal"] >= 0:
                datos["catalogo_servicios"][i]["descuento"]["leal"] = datos["catalogo_servicios"][i]["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", datos["catalogo_servicios"][i]["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios leales valido")
            
def mod_int_descuento(datos,i):    
    while True:
        op = input("Ingrese el descuento:\n     0. Salir\n     1. Nuevo\n     2. Regular\n     3. Leal\n>>")
        if op == "1": 
            mod_int_nuevo(datos,i)
            print_(datos["catalogo_servicios"][i]["descuento"]["nuevo"],"modificado con éxito!")         
        elif op == "2":
            mod_int_regular(datos,i) 
            print_(datos["catalogo_servicios"][i]["descuento"]["regular"],"modificado con éxito!")
        elif op == "3":
            mod_int_leal(datos,i)
            print_(datos["catalogo_servicios"][i]["descuento"]["leal"],"modificado con éxito!")
        elif op == "0": return datos
        else:
            dm = "Error al registrar descuento"
            reportar_error_a_txt(dm)
            print_("El descuento no es valido")
            
def modificar(datos,i):    
    while True:
        op = input("Ingrese una opcion:\n    0. Salir \n    1. Referencia\n    2. Plan\n    3. Precio\n    4. Duracion\n    5. Descripcion\n    6. Cantidad Total\n    7. Cantidad Vendida\n    8. Descuento \n\n>>  ")
        if op == "1": 
            datos["catalogo_servicios"][i]["referencia"] = input("Ingrese la referencia nueva: ")
            print_(datos["catalogo_servicios"][i]["referencia"],"modificada con éxito!")                
        elif op == "2":
            datos["catalogo_servicios"][i]["plan"] = input("Ingrese el plan nuevo: ")                    
            print_(datos["catalogo_servicios"][i]["plan"],"modificado con éxito!")                
        elif op == "3":
            mod_int_precio(datos,i)
            print_(datos["catalogo_servicios"][i]["precio"],"modificado con éxito!")                   
        elif op == "4":
            datos["catalogo_servicios"][i]["duracion"] = input("Ingrese la duracion nueva: ")
            print_(datos["catalogo_servicios"][i]["duracion"],"modificado con éxito!")         
        elif op == "5": 
            datos["catalogo_servicios"][i]["descripcion"] = input("Ingrese la descripcion nueva: ")
            print_(datos["catalogo_servicios"][i]["descripcion"],"modificado con éxito!")         
        elif op == "6":
            mod_int_cantidad_total(datos,i)
            print_(datos["catalogo_servicios"][i]["cantidad_total"],"modificado con éxito!")         
        elif op == "7":
            mod_int_cantidad_vendida(datos,i)
            print_(datos["catalogo_servicios"][i]["cantidad_vendida"],"modificado con éxito!")         
        elif op == "8": mod_int_descuento(datos,i)
        elif op == "0": return datos        
        else:
            dm = "Error al registrar tipo_servicios"
            reportar_error_a_txt(dm)
            print_("Opcion no valida")
