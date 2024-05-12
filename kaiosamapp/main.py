from importaciones import *

while True:
    #clear_screen()
    diseño_logo()
    mostrar_txt(principal)
    op = input("Ingrese una opción:\n👉  ")
    
    if op == "1":
        continuar_m_1_4_2 = input("Desea continuar?\n��  ")
        while True:
            #clear_screen()
            mostrar_txt(m_1)
            op_m_1 = input("Seleccione una opcion:\n👉   ")
            if op_m_1 == "1":                
                print("Gestion de usuarios")
                mostrar_txt(m_1_1)
                op_m_1_1 = input("Seleccione una opcion:\n👉   ")
                if op_m_1_1 == "1":
                    print("crear_usuario")
                    
                elif op_m_1_1 == "2":
                    print("eliminar_usuario")
                    
                elif op_m_1_1 == "3":
                    print("actualizar_usuario")
                    
                elif op_m_1_1 == "4":
                    print("leer_usuario")
                        
                elif op_m_1_1 == "5":
                    print("nueva_compra_usuario")
                    
                elif op_m_1_1 == "6":
                    print("recomendaciones_usuario")    
                    
                elif op_m_1_1 == "0":
                    print("menu_anterior")
                    
                elif op_m_1_1 == "00":
                    print("Volver al menu principal")
                    break
                else:
                    opcion_no_valida()
                        
            elif op_m_1 == "2":
                print("pqr")
                mostrar_txt(m_1_2)
                op_m_1_2 = input("Seleccione una opcion:\n👉   ")
                if op_m_1_2 == "1":
                    print("consultar_pqr")
                    
                elif op_m_1_2 == "2":
                    print("registrar_pqr")
                elif op_m_1_2 == "3":
                    print("Eliminar_pqr")
                
                
                elif op_m_1_2 == "0":
                    print("menu_anterior")


                elif op_m_1_2 == "00":
                    print("Volver al menu principal")
                    break
                else:
                    opcion_no_valida()
                        
            elif op_m_1 == "3":
                print("Analisis de clientes")
                mostrar_txt(m_1_3)
                op_m_1_3 = input("Seleccione una opcion:\n👉   ")
                if op_m_1_3 == "1":
                    print("Falta menu para analisis total o especifico")
                    print("analisis_general")
                elif op_m_1_3 == "2":
                    print("analisis_cliente")
                
                
                elif op_m_1_3 == "0":
                    print("menu_anterior")
                    
                elif op_m_1_3 == "00":
                    print("Volver al menu principal")
                    break
                else:
                    opcion_no_valida()
                    
            elif op_m_1 == "4":
                print("Ventas")
                mostrar_txt(m_1_4)
                op_m_1_4 = input("Seleccione una opcion:\n👉   ")
                if op_m_1_4 == "1":
                    print("factura_ventas")
                elif op_m_1_4 == "2":
                    print("catalogo_servicios")
                    
                    continuar_m_1_4_2 = True
                    while continuar_m_1_4_2 == True:
                        mostrar_txt(m_1_4_2)
                        op_m_1_4_2 = input("Seleccione una opcion:\n👉   ")
                        if op_m_1_4_2 == "1":
                            print("crear_servicio")
                        elif op_m_1_4_2 == "2":
                            print("eliminar_servicio")
                        elif op_m_1_4_2 == "3":
                            print("modificar_servicio")
                        elif op_m_1_4_2 == "4":
                            print("consultar_servicio")
                        elif op_m_1_4_2 == "0":
                            print("menu_anterior")
                            continuar_m_1_4_2 = False
                        elif op_m_1_4_2 == "00":
                            print("Volver al menu principal")
                            break
                        else:
                            opcion_no_valida()
                            continuar_m_1_4_2 = False
                    
                elif op_m_1_4 == "3":
                    print("catalogo_productos")
                elif op_m_1_4 == "4":
                    print ("factura_usuario")
                elif op_m_1_4 == "5":
                    print ("nueva_compra_usuario")
                
                
                elif op_m_1_4 == "0":
                    print("menu_anterior")

                elif op_m_1_4 == "00":
                    print("Volver al menu principal")
                    break
                else:
                    opcion_no_valida()
            
            
            elif op_m_1 == "0":
                print("menu_anterior")
                break
            else:
                opcion_no_valida()
    
    elif op == "2":
        print ("Menu de usuarios")
        op_2 = input("Ingrese una opción: ")
        while True:
            if op_2 == "1":
                print("Ha seleccionado Opción 1")
            elif op_2 == "2":
                print("Ha seleccionado Opción 2")
            elif op_2 == "3":
                print("Ha seleccionado Opción 3")
            elif op_2 == "4":
                print("Ha seleccionado Opción 4")
            
            
            elif op_2 == "0":
                print("menu_anterior")


            elif op_2 == "00":
                print("Volver al menu principal")
                break
            else:
                opcion_no_valida()
    elif op == "0":
        clear_screen()
        diseño_logo()
        print ("Saliendo del programa...")
        break
    else:
        opcion_no_valida()
