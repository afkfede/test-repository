"""#Ejemplo 1
(lambda nombre: print(f"Hola {nombre}"))("Pedro")

#Ejemplo 2
colores = ["rojo", "azul", "verde", "amarillo"]
(lambda color: print(f"El color se encuentra en la posicion {colores.index(color)} de la lista"))

#Ejemplo 3
multiplicacion = lambda numero1, numero2: numero1*numero2

resultado = multiplicacion(10,5)
resultado1 = multiplicacion(8,2)

print(resultado)
print(resultado1)

#Ejemplo 4
mayuscula = lambda cadena: cadena.upper()

print(mayuscula("rodrigo"))

#Ejemplo 5
positivo = lambda x: "El numero es positivo" if x>0 else "El numero es negativo"

print(positivo(4))

#Ejemplo 6
mayor_edad = lambda edad: "Eres mayor de edad" if edad>=18 else "Eres menor de edad"

edad = int(input("Ingrese su edad"))
resultado_edad = mayor_edad(edad)
print(resultado_edad)

#Ejemplo 7
lista = [20, 15, -4, 5, -1, 12, -3]

lista_positivos = list(filter(lambda x: x>=0, lista))
print(lista_positivos)

#Ejemplo 8
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_duplicar = list(map(lambda x: x*3, lista))
print(lista_duplicar)"""

#Ejercicio 1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)

#Ejercicio 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_cuadrados = list(map(lambda x: x*x, lista))
print(lista_cuadrados)

#Ejercicio 3
lista1 = [3, 5, 6, 7, 9]
lista2 = [2, 4, 6, 8, 10]

lista_nueva = list(map(lambda x, y: x + y, lista1, lista2))
print(lista_nueva)

#Ejercicio 4
lista = ["hola", "chau", "computadora", "curso", "mouse"]

lista_filtrada = list(filter(lambda x: len(x) >=5, lista))
print(lista_filtrada)