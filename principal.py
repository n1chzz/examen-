import libreria as lb
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion=input("Ingrese opción: ")
        if opcion=="1":
            marca=input("Ingrese marca a consultar: ")
            lb.stock_marca(marca)
        elif opcion=="2":
            while True:
                try:
                    p_min=int(input("Ingrese precio mínimo: "))
                    p_max=int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            lb.busqueda_precio(p_min, p_max)
        elif opcion=="3":
            while True:
                modelo=input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio=int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un valor entero para el precio.")
                    continue
                resultado=lb.actualizar_precio(modelo, nuevo_precio)
                if resultado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                repetir=input("¿Desea actualizar otro precio(si/no)?: ").lower()
                if repetir!="si":
                    break
        elif opcion=="4":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")
menu()
