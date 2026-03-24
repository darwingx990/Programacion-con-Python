contraseña = "12345" # Se crea una contraseña fija para el programa verificar y validar acceso, pero se puede modificar a gusto del usuario
nombre = input("Ingrese su nombre: ")
contraseña_verifiada = 0 # Se crea una variable para almacenar la contraseña ingresada por el usuario y compararla con la contraseña fija, se inicializa en 0 para que el ciclo se ejecute al menos una vez

# El ciclo while se ejecuta mientras la contraseña ingresada por el usuario sea diferente a la contraseña fija, si el usuario ingresa la contraseña correcta, el ciclo se detiene y se muestra un mensaje de bienvenida con el nombre del usuario
while contraseña != contraseña_verifiada:
    contraseña_verifiada = input("Ingrese su contraseña: ")
    print("Contraseña incorrecta. Intentelo de nuevo: ")
    contraseña_verifiada
print("Bienvenido,", nombre)

palabra = input("Ingrese una palabra: ") # Se pide al usuario que ingrese una palabra y se almacena en la variable "palabra"
vocales = [] # Se crea una lista vacía para almacenar las vocales encontradas en la palabra ingresada por el usuario, se utiliza una lista para poder almacenar todas las vocales encontradas y luego contar cuantas vocales hay en total
for letra in palabra: # Utilizamos el ciclo For para recorrer cada letra de la palabra ingresada por el usuario, el ciclo se ejecuta una vez por cada letra de la palabra, y en cada iteración se almacena la letra actual en la variable "letra".
    if letra.lower() in ("aeiou"):
        vocales.append(letra) # Aqui utilizamos el metodo append para agregar la letra actual a la lista de vocales.
print(palabra, "tiene", len(vocales), "vocales.") # Se imprime el resultado.

for i in range(len(vocales)):
    print(vocales[i])