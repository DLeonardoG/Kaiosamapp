def menu_principal():
    print("***************************************")
    print("Ingrese la opción que requiera")
    print("1. para registrar un participante")
    print("2. para eliminar un participante")
    print("3. para pagar la entrada de un participante")
    print("4. para registrar un evento")
    print("5. para modificar un evento")
    print("6. para marcar un evento como finalizado")
    print("7. para saber cuales participantes no han pagado")
    print("8. para saber cuantos participantes no han pagado")
    print("9. para conocer eventos del mes")
    print("10. para conocer participantes del mes")
    print("11. para salir")
    print("***************************************")
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1