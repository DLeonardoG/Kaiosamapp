

def registrar_evento(datos):
    datos = dict(datos)
    eventos={}
    eventos["nombre"]=input("Ingrese el nombre: ")
    eventos["locacion"]=input("Ingrese el documento: ")
    eventos["dia"]=input("Ingrese el dia: ")

    datos["eventos"].append(eventos)
    print("eventos registrado con éxito!")
    return datos

def eliminar_evento(datos):
    datos = dict(datos)
    nombre =input("Ingrese el nombre del evento: ")
    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["nombre"] == nombre:
            datos["eventos"].pop(i)
            print("evento eliminado!")
            return datos
    print("evento no existe")
    return datos

def buscando_evento(datos):
    datos = dict(datos)
    nombre =input("nombre del evento: ")
    evento={}
    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["nombre"] == nombre:
            evento=datos["eventos"][i]
            break
    return evento
    
def asignacion_evento(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del participante: ")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["documento"] == documento:
            datos["participantes"][i]["eventos"]=[]
            datos["participantes"][i]["eventos"].append(buscando_evento(datos))
            print(datos["participantes"][i]["eventos"])
            break
    return datos



