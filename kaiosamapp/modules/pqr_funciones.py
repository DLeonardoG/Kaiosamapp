import csv
from modules.funciones_secundarias import reportar_error_a_txt

def int_id(pqr):
    while True:
        try:
            pqr["id"] = int(input("Ingrese el id: "))
            if isinstance(pqr["id"], int) and pqr["id"] > -1: 
                return pqr["id"]
            else: raise ValueError("id ", pqr["id"]," no es valido")
        except Exception as e:
            e = e,"Error al registrar id"
            reportar_error_a_txt(e)
            print("Ingrese un id valido")

def id_valido(pqr):    
    while True:
        int_id(pqr)
        cad = str(pqr["id"])
        if len(cad) == 5: return str(pqr["id"])
        else:
            dm = "Error al registrar id"
            reportar_error_a_txt(dm)
            print("El numero de id debe tener 5 digitos")
            pqr["id"] = ""
            
def tipo_pqr(pqr):    
    while True:
        
        
        op = input("Ingrese el tipo de PQR: \n    1. Pregunta\n    2. Queja\n    3. Reclamo\n    4. Sugerencia\n>>  ")
        if op == "1": 
            pqr["tipo_pqr"] = "pregunta"
            pqr["code_unico"] = "0013"
            break
        elif op == "2":
            pqr["tipo_pqr"] = "queja"
            pqr["code_unico"] = "0023"
            break
        elif op == "3":
            pqr["tipo_pqr"] = "reclamo"
            pqr["code_unico"] = "0033"
            break
        elif op == "4":
            pqr["tipo_pqr"] = "sugerencia"
            pqr["code_unico"] = "0043"
            break
        else:
            reportar_error_a_txt("Error al registrar tipo de PQR")
            print("Ingrese un tipo de PQR valido")
            pqr["tipo_pqr"] = ""
def contador_id():
    class idPQR:
        def __init__(self, archivo):
            self.archivo = archivo
            self.id_id = self.cargar_id()
        def cargar_id(self):
            try:
                with open(self.archivo, 'r') as f:
                    reader = csv.reader(f)
                    return int(next(reader)[0])
            except FileNotFoundError:
                return 0
        def guardar_id(self):
            with open(self.archivo, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(['{:05d}'.format(self.id_id)])
        def registrar_pqr(self):
            self.id_id += 1
            self.guardar_id()
        def obtener_id(self):
            return '{:06d}'.format(self.id_id)
    id = idPQR('id_pqr.csv')
    id.registrar_pqr()
    id_pqrs = id.obtener_id()
    return id_pqrs