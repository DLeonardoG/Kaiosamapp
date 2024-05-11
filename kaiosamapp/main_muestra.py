def mostrar_menu_principal():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

def mostrar_submenu_opcion1():
    print("SubMenu de la Opción 1")
    print("a. SubOpción 1")
    print("b. SubOpción 2")
    print("c. Volver al menú principal")

def mostrar_submenu_opcion2():
    print("SubMenu de la Opción 2")
    print("x. SubOpción X")
    print("y. SubOpción Y")
    print("z. Volver al menú principal")

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
