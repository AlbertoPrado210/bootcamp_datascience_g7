salir ="no"
while salir != "si":
    print("=====OPCIONES=====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. tabla de multiplicar")
    print("6. raiz cuadrada")
    print("7. Salir")
    opcion = input("Ingrese una opción (1-7): ")
    if opcion in ["1", "2", "3", "4"]:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        if opcion == "1":
            resultado = num1 + num2
            print(f"La suma de {num1} y {num2} es: {resultado}")
            salir = not input("¿Desea continuar? (si/no): ")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"La resta de {num1} y {num2} es: {resultado}")
            salir = not input("¿Desea continuar? (si/no): ")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"La multiplicación de {num1} y {num2} es: {resultado}")
            salir = not input("¿Desea continuar? (si/no): ")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"La división de {num1} entre {num2} es: {resultado}")
                salir = not input("¿Desea continuar? (si/no): ")
            else:
                print("Error: No se puede dividir por cero.")
                salir = not input("¿Desea continuar? (si/no): ")
    else:        
        num1 = int(input("Ingrese un número: ")) 
        if opcion == "5":
            print(f"Tabla de multiplicar del {num1}:")
            for i in range(1, 13):
                print(f"{num1} x {i} = {num1 * i}")
            salir = not input("¿Desea continuar? (si/no): ")
        elif opcion == "6":
            if num1 >= 0:
                resultado = num1 ** 0.5
                print(f"La raíz cuadrada de {num1} es: {resultado}")
                salir = not input("¿Desea continuar? (si/no): ")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
                salir = not input("¿Desea continuar? (si/no): ")
        elif opcion == "7":
            salir = input("¿esta seguro de salir? (si/no): ")