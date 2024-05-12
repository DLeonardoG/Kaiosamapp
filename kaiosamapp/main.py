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
                    while True:
                        print("Gestion de usuarios")                        
                        break
                    mostrar_txt(m_1_1)
                    op_m_1_1 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_1 == "1":
                        while True:
                            crear_usuario()                          
                            break
                        
                    elif op_m_1_1 == "2":
                        
                        while True:
                            print("eliminar_usuario")                            
                            break
                        
                    elif op_m_1_1 == "3":
                        while True:
                            print("actualizar_usuario")                            
                            break
                        
                    elif op_m_1_1 == "4":
                        while True:
                            print("leer_usuario")                            
                            break
                            
                    elif op_m_1_1 == "5":
                        while True:
                            print("nueva_compra_usuario")                            
                            break
                        
                    elif op_m_1_1 == "6":
                        while True:
                            print("recomendaciones_usuario")                                
                            break
                        
                    elif op_m_1_1 == "0":
                        while True:
                            print("menu_anterior")                            
                            break
                        break
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "2":
                while True:
                    while True:
                        print("pqr")                        
                        break
                    mostrar_txt(m_1_2)
                    op_m_1_2 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_2 == "1":
                        while True:
                            print("consultar_pqr")                            
                            break
                        
                    elif op_m_1_2 == "2":
                        while True:
                            print("registrar_pqr")                            
                            break
                    elif op_m_1_2 == "3":
                        while True:
                            print("Eliminar_pqr")                            
                            break
                    
                    
                    elif op_m_1_2 == "0":
                        while True:
                            print("menu_anterior")                            
                            break
                        break

                        
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "3":
                while True:
                    while True:
                        print("Analisis de clientes")                        
                        break
                    mostrar_txt(m_1_3)
                    op_m_1_3 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_3 == "1":
                        while True:
                            print("Falta menu para analisis total o especifico")                            
                            break
                        while True:
                            print("analisis_general")                            
                            break
                    elif op_m_1_3 == "2":
                        while True:
                            print("analisis_cliente")                            
                            break
                    
                    
                    elif op_m_1_3 == "0":
                        while True:
                            print("menu_anterior")                            
                            break
                        break
                        
                    else:
                        opcion_no_valida()
                        
            elif op_m_1 == "4":
                while True:
                    while True:
                        print("Ventas")                        
                        break
                    mostrar_txt(m_1_4)
                    op_m_1_4 = input("Seleccione una opcion:\n👉   ")
                    if op_m_1_4 == "1":
                        while True:
                            print("factura_ventas")                            
                            break
                    elif op_m_1_4 == "2":
                        while True:
                            while True:
                                print("catalogo_servicios")                                
                                break
                            mostrar_txt(m_1_4_2)
                            op_m_1_4_2 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_2 == "1":
                                while True:
                                    print("crear_servicio")                                    
                                    break
                            elif op_m_1_4_2 == "2":
                                while True:
                                    print("eliminar_servicio")                                    
                                    break
                            elif op_m_1_4_2 == "3":
                                while True:
                                    print("modificar_servicio")                                    
                                    break
                            elif op_m_1_4_2 == "4":
                                while True:
                                    print("consultar_servicio")                                    
                                    break
                            elif op_m_1_4_2 == "0":
                                while True:
                                    print("menu_anterior")                                    
                                    break
                                break
                                
                            else:
                                opcion_no_valida()
                                
                    
                    elif op_m_1_4 == "3":
                        while True:
                            while True:
                                print("catalogo_productos")                                
                                break
                            mostrar_txt(m_1_4_3)
                            op_m_1_4_3 = input("Seleccione una opcion:\n👉   ")
                            if op_m_1_4_3 == "1":
                                while True:
                                    print("crear_producto")                                    
                                    break
                            elif op_m_1_4_3 == "2":
                                while True:
                                    print("eliminar_producto")                                    
                                    break
                            elif op_m_1_4_3 == "3":
                                while True:
                                    print("modificar_producto")                                    
                                    break
                            elif op_m_1_4_3 == "4":
                                while True:
                                    print("consultar_producto")                                    
                                    break
                            elif op_m_1_4_3 == "0":
                                while True:
                                    print("menu_anterior")                                    
                                    break
                                break
                            else:
                                opcion_no_valida()    
                    elif op_m_1_4 == "4":
                        while True:
                            print ("factura_usuario")                            
                            break
                    elif op_m_1_4 == "5":
                        while True:
                            print ("nueva_compra_usuario")                            
                            break
                
                
                    elif op_m_1_4 == "0":
                        while True:
                            print("menu_anterior")                            
                            break
                        break

                        
                    else:
                        opcion_no_valida()
            
            
            elif op_m_1 == "0":
                while True:
                    print("menu_anterior")                    
                    break
                break
            else:
                opcion_no_valida()
    
    elif op == "2":
        while True:
            print ("Menu de usuarios")            
            break
        op_2 = input("Ingrese una opción: ")
        while True:
            if op_2 == "1":
                while True:
                    print("Ha seleccionado Opción 1")                    
                    break
            elif op_2 == "2":
                while True:
                    print("Ha seleccionado Opción 2")                    
                    break
            elif op_2 == "3":
                while True:
                    print("Ha seleccionado Opción 3")                    
                    break
            elif op_2 == "4":
                while True:
                    print("Ha seleccionado Opción 4")                    
                    break
            
            
            elif op_2 == "0":
                while True:
                    print("menu_anterior")                    
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
