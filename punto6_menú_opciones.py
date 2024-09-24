# Función para pedir el alfabeto al usuario
def obtener_alfabeto():
    cantidad = int(input("Introduce la cantidad de elementos en el alfabeto: "))
    alfabeto = []
    for i in range(cantidad):
        elemento = input(f"Introduce el elemento {i+1} del alfabeto: ")
        alfabeto.append(elemento)
    return alfabeto

# Función para definir tres lenguajes a partir del alfabeto
def definir_lenguajes(alfabeto):
    lenguaje1 = {alfabeto[0], alfabeto[1]}
    lenguaje2 = {alfabeto[1], alfabeto[2]}
    lenguaje3 = {alfabeto[0] + alfabeto[1], alfabeto[2] + alfabeto[1]}
    return lenguaje1, lenguaje2, lenguaje3

# Función para realizar la operación estrella
def estrella(lenguaje, n):
    resultado = set([""])
    for _ in range(n):
        nuevo = set()
        for palabra in resultado:
            for elemento in lenguaje:
                nuevo.add(palabra + elemento)
        resultado.update(nuevo)
    return resultado

# Función para verificar si una cadena es palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]

# Función para generar palíndromos de longitud específica
def generar_palindromos(alfabeto, longitud):
    palindromos = set()
    for i in range(len(alfabeto)):
        for j in range(len(alfabeto)):
            if longitud == 2:
                palindromos.add(alfabeto[i] + alfabeto[i])
            elif longitud == 3:
                palindromos.add(alfabeto[i] + alfabeto[j] + alfabeto[i])
    return palindromos

# Función para reemplazar caracteres en una cadena
def reemplazar_caracteres(cadena, antiguo, nuevo):
    return cadena.replace(antiguo, nuevo)

# Función para invertir una cadena
def invertir_cadena(cadena):
    return cadena[::-1]

# Menú principal del programa
def menu():
    alfabeto = obtener_alfabeto()
    leng1, leng2, leng3 = definir_lenguajes(alfabeto)
    while True:
        print("\n--- Menú ---")
        print("1. Definir lenguajes y realizar operaciones")
        print("2. Generar palíndromos")
        print("3. Verificar si una cadena es palíndromo")
        print("4. Transformar cadena")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            print(f"Lenguaje 1: {leng1}")
            print(f"Lenguaje 2: {leng2}")
            print(f"Lenguaje 3: {leng3}")
            union_lenguajes = leng1.union(leng2)
            concatenacion = {a + b for a in leng1 for b in leng2}
            print(f"Unión de lenguaje 1 y 2: {union_lenguajes}")
            print(f"Concatenación de lenguaje 1 y 2: {concatenacion}")
            print(f"Estrella de lenguaje 1 (n=2): {estrella(leng1, 2)}")

        elif opcion == 2:
            longitud = int(input("Introduce la longitud del palíndromo (2 o 3): "))
            palindromos = generar_palindromos(alfabeto, longitud)
            print(f"Palíndromos generados: {palindromos}")

        elif opcion == 3:
            cadena = input("Introduce una cadena: ")
            if es_palindromo(cadena):
                print(f"La cadena '{cadena}' es un palíndromo.")
            else:
                print(f"La cadena '{cadena}' no es un palíndromo.")

        elif opcion == 4:
            cadena = input("Introduce una cadena: ")
            print("1. Reemplazar caracteres")
            print("2. Invertir cadena")
            subopcion = int(input("Selecciona una opción: "))

            if subopcion == 1:
                antiguo = input("Introduce el carácter a reemplazar: ")
                nuevo = input("Introduce el nuevo carácter: ")
                nueva_cadena = reemplazar_caracteres(cadena, antiguo, nuevo)
                print(f"Cadena resultante: {nueva_cadena}")
            elif subopcion == 2:
                print(f"Cadena invertida: {invertir_cadena(cadena)}")

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
