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
        if len(cad) == 5: return catalogo_servicios["id"]
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print("El numero de id debe tener 5 digitos")
            catalogo_servicios["id"] = ""