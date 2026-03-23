contraseña = "12345"
nombre = input("Ingrese su nombre: ")
contraseña_verifiada = 0

while contraseña != contraseña_verifiada:
    contraseña_verifiada = input("Ingrese su contraseña: ")
    print("Contraseña incorrecta. Intentelo de nuevo: ")
    contraseña_verifiada
print("Bienvenido,", nombre)

palabra = input("Ingrese una palabra: ")  # Puede ser Esternomascloideo
vocales = []
for letra in palabra:
    if letra.lower() in ("aeiou"):
        vocales.append(letra)
print(palabra, "tiene", len(vocales), "vocales.")

for i in range(len(vocales)):
    print(vocales[i])
# Studying the for loop and while loop in python.