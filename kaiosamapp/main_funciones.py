from modules.funciones_secundarias import fecha,os

def mostrar_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
        

#v = very()
#print(v) 