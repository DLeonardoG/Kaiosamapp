                        #funcionamiento del main
from txt_menus import *
from main_funciones import *
from diseños import *
from modules.funciones_secundarias import clear_screen
from modules.funciones_secundarias import opcion_no_valida

#funcionamiento interno del main
                        #Gestion usuarios
from modules.datos_users import *
from modules.gestion_usuarios import crear_usuario,eliminar_usuario
from modules.gestion_usuarios import actualizar_usuario,leer_usuario,nueva_compra_usuario

                        #Gestion PQRS
from modules.pqr import registrar_pqr,consultar_pqr,eliminar_pqr
                        #Gestion ventas

                        #Gstion catalogo 
#Gestion servicios
from modules.catalogo_servicios import crear_servicio,eliminar_servicio,mostrar_servicios
from modules.catalogo_servicios import modificar_servicio,consultar_servicio,mostrar_tipos_servicios
#Gestion productos
from modules.catalogo_productos import crear_producto,eliminar_producto,mostrar_tipos_productos
from modules.catalogo_productos import modificar_producto,consultar_producto,mostrar_productos