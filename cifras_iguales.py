#Caso No. 5: Dado un número entero determinar si sus dos últimas cifras son iguales


print("-----------------------------------")
print("----------Cifras Iguales-----------")
print("-----------------------------------")


# input

z = int(input("Ingrese el número entero a verificar: "))
print(" ")

# processing
q1 = z%10
q2 = ((z%100)-q1)//10

# output

if q1 == q2:
    print("Las dos últimas cifras si son iguales.")
    print(" ")
else:
    print("Las dos últimas cifras no son iguales. Por favor, verifique sus datos.")
    print(" ")