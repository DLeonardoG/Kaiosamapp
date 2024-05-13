import csv

def escribir_en_csv(ruta_archivo, datos):
    # Añadir los datos al archivo CSV
    with open(ruta_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(datos)

def leer_csv(ruta_archivo):
    # Leer el archivo CSV y devolver los datos como una lista de listas
    with open(ruta_archivo, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        return list(lector_csv)

def consultar_dato(ruta_archivo, fila, columna):
    # Leer el archivo CSV y devolver el dato en la fila y columna especificadas
    datos = leer_csv(ruta_archivo)
    return datos[fila][columna]

# Ejemplo de uso:

# Ruta al archivo CSV
ruta_archivo = 'datos.csv'

# Datos a añadir
pqr =["0003", "12345", "servicio al cliente, reclamaciones y sugerencias.", "0013"-"0023"-"0033"-"0043","no me gusta","que mal servicio al cliente","92122" ]
nuevos_datos = [["Pedro", 35, "Cusco"], ["Luisa", 28, "Trujillo"]]

# Añadir datos al archivo CSV
for datos in nuevos_datos:
    escribir_en_csv(ruta_archivo, datos)

# Consultar dato específico
dato = consultar_dato(ruta_archivo, fila=0, columna=1)
print("Dato en la fila 0, columna 1:", dato)

# Leer todos los datos del archivo CSV
datos = leer_csv(ruta_archivo)
print("Todos los datos en el archivo CSV:")
for fila in datos:
    print(fila)

# Aquí puedes realizar tus análisis sobre los datos, utilizando herramientas como pandas, numpy, etc.
