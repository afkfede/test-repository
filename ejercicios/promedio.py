nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
prom = (nota1 + nota2) / 2
if prom >= 4:
    print("Promedio de: ", prom)
    print("¿Está aprobado? Si")
else:
    print("Promedio de: ", prom)
    print("¿Está aprobado? No")