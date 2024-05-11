from datos_catalogo import *



def registrar_servicio(datos):
    datos = dict(datos)
    catalogo_servicios={}
    #try:
        #id =input("Ingrese el id del servicio: ")
        #for i in range(len(datos["catalogo_servicios"])):
            #if datos["catalogo_servicios"][i]["id"] == id:
                #print (datos["catalogo_servicios"][i]["id"])
                
        #catalogo_servicios["id"] = int(input("Ingrese el id: "))
        
    #except Exception as e:
        #reportar_error_a_txt(e)
        #catalogo_servicios["edad"] = 18
    catalogo_servicios["id"]=input("Ingrese el id: ")
    catalogo_servicios["tipo_servicios"]=input("Ingrese el tipo de servicio: ")
    catalogo_servicios["referencia"]=input("Ingrese la referencia: ")
    catalogo_servicios["plan"]=input("Ingrese el plan: ")
    catalogo_servicios["precio"]=input("Ingrese el precio: ")
    catalogo_servicios["duracion"]=input("Ingrese la duracion: ")
    
    datos["catalogo_servicios"].append(catalogo_servicios)
    print( catalogo_servicios["referencia"],catalogo_servicios["plan"],"registrado con éxito!")
    return datos
    
    


datos = cargar_datos(RUTA_BASE_DE_DATOS_CATALOGO)
datos = registrar_servicio(datos)
guardar_datos(datos, RUTA_BASE_DE_DATOS_CATALOGO)


