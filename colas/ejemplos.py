# Cola criterio FIFO primer elemento en ingresar es primer elemento en salir

cola = []
cola = ["Juan", "Pedro", "Maria"]

print(cola)

# Agregar elementos a la cola

cola.append("Gustavo")
cola.append("Vanesa")

print(cola)

# Sacar elementos de la cola

salida = cola.pop(0)
print(f"Atendiendo a {salida}")

salida = cola.pop(0)
print(f"Atendiendo a {salida}")

print(cola)
