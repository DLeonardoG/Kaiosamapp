from datetime import datetime

fecha_y_hora = datetime.now()
fecha_y_hora = fecha_y_hora.replace(microsecond=0)
print(fecha_y_hora)