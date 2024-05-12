def mostrar_menu_principal():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

def mostrar_submenu_opcion1():
    print("SubMenu de la Opción 1")
    print("a. SubOpción 1")
    print("b. SubOpción 2")
    print("c. Otra subopción")
    print("d. Volver al menú principal")

def mostrar_submenu_opcion2():
    print("SubMenu de la Opción 2")
    print("x. SubOpción X")
    print("y. SubOpción Y")
    print("z. Volver al menú principal")

def mostrar_otro_submenu_opcion1():
    print("Otro SubMenu de la Opción 1")
    print("1. SubOpción A")
    print("2. SubOpción B")
    print("3. Volver al submenú anterior")

while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            mostrar_submenu_opcion1()
            subopcion = input("Seleccione una opción del submenú: ")
            if subopcion == "a":
                print("Ha seleccionado SubOpción 1")
            elif subopcion == "b":
                print("Ha seleccionado SubOpción 2")
            elif subopcion == "c":
                while True:
                    mostrar_otro_submenu_opcion1()
                    otra_subopcion = input("Seleccione una opción del otro submenú: ")
                    if otra_subopcion == "1":
                        print("Ha seleccionado SubOpción A")
                    elif otra_subopcion == "2":
                        print("Ha seleccionado SubOpción B")
                    elif otra_subopcion == "3":
                        break
                    else:
                        print("Opción no válida")
            elif subopcion == "d":
                break
            else:
                print("Opción no válida")
    
    elif opcion == "2":
        while True:
            mostrar_submenu_opcion2()
            subopcion = input("Seleccione una opción del submenú: ")
            if subopcion == "x":
                print("Ha seleccionado SubOpción X")
            elif subopcion == "y":
                print("Ha seleccionado SubOpción Y")
            elif subopcion == "z":
                break
            else:
                print("Opción no válida")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")
