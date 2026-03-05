cambio = 3 #se utiliza el valor considerado por el profesor para el ejercicio
salir ="no"
while salir == "no":
    print("=====CONVERSOR DE MONEDAS=====")
    print("1. convertir soles a dolares")
    print("2. convertir dolares a soles")
    print("3. salir")
    opcion = input("Ingrese una opción (1-3): ")
    if opcion in ["1", "2"]:
        monto = float(input("Ingrese su monto: "))
        if opcion == "1":
            resultado = monto / cambio
            print(f"{monto} soles equivalen a {resultado:.2f} dólares")
            salir = input("¿Desea salir? (si/no): ")
        elif opcion == "2":
            resultado = monto * cambio
            print(f"{monto} dólares equivalen a {resultado:.2f} soles")
            salir = input("¿Desea salir? (si/no): ")
    elif opcion == "3":
            salir = "si"

    else:        
        print("Opción no válida. Por favor, ingrese una opción del 1 al 3.")