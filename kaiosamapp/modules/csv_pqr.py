import csv

RUTA_BASE_DE_DATOS_PQR = 'kaiosamapp/csv/pqr.csv'
def leer_csv(RUTA_BASE_DE_DATOS_PQR):
    with open(RUTA_BASE_DE_DATOS_PQR, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        nombres_columnas = next(lector_csv)
        columnas = [[] for _ in nombres_columnas]
        for fila in lector_csv:
            for i, valor in enumerate(fila):
                columnas[i].append(valor)
    for nombre_columna, columna in zip(nombres_columnas, columnas):
        print(f"{nombre_columna}: {columna}")

def buscar_csv(RUTA_BASE_DE_DATOS_PQR):
    valor_buscado = "2025"
    with open(RUTA_BASE_DE_DATOS_PQR, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if valor_buscado in fila:
                print(f"¡Encontrado! La fila que contiene '{valor_buscado}' es: {fila}")
                
buscar_csv(RUTA_BASE_DE_DATOS_PQR)

pqr =["0003", "12345", "servicio al cliente, reclamaciones y sugerencias.", "0013"-"0023"-"0033"-"0043","no me gusta","que mal servicio al cliente","92122" ]

def escribir_csv(RUTA_BASE_DE_DATOS_PQR,pqr):
    # Añadir los datos al archivo CSV
    with open(RUTA_BASE_DE_DATOS_PQR, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in pqr:
            escritor_csv.writerow(fila)

            
escribir_csv(RUTA_BASE_DE_DATOS_PQR,pqr)

