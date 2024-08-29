print("Menu del dia: ")
print("1- LOMITO: $4000")
print("2- HAMBURGUESA: $5000")
print("3- PIZZA: $7000")
cod = int(input("Ingrese comida a pedir: "))
if cod == 1:
    pedido = str(input("Es para llevar? (Si/No)")).capitalize()
    if pedido == "Si":
        precio_rec = 4000*1.1
        precio_total = 4000+precio_rec
        print("El costo con envio es de: $", precio_total)
    else:
        print("El precio en el local es: $4000")
        