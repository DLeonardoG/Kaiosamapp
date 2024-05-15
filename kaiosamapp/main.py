from importaciones import *
while True:
    clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Seleccione una opcion:\n👉   ")
    line()
    if op == "1":
        while True:
            clear_screen()
            mostrar_txt(m_1)
            op_m_1 = input("Seleccione una opcion:\n👉   ")
            line()
            if op_m_1 == "1":
                while True:                
                    print("Gestion de usuarios")                        
                    clear_screen()
                    mostrar_txt(m_1_1)
                    op_m_1_1 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_m_1_1 == "1": crear_usuario()
                    elif op_m_1_1 == "2": eliminar_usuario()
                    elif op_m_1_1 == "3": actualizar_usuario()               
                    elif op_m_1_1 == "4": leer_usuario()                           
                    elif op_m_1_1 == "0":
                        print("menu_anterior")                            
                        break
                    else: opcion_no_valida()
            elif op_m_1 == "2":
                while True:
                    print("pqr")
                    clear_screen()
                    mostrar_txt(m_1_2)
                    op_m_1_2 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_m_1_2 == "1": consultar_pqr()
                    elif op_m_1_2 == "2": registrar_pqr()
                    elif op_m_1_2 == "3": eliminar_pqr()
                    elif op_m_1_2 == "0":
                        print("menu_anterior")                            
                        break
                    else: opcion_no_valida()
                        
            elif op_m_1 == "3":
                while True:
                    print("Ventas")
                    clear_screen()
                    mostrar_txt(m_1_4)
                    op_m_1_4 = input("Seleccione una opcion:\n👉   ")
                    line()
                    if op_m_1_4 == "1":
                            print("catalogo_servicios")
                            clear_screen()
                            mostrar_txt(m_1_4_2)
                            op_m_1_4_2 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_m_1_4_2 == "1": crear_servicio()                                    
                            elif op_m_1_4_2 == "2": eliminar_servicio()
                            elif op_m_1_4_2 == "3": modificar_servicio()
                            elif op_m_1_4_2 == "4": consultar_servicio()
                            elif op_m_1_4_2 == "0":
                                print("menu_anterior")
                                break
                            else: opcion_no_valida()
                    elif op_m_1_4 == "2":
                        while True:
                            print("catalogo_productos")
                            clear_screen()
                            mostrar_txt(m_1_4_3)
                            op_m_1_4_3 = input("Seleccione una opcion:\n👉   ")
                            line()
                            if op_m_1_4_3 == "1": crear_producto()
                            elif op_m_1_4_3 == "2": eliminar_producto()
                            elif op_m_1_4_3 == "3": modificar_producto()
                            elif op_m_1_4_3 == "4": consultar_producto()
                            elif op_m_1_4_3 == "0":
                                print("menu_anterior")
                                break
                            else: opcion_no_valida() 
                        print("menu_anterior")        
                        break
                    elif op_m_1_4 == "3": print("vender_producto()")
                    elif op_m_1_4 == "0":
                        print("menu_anterior")                    
                        break
                    else: opcion_no_valida()
            elif op_m_1 == "0":
                print("menu_anterior")                    
                break
            else: opcion_no_valida()
    elif op == "0":
        clear_screen()
        diseño_logo()
        print_("Gracias Por entrar...")
        break
    else:
        opcion_no_valida()