prod = int(input("Ingrese la cantidad de productos: "))
for x in range (0, prod):
    monto = int(input("Ingrese el monto del producto: "))
    if monto >= 15000:
        print("Accede a Envio Gratis")
    else:
        print("No le corresponde Envio Gratis")