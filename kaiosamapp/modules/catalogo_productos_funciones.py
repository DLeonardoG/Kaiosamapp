from modules.funciones_secundarias import reportar_error_a_txt,opcion_no_valida,print_
from modules.funciones_secundarias import line
def int_id(catalogo_productos):
    while True:
        try:
            catalogo_productos["id"] = int(input("Ingrese el id: "))
            if isinstance(catalogo_productos["id"], int) and catalogo_productos["id"] > -1: 
                return catalogo_productos["id"]
            else: raise ValueError("id ", catalogo_productos["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print_("Ingrese un id valido")
            
def id_valido(catalogo_productos):    
    while True:
        int_id(catalogo_productos)
        cad = str(catalogo_productos["id"])
        if len(cad) == 5: return str(catalogo_productos["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print_("El numero de id debe tener 5 digitos")
            catalogo_productos["id"] = ""
            
def int_modelo(catalogo_productos,name):
    while True:
        try:
            modelo = int(input("Ingrese el modelo de ",name,": "))
            if modelo >= 2018: 
                catalogo_productos["caracteristicas"]["modelo"] = str(modelo)
                break
            else: 
                raise ValueError("El modelo de ",name, catalogo_productos["caracteristicas"]["modelo"]," no es valido")
        except Exception as e:
            e = (e,"Error al registrar modelo de ",name)
            reportar_error_a_txt(e)
            print_("Ingrese un modelo de ",name," valido")
            
def tipo_productos(catalogo_productos):    
    while True:
        op = input("Ingrese el tipo de Kame producto: \n    1. Kame celular\n    2. kame tv\n    3. kame computador\n>>    ")
        if op == "1": 
            catalogo_productos["tipo_productos"] = "kame_celular"
            catalogo_productos["caracteristicas"]={"color":"negro", "memoria":"128G", "generacion":"5G", "camara": "48 MP", "resolucion":"2.778 x 1.284 píxeles", "bateria":"4.383 mah"}
            catalogo_productos["caracteristicas"]["color"] = input("Ingrese el color (o colores disponibles) del kame celular: ")
            catalogo_productos["caracteristicas"]["memoria"] = input("Ingrese la memoria del kame celular: ")
            catalogo_productos["caracteristicas"]["generacion"] = input("Ingrese la generacion del kame celular: ")
            catalogo_productos["caracteristicas"]["camara"] = input("Ingrese la camara del kame celular: ")
            catalogo_productos["caracteristicas"]["resolucion"] = input("Ingrese la resolucion del kame celular: ")
            catalogo_productos["caracteristicas"]["bateria"] = input("Ingrese la bateria del kame celular: ")
            name = "kame celular"
            #int_modelo(catalogo_productos,name)
            catalogo_productos["code_unico"] = "0012"
            break
        elif op == "2":
            catalogo_productos["tipo_productos"] = "kame_tv"
            catalogo_productos["caracteristicas"]={"resolucion":"Full HD", "pulgadas":"40", "smart_tv":"si", "modelo":"2024"}
            catalogo_productos["caracteristicas"]["resolucion"] = input("Ingrese la resolucion del kame TV: ")                 
            catalogo_productos["caracteristicas"]["pulgadas"] = input("Ingrese las pulgadas del kame TV: ")
            while True:
                smart_tv = input("¿Es Smart TV?\n    1 . Si\n    2 . No\n��  ")
                if smart_tv == "1": 
                    smart_tv = "si"
                    break
                elif smart_tv == "2": 
                    smart_tv = "no"
                    break
                else: opcion_no_valida()     
            catalogo_productos["caracteristicas"]["smart_tv"] = smart_tv
            while True:
                voice = input("¿El kame TV tiene comando de voice?\n    1 . Si\n    2 . No\n��  ")
                if voice == "1": 
                    voice = "si"
                    break
                elif voice == "2": 
                    voice = "no"
                    break
                else: opcion_no_valida()     
            catalogo_productos["caracteristicas"]["voice"] = voice
            name = "kame TV"
            #int_modelo(catalogo_productos,name)
            catalogo_productos["code_unico"] = "0022"
            break
        elif op == "3":
            catalogo_productos["tipo_productos"] = "kame_computador"  
            catalogo_productos["caracteristicas"]={"color":"azul", "memoria":"1tb ", "ram":"Ram 24gb", "generacion":"Intel Core I9", "pantalla":"full hd 14 pulg(35.6 cm)", "procesador":"13 ","bateria": "13900h"}
            catalogo_productos["caracteristicas"]["color"] = input("Ingrese el color (o colores disponibles) del kame computador: ")
            catalogo_productos["caracteristicas"]["memoria"] = input("Ingrese la memoria del kame computador: ")
            catalogo_productos["caracteristicas"]["ram"] = input("Ingrese la ram del kame computador: ")
            catalogo_productos["caracteristicas"]["generacion"] = input("Ingrese la generacion del kame computador: ")
            catalogo_productos["caracteristicas"]["pantalla"] = input("Ingrese las caracteristicas de la pantalla del kame computador (Full HD 14 pulg,(35.6 cm)): ")
            catalogo_productos["caracteristicas"]["procesador"] = input("Ingrese el procesador kame computador: ")
            catalogo_productos["caracteristicas"]["bateria"] = input("Ingrese el procesador kame computador: ")
            name = "kame computador"
            #int_modelo(catalogo_productos,name)
            catalogo_productos["code_unico"] = "0032"            
            break
        else:
            dm = "Error al registrar tipo_productos"
            reportar_error_a_txt(dm)
            print_("La opcion no es valida")
            catalogo_productos["tipo_productos"] = ""  
            
def kame_celular(datos_catalogo):
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["code_unico"] == "0012":
            line()
            print_(datos_catalogo["catalogo_productos"][i]["tipo_productos"])
            line()
            print_(datos_catalogo["catalogo_productos"][i]["id"] + "  -   Id")
            print_(datos_catalogo["catalogo_productos"][i]["referencia"], "  -   Referencia")
            print_(datos_catalogo["catalogo_productos"][i]["marca"], "  -   Marca")
            print_(datos_catalogo["catalogo_productos"][i]["precio"], "  -   Precio")
            print_(datos_catalogo["catalogo_productos"][i]["garantia"], "  -   Garantia")
            print_(datos_catalogo["catalogo_productos"][i]["descripcion"], " - Descripcion")
            print_(datos_catalogo["catalogo_productos"][i]["cantidad_total"], "  -   Cantidad Total")
            line()
            print_("----  Caracteristicas ----")
            line()
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["color"] , "  -   Color")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["memoria"] , "  -   Memoria")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["generacion"], "  -   Generacion")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["camara"], "  -   Camara")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["resolucion"], "  -   Resolucion")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["bateria"], "  -   Bateria")
            line()
    return datos_catalogo
            
def kame_tv(datos_catalogo):
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["code_unico"] == "0022":
            line()
            print_(datos_catalogo["catalogo_productos"][i]["tipo_productos"])
            line()
            print_(datos_catalogo["catalogo_productos"][i]["id"] + "  -   Id")
            print_(datos_catalogo["catalogo_productos"][i]["referencia"], "  -   Referencia")
            print_(datos_catalogo["catalogo_productos"][i]["marca"], "  -   Marca")
            print_(datos_catalogo["catalogo_productos"][i]["precio"], "  -   Precio")
            print_(datos_catalogo["catalogo_productos"][i]["garantia"], "  -   Garantia")
            print_(datos_catalogo["catalogo_productos"][i]["descripcion"], " - Descripcion")
            print_(datos_catalogo["catalogo_productos"][i]["cantidad_total"], "  -   Cantidad Total")
            line()
            print_("----  Caracteristicas ----")
            line()
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["resolucion"], "  -   Resolucion")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["pulgadas"], "  -   Pulgadas")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["smart_tv"], "  -   Smart TV")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["modelo"], "  -   Modelo")
            line()
    return datos_catalogo

def kame_computador(datos_catalogo):
    for i in range(len(datos_catalogo["catalogo_productos"])):
        if datos_catalogo["catalogo_productos"][i]["code_unico"] == "0032":
            line()
            print_(datos_catalogo["catalogo_productos"][i]["tipo_productos"])
            line()
            print_(datos_catalogo["catalogo_productos"][i]["id"] + "  -   Id")
            print_(datos_catalogo["catalogo_productos"][i]["referencia"], "  -   Referencia")
            print_(datos_catalogo["catalogo_productos"][i]["marca"], "  -   Marca")
            print_(datos_catalogo["catalogo_productos"][i]["precio"], "  -   Precio")
            print_(datos_catalogo["catalogo_productos"][i]["garantia"], "  -   Garantia")
            print_(datos_catalogo["catalogo_productos"][i]["descripcion"], " - Descripcion")
            print_(datos_catalogo["catalogo_productos"][i]["cantidad_total"], "  -   Cantidad Total")
            line()
            print_("----  Caracteristicas ----")
            line()
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["color"], "  -   Color")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["memoria"], " -   Memoria")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["generacion"], " -   Generacion")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["ram"] , " -   Ram")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["pantalla"], " -   Pantalla")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["procesador"], "  -   Procesador")
            print_(datos_catalogo["catalogo_productos"][i]["caracteristicas"]["bateria"], " -   Bateria")
            line()
    return datos_catalogo

def mostrar_tipo_productos(datos_catalogo):    
    while True:
        line()
        op = input("Ingrese el tipo de Kame producto: \n    0. Salir\n    1. Kame celular\n    2. kame tv\n    3. kame computador\n>>    ")
        line()
        if op == "1": 
            kame_celular(datos_catalogo)
        elif op == "2":
            kame_tv(datos_catalogo)
        elif op == "3":
            kame_computador(datos_catalogo)
        elif op == "0":
            line()
            print_("Regresando...")
            line()
            return datos_catalogo
        else:
            dm = "Error al registrar tipo_productos"
            reportar_error_a_txt(dm)
            print_("El tipo de servicio no es valido")
            

            
def int_precio(catalogo_productos):
    while True:
        try:
            catalogo_productos["precio"] = int(input("Ingrese el precio: "))
            if isinstance(catalogo_productos["precio"], int) and catalogo_productos["precio"] >= 1000: 
                catalogo_productos["precio"] = catalogo_productos["precio"]
                break
            else: raise ValueError("precio ", catalogo_productos["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print_("Ingrese un precio valido")
            
def int_nuevo(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(catalogo_productos["descuento"]["nuevo"], int) and catalogo_productos["descuento"]["nuevo"] >= 0:
                catalogo_productos["descuento"]["nuevo"] = catalogo_productos["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", catalogo_productos["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios nuevos valido")
            
def int_regular(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(catalogo_productos["descuento"]["regular"], int) and catalogo_productos["descuento"]["regular"] >= 0:
                catalogo_productos["descuento"]["regular"] = catalogo_productos["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", catalogo_productos["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios regulares valido")
            
def int_leal(catalogo_productos):
    while True:
        try:
            catalogo_productos["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(catalogo_productos["descuento"]["leal"], int) and catalogo_productos["descuento"]["leal"] >= 0:
                catalogo_productos["descuento"]["leal"] = catalogo_productos["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", catalogo_productos["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios leales valido")
            
def int_cantidad_total(catalogo_productos):
    while True:
        try:
            catalogo_productos["cantidad_total"] = int(input("Ingrese la catidad total: "))
            if isinstance(catalogo_productos["cantidad_total"], int) and catalogo_productos["cantidad_total"] > 0: 
                catalogo_productos["cantidad_total"] = catalogo_productos["cantidad_total"]
                break
            else: raise ValueError("La cantidad total ", catalogo_productos["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad total valida")
            
def mod_int_precio(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["precio"] = int(input("Ingrese el precio nuevo: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["precio"], int) and datos_catalogo["catalogo_productos"][i]["precio"] >= 0:
                datos_catalogo["catalogo_productos"][i]["precio"] = datos_catalogo["catalogo_productos"][i]["precio"]
                return datos_catalogo 
            else: raise ValueError("precio ", datos_catalogo["catalogo_productos"][i]["precio"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar precio"
            reportar_error_a_txt(e)
            print_("Ingrese un precio valido")
            
def mod_int_cantidad_total(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["cantidad_total"] = int(input("Ingrese la catidad total nueva: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["cantidad_total"], int) and datos_catalogo["catalogo_productos"][i]["cantidad_total"] >= 0: 
                datos_catalogo["catalogo_productos"][i]["cantidad_total"] = datos_catalogo["catalogo_productos"][i]["cantidad_total"]
                return datos_catalogo                    
            else: raise ValueError("La cantidad total ", datos_catalogo["catalogo_productos"][i]["cantidad_total"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad total"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad total valida")
            
def mod_int_cantidad_vendida(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["cantidad_vendida"] = int(input("Ingrese la catidad vendida nueva: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["cantidad_vendida"], int) and datos_catalogo["catalogo_productos"][i]["cantidad_vendida"] >= 0:
                datos_catalogo["catalogo_productos"][i]["cantidad_vendida"] = datos_catalogo["catalogo_productos"][i]["cantidad_vendida"]
                return datos_catalogo                    
            else: raise ValueError("La cantidad vendida ", datos_catalogo["catalogo_productos"][i]["cantidad_vendida"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar cantidad vendida"
            reportar_error_a_txt(e)
            print_("Ingrese una cantidad vendida valida")
            
def mod_int_nuevo(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"] = int(input("Ingrese el descuento para usuarios nuevos: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"], int) and datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"] >= 0:
                datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"] = datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"]
                break
            else: raise ValueError("El descuento para usuarios nuevos ", datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios nuevos"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios nuevos valido")
            
def mod_int_regular(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["descuento"]["regular"] = int(input("Ingrese el descuento para usuarios regulares: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["descuento"]["regular"], int) and datos_catalogo["catalogo_productos"][i]["descuento"]["regular"] >= 0: 
                datos_catalogo["catalogo_productos"][i]["descuento"]["regular"] = datos_catalogo["catalogo_productos"][i]["descuento"]["regular"]
                break
            else: raise ValueError("El descuento para usuarios regulares ", datos_catalogo["catalogo_productos"][i]["descuento"]["regular"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios regulares"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios regulares valido")
            
def mod_int_leal(datos_catalogo,i):
    while True:
        try:
            datos_catalogo["catalogo_productos"][i]["descuento"]["leal"] = int(input("Ingrese el descuento para usuarios leales: "))
            if isinstance(datos_catalogo["catalogo_productos"][i]["descuento"]["leal"], int) and datos_catalogo["catalogo_productos"][i]["descuento"]["leal"] >= 0: 
                datos_catalogo["catalogo_productos"][i]["descuento"]["leal"] = datos_catalogo["catalogo_productos"][i]["descuento"]["leal"]
                break
            else: raise ValueError("El descuento para usuarios leales ", datos_catalogo["catalogo_productos"][i]["descuento"]["leal"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar descuento para usuarios leales"
            reportar_error_a_txt(e)
            print_("Ingrese un descuento para usuarios leales valido")
            
def mod_int_descuento(datos_catalogo,i):    
    while True:
        op = input("Ingrese el descuento:\n     0. Salir\n     1. Nuevo\n     2. Regular\n     3. Leal\n>>")
        if op == "1": 
            mod_int_nuevo(datos_catalogo,i)
            print_(datos_catalogo["catalogo_productos"][i]["descuento"]["nuevo"],"modificado con éxito!")         
        elif op == "2":
            mod_int_regular(datos_catalogo,i) 
            print_(datos_catalogo["catalogo_productos"][i]["descuento"]["regular"],"modificado con éxito!")
        elif op == "3":
            mod_int_leal(datos_catalogo,i)
            print_(datos_catalogo["catalogo_productos"][i]["descuento"]["leal"],"modificado con éxito!")
        elif op == "0": return datos_catalogo
        else:
            dm = "Error al registrar descuento"
            reportar_error_a_txt(dm)
            print_("El descuento no es valido")
            
def modificar(datos_catalogo,i):    
    while True:
        op = input("Ingrese una opcion:\n    0. Salir \n    1. Referencia\n    2. Plan\n    3. Precio\n    4. Duracion\n    5. Descripcion\n    6. Cantidad Total\n    7. Cantidad Vendida\n    8. Descuento \n\n>>  ")
        if op == "1": 
            datos_catalogo["catalogo_productos"][i]["referencia"] = input("Ingrese la referencia nueva: ")
            print_(datos_catalogo["catalogo_productos"][i]["referencia"],"modificada con éxito!")                
        elif op == "2":
            datos_catalogo["catalogo_productos"][i]["plan"] = input("Ingrese el plan nuevo: ")                    
            print_(datos_catalogo["catalogo_productos"][i]["plan"],"modificado con éxito!")                
        elif op == "3":
            mod_int_precio(datos_catalogo,i)
            print_(datos_catalogo["catalogo_productos"][i]["precio"],"modificado con éxito!")                   
        elif op == "4":
            datos_catalogo["catalogo_productos"][i]["duracion"] = input("Ingrese la duracion nueva: ")
            print_(datos_catalogo["catalogo_productos"][i]["duracion"],"modificado con éxito!")         
        elif op == "5": 
            datos_catalogo["catalogo_productos"][i]["descripcion"] = input("Ingrese la descripcion nueva: ")
            print_(datos_catalogo["catalogo_productos"][i]["descripcion"],"modificado con éxito!")         
        elif op == "6":
            mod_int_cantidad_total(datos_catalogo,i)
            print_(datos_catalogo["catalogo_productos"][i]["cantidad_total"],"modificado con éxito!")         
        elif op == "7":
            mod_int_cantidad_vendida(datos_catalogo,i)
            print_(datos_catalogo["catalogo_productos"][i]["cantidad_vendida"],"modificado con éxito!")         
        elif op == "8": mod_int_descuento(datos_catalogo,i)
        elif op == "0": return datos_catalogo        
        else:
            dm = "Error al registrar tipo_productos"
            reportar_error_a_txt(dm)
            print_("Opcion no valida")
