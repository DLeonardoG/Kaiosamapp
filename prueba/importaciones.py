                        #funcionamiento del main
from txt_menus import *
from main_funciones import *
from diseños import *
from funciones_secundarias import clear_screen
from funciones_secundarias import opcion_no_valida

#funcionamiento interno del main
                        #Gestion usuarios
from datos import *
from gestion_usuarios import crear_usuario,eliminar_usuario
from gestion_usuarios import actualizar_usuario,leer_usuario,nueva_compra_usuario

                        #Gestion PQRS
from pqr import registrar_pqr,consultar_pqr,eliminar_pqr
                        #Gestion ventas
#from catalogo_productos import vender_producto
                        #Gstion catalogo 
#Gestion servicios
from catalogo_servicios import crear_servicio,eliminar_servicio,mostrar_servicios
from catalogo_servicios import modificar_servicio,consultar_servicio,mostrar_tipos_servicios
#Gestion productos
from catalogo_productos import crear_producto,eliminar_producto,mostrar_tipos_productos
from catalogo_productos import modificar_producto,consultar_producto,mostrar_productos