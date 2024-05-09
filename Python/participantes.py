def registrar_participante(datos):
    datos = dict(datos)
    participante={}
    participante["nombre"]=input("Ingrese el nombre: ")
    participante["documento"]=input("Ingrese el documento: ")
    participante["cargo"]=input("Ingrese el cargo: ")
    try:
        participante["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        participante["edad"] = 0
    print("Ingrese 1 si el participante paga o 2 de lo contrario")
    opc = -1
    try:
        opc = int(input("Ingrese la opcion: "))
    except Exception:
        opc = 2
    if opc == 1:
        participante["pago"] = True
    else:
        participante["pago"] = False
    
    datos["participantes"].append(participante)
    print("Participante registrado con éxito!")
    return datos

def eliminar_participante(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del participante: ")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["documento"] == documento:
            if datos["participantes"][i]["pago"] == False:
                datos["participantes"].pop(i)
                print("Participante eliminado!")
                return datos
            else:
                print("Ya perdió, y pagó!!")
                return datos
    print("Participante no existe")
    return datos
    
def pagar_participante(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del participante: ")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["documento"] == documento:
            if datos["participantes"][i]["pago"] == False:
                datos["participantes"][i]["pago"] = True
                print("Se pago la entrada del participante")
                return datos
            else:
                print("El participante ya habia pagado")
                return datos
    print("Participante no existe")
    return datos
    
def cuales_participantes_sin_pagar(datos):
    datos = dict(datos)
    print("Participantes que no han pagado:")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["pago"] == False:
            print(datos["participantes"][i]["nombre"], " - ", datos["participantes"][i]["documento"])
    
def cuantos_participantes_sin_pagar(datos):
    datos = dict(datos)
    cont = 0
    print("Participantes que no han pagado:")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["pago"] == False:
            cont += 1
    print(cont, " participantes no han pagado y la deuda total es de ", cont*50000)
    
def participantes_del_mes(datos):
    datos = dict(datos)
    print("Participantes del mes:")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["pago"] == True:
            print(datos["participantes"][i]["nombre"], " - ", datos["participantes"][i]["documento"])
    