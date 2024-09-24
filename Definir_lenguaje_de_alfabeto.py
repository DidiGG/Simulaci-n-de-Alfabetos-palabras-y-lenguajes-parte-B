# Pedir al usuario el tamaño del alfabeto: ingresa un número para definir el tamaño del alfabeto
cantidad = int(input("Introduce la cantidad de elementos en el alfabeto: "))

# Pedir los elementos del alfabeto:
alfabeto = []
for i in range(cantidad):
    elemento = input(f"Introduce el elemento {i+1} del alfabeto: ")
    alfabeto.append(elemento)

# Mostrar el alfabeto ingresado
print(f"El alfabeto ingresado es: {alfabeto}")

# Definir tres lenguajes a partir del alfabeto
lenguaje1 = {alfabeto[0] + alfabeto[1], alfabeto[1] + alfabeto[2]}
lenguaje2 = {alfabeto[2] + alfabeto[0], alfabeto[0] + alfabeto[2]}
lenguaje3 = {alfabeto[1] * 2, alfabeto[0] * 3}

# Mostrar los lenguajes
print(f"Lenguaje 1: {lenguaje1}")
print(f"Lenguaje 2: {lenguaje2}")
print(f"Lenguaje 3: {lenguaje3}")
