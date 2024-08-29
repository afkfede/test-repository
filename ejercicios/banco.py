saldo = float(input("Ingrese saldo actual: $"))
print("1- Extraccion de dinero")
print("2- Prestamo rapido de $50.000")
print("3- Pagar servicio de luz")
cod = int(input("Ingrese un codigo de operación: "))
if cod == 1:
    montExt = int(input("Ingrese monto a extraer: $"))
    if montExt <= saldo:
        print("Operación valida.")
        saldoRes = saldo - montExt
        print("Se extrajo $", montExt)
        print("Saldo actualizado: $", saldoRes)
    else:
        print("Operacion invalida. Saldo insuficiente.")
elif cod == 2:
    saldoRes = saldo + 50000
    print("Se realizo la solicitud del prestamo.")
    print("Saldo actualizado: $", saldoRes)
elif cod == 3:
    montServ = float(input("Ingresar monto a pagar: $"))
    if montServ <= saldo:
        print("Operacion valida.")
        saldoRes = saldo - montServ
        print("Se realizo el pago de: $", montServ)
        print("Saldo actualizado: $", saldoRes)
    else:
        print("Operacion invalida. Saldo insuficiente.")
else: 
    print("Operacion invalida.")
    