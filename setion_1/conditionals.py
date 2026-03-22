# El programa debe pedir al usuario un numero y determinar si el numero es par o impar y si es mayor, menos o igual a 10.

numero = int(input("Digite un numero: "))
# print(numero % 2)
if numero % 2 == 0:
    print(numero, "es un numero par")
else:
    print(numero, "es un numero impar")

if numero > 10:
    print(numero, "es mayor que 10")
elif numero == 10:
    print("El numero diligenciado es 10.")
else:
    print(numero, "es menor a 10.")
