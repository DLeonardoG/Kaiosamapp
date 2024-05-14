from importaciones import *
while True:
    clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Ingrese una opción:\n👉  ")
    
    if op == "1":
        
        while True:
            #clear_screen()
            mostrar_txt(m_1)
            op_m_1 = input("Seleccione una opcion:\n👉   ")
            if op_m_1 == "1":
                while True:                
                    print("Gestion de usuarios")                        
                    mostrar_txt(m_1_1)
                    op_m_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_1 == "1": crear_usuario()
                    elif op_m_1_1 == "2": eliminar_usuario()
                    elif op_m_1_1 == "3": actualizar_usuario()               
                    elif op_m_1_1 == "4": leer_usuario()                            
                    elif op_m_1_1 == "5": print("nueva_compra_usuario")
                    elif op_m_1_1 == "6": print("recomendaciones_usuario")                                
                    elif op_m_1_1 == "0":
                        print("menu_anterior")                            
                        break
                    else: opcion_no_valida()
                        
            elif op_m_1 == "2":
                while True:
                    print("pqr")
                    mostrar_txt(m_1_2)
                    op_m_1_2 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_2 == "1": consultar_pqr()
                    elif op_m_1_2 == "2": registrar_pqr()
                    elif op_m_1_2 == "3": print("Eliminar_pqr")
                    elif op_m_1_2 == "0":
                        print("menu_anterior")                            
                        break
                    else: opcion_no_valida()
                        
            elif op_m_1 == "3":
                while True:
                    print("Analisis de clientes")
                    mostrar_txt(m_1_3)
                    op_m_1_3 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_3 == "1": 
                        print("Falta menu para analisis total o especifico")                            
                        print("analisis_general")
                    elif op_m_1_3 == "2": print("analisis_cliente")                            
                    elif op_m_1_3 == "0":
                        print("menu_anterior")
                        break
                    else: opcion_no_valida()
                        
            elif op_m_1 == "4":
                while True:
                    print("Ventas")
                    mostrar_txt(m_1_4)
                    op_m_1_4 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_4 == "1": print("factura_ventas")
                    elif op_m_1_4 == "2": 
                        while True:
                            print("catalogo_servicios")
                            mostrar_txt(m_1_4_2)
                            op_m_1_4_2 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_2 == "1": crear_servicio()                                    
                            elif op_m_1_4_2 == "2": eliminar_servicio()
                            elif op_m_1_4_2 == "3": modificar_servicio()
                            elif op_m_1_4_2 == "4": consultar_servicio()
                            elif op_m_1_4_2 == "0":
                                print("menu_anterior")
                                break
                            else: opcion_no_valida()
                    elif op_m_1_4 == "3":
                        while True:
                            print("catalogo_productos")
                            mostrar_txt(m_1_4_3)
                            op_m_1_4_3 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_3 == "1": crear_producto()
                            elif op_m_1_4_3 == "2": eliminar_producto()
                            elif op_m_1_4_3 == "3": modificar_producto()
                            elif op_m_1_4_3 == "4": consultar_producto()
                            elif op_m_1_4_3 == "0":
                                print("menu_anterior")
                                break
                            else: opcion_no_valida()    
                    elif op_m_1_4 == "4": print ("factura_usuario")
                    elif op_m_1_4 == "5": print ("nueva_compra_usuario")
                    elif op_m_1_4 == "0":
                        print("menu_anterior")        
                        break
                    else: opcion_no_valida()
            elif op_m_1 == "0":
                print("menu_anterior")                    
                break
            else: opcion_no_valida()
    elif op == "2": 
        print ("Menu de usuarios")
        op_2 = input("Ingrese una opción: ")
        while True:
            if op_2 == "1": print("Ha seleccionado Opción 1")
            elif op_2 == "2": print("Ha seleccionado Opción 2")
            elif op_2 == "3": print("Ha seleccionado Opción 3")
            elif op_2 == "4": print("Ha seleccionado Opción 4")                    
            elif op_2 == "0":
                print("menu_anterior")                    
                break
            else: opcion_no_valida()
    elif op == "0":
        clear_screen()
        diseño_logo()
        break
    else:
        opcion_no_valida()