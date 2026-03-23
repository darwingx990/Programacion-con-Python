while True:
    print("_-------MENU ITERACTIVO----------")
    print("""
          1. Menu de comidas
          2. Menu de bebidas
          3. Menu de pago
          4. Salir
          """
    )
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 4:
        print("Gracias por utilizar nuestros servicios.")
        break
