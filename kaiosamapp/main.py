from importaciones import *

while True:
    #clear_screen()
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
                    while True:
                        print("Gestion de usuarios")                        
                        veri = very()
                        if veri == True:
                            clear_screen()                            
                        else:    
                            break
                    mostrar_txt(m_1_1)
                    op_m_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_1 == "1":
                        while True:
                            print("crear_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_1 == "2":
                        
                        while True:
                            print("eliminar_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_1 == "3":
                        while True:
                            print("actualizar_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_1 == "4":
                        while True:
                            print("leer_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                            
                    elif op_m_1_1 == "5":
                        while True:
                            print("nueva_compra_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_1 == "6":
                        while True:
                            print("recomendaciones_usuario")                                
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_1 == "0":
                        while True:
                            print("menu_anterior")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        break
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "2":
                while True:
                    while True:
                        print("pqr")                        
                        veri = very()
                        if veri == True:
                            clear_screen()                            
                        else:    
                            break
                    mostrar_txt(m_1_2)
                    op_m_1_2 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_2 == "1":
                        while True:
                            print("consultar_pqr")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        
                    elif op_m_1_2 == "2":
                        while True:
                            print("registrar_pqr")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    elif op_m_1_2 == "3":
                        while True:
                            print("Eliminar_pqr")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    
                    
                    elif op_m_1_2 == "0":
                        while True:
                            print("menu_anterior")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        break

                        
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "3":
                while True:
                    while True:
                        print("Analisis de clientes")                        
                        veri = very()
                        if veri == True:
                            clear_screen()                            
                        else:    
                            break
                    mostrar_txt(m_1_3)
                    op_m_1_3 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_3 == "1":
                        while True:
                            print("Falta menu para analisis total o especifico")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        while True:
                            print("analisis_general")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    elif op_m_1_3 == "2":
                        while True:
                            print("analisis_cliente")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    
                    
                    elif op_m_1_3 == "0":
                        while True:
                            print("menu_anterior")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        break
                        
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "4":
                while True:
                    while True:
                        print("Ventas")                        
                        veri = very()
                        if veri == True:
                            clear_screen()                            
                        else:    
                            break
                    mostrar_txt(m_1_4)
                    op_m_1_4 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_4 == "1":
                        while True:
                            print("factura_ventas")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    elif op_m_1_4 == "2":
                        while True:
                            while True:
                                print("catalogo_servicios")                                
                                veri = very()
                                if veri == True:
                                    clear_screen()                                    
                                else:    
                                    break
                            mostrar_txt(m_1_4_2)
                            op_m_1_4_2 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_2 == "1":
                                while True:
                                    print("crear_servicio")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_2 == "2":
                                while True:
                                    print("eliminar_servicio")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_2 == "3":
                                while True:
                                    print("modificar_servicio")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_2 == "4":
                                while True:
                                    print("consultar_servicio")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_2 == "0":
                                while True:
                                    print("menu_anterior")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                                break
                                
                            else:
                                opcion_no_valida()
                                
                    
                    elif op_m_1_4 == "3":
                        while True:
                            while True:
                                print("catalogo_productos")                                
                                veri = very()
                                if veri == True:
                                    clear_screen()                                    
                                else:    
                                    break
                            mostrar_txt(m_1_4_3)
                            op_m_1_4_3 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_3 == "1":
                                while True:
                                    print("crear_producto")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_3 == "2":
                                while True:
                                    print("eliminar_producto")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_3 == "3":
                                while True:
                                    print("modificar_producto")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_3 == "4":
                                while True:
                                    print("consultar_producto")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                            elif op_m_1_4_3 == "0":
                                while True:
                                    print("menu_anterior")                                    
                                    veri = very()
                                    if veri == True:
                                        clear_screen()                                        
                                    else:    
                                        break
                                break
                            else:
                                opcion_no_valida()    
                    elif op_m_1_4 == "4":
                        while True:
                            print ("factura_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                    elif op_m_1_4 == "5":
                        while True:
                            print ("nueva_compra_usuario")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                
                
                    elif op_m_1_4 == "0":
                        while True:
                            print("menu_anterior")                            
                            veri = very()
                            if veri == True:
                                clear_screen()                                
                            else:    
                                break
                        break

                        
                    else:
                        opcion_no_valida()
            
            
            elif op_m_1 == "0":
                while True:
                    print("menu_anterior")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break
                break
            else:
                opcion_no_valida()
    
    elif op == "2":
        while True:
            print ("Menu de usuarios")            
            veri = very()
            if veri == True:
                clear_screen()                
            else:    
                break
        op_2 = input("Ingrese una opción: ")
        while True:
            if op_2 == "1":
                while True:
                    print("Ha seleccionado Opción 1")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break
            elif op_2 == "2":
                while True:
                    print("Ha seleccionado Opción 2")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break
            elif op_2 == "3":
                while True:
                    print("Ha seleccionado Opción 3")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break
            elif op_2 == "4":
                while True:
                    print("Ha seleccionado Opción 4")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break
            
            
            elif op_2 == "0":
                while True:
                    print("menu_anterior")                    
                    veri = very()
                    if veri == True:
                        clear_screen()                        
                    else:    
                        break


                break
            else:
                opcion_no_valida()
    elif op == "0":
        clear_screen()
        diseño_logo()
        break
    else:
        opcion_no_valida()
