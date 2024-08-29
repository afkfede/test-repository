

def agregarFactura(numero, costo, diccionario):
    if numero in diccionario:
        diccionario[numero]['costo'] += costo
    else:
        diccionario[numero] = {
            'costo': costo
        }
    print(" ---------- ")
    print("Factura agregada")
    print(" ---------- ")
    print("Lista de facturas pendientes: ")
    print(diccionario)
    print(" ---------- ")

    

def pagarFactura(numero, diccionario):
    if numero in diccionario:
        del diccionario[numero]
        print(f"Factura nro: {numero}, pagada exitosamente")
        print(" ---------- ")
        print("Cuenta actualizada.")
        print("Lista de facturas pendientes: ")
        print(diccionario)
        print(" ---------- ")
    else:
        print(" ---------- ")
        print("No se encontro factura con ese numero.")
        print(" ---------- ")


def main():
    facturas = {}
    
    while True:
        print("1- Agregar factura")
        print("2- Pagar factura")
        print("3- Terminar")
        
        op = int(input("Ingrese opcion(1, 2, 3): "))
        
        if op == 1:
            nroFactura = int(input("Ingrese numero de factura: "))
            costeFactura = int(input("Ingrese el coste de la factura: "))
            agregarFactura(nroFactura, costeFactura, facturas)
            
        elif op == 2:
            nroFactura = int(input("Ingresar el numero de la factura a pagar: "))
            pagarFactura(nroFactura, facturas)
            
        elif op == 3:
            print(" ---------- ")
            print("Hasta luego!")
            print(" ---------- ")
            break
        
        else:
            print(" ---------- ")
            print("Opcion invalida, ingrese una opcion valida.")
            print(" ---------- ")

main()