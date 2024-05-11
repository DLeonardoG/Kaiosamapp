from modules.txt_menus import *
from modules.funciones_secundarias import *

while True:
    clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        mostrar_txt(_1)
    
    elif opcion == "2":
        mostrar_txt(_2)
        
    elif opcion == "0":
        print("Saliendo del programa...")
