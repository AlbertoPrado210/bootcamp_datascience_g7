list = []
num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el sgundo numero "))
num3 = int(input("Ingrese el tercer numero "))
num4 = int(input("Ingrese el cuarto numero "))
num5 = int(input("Ingrese el quinto numero "))
list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
print(list[:])
min = 9999
for i in list:
    if i <= min:
        min = i
print(f"el numer minimo es {min}")
max = 0
for n in list:
    if n >= max:
        max = n
print(f"el numer mayor es {max}")
