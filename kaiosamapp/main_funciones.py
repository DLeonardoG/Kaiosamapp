from modules.funciones_secundarias import fecha,os,line

def mostrar_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        line()
        print(contenido)
        line()
        

#v = very()
#print(v) 