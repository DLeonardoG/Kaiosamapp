from modules.funciones_secundarias import fecha,os


def opcion_no_valida():
    ruta_errores = os.path.join("kaiosamapp/txt/errores.txt")
    with open(ruta_errores, 'a') as f:
        mensaje_error = f"{fecha}: Opcion de menu no valida" 
        f.write(mensaje_error + '\n')
#opcion_no_valida()


def mostrar_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
        
def very():
    while True:
        continuar = input("Desea continuar?\n1 . S i\n2 . N o\n��  ")
        if continuar == "1": 
            return True
        elif continuar == "2":
            return False
        else:
            opcion_no_valida()
#v = very()
#print(v) 