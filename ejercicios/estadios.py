estadios = []
for i in range(3):
    nombre = input("Ingresar nombre del estadio {}:".format(i+1))
    capacidad = int(input("Ingresar capacidad del estadio {}:".format(i+1)))
    estadios.append((nombre, capacidad))
    
mayor_cap = max(estadios, key=lambda x: x[1])
print("El estadio {} con capacidad de {} personas, es el de mayor capacidad.".format(mayor_cap[0], mayor_cap[1]))