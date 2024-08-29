"""Hacer un codigo para manejar una base de datos de una empresa. Habra un diccionario princiapal 
en el que la clave de cada cliente sera DNI y el valor sera otro dccionario  con los datos del clientes 
(nombre, apellido correo)
El programa debe preguntar al usuario por un opcion del siguiente menu (1) Añadir cliente, 
(2) Eliminiar Cliente, (3) Mostrar cliente  (4) Terminar

a) pedir los datos necesarios, agregar un cliente nuevo y mostrar el diccionario
b) pedir un DNI y eliminar cliente. En caso  que exista, debe avisarlo por mensaje
c)pedir DNI y mostrar los datos en un mensaje (nombre , apellido y ...) . 
Mostrar error si no lo encuentra
d) vaciar el diccionario, mostrandolo y mostrar mensaje despedida.  """


def agregarCliente(dni, nombre, apellido, correo, diccionario):
    diccionario[dni] = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo
    }
    print(" ---------- ")
    print("Cliente agregado correctamente")
    print("Estado actual del diccionario:")
    print(diccionario)
    print(" ---------- ")


def eliminarCliente(dni, diccionario):
    if dni in diccionario:
        del diccionario[dni]
        print(" ---------- ")
        print(f"Cliente con DNI {dni} eliminado correctamente.")
        print("Estado actual del diccionario:")
        print(diccionario)
        print(" ---------- ")
    else:
        print(" ---------- ")
        print(f"No se encontró ningún cliente con DNI {dni}.")
        print(" ---------- ")


def mostrarCliente(dni, diccionario):
    if dni in diccionario:
        cliente = diccionario[dni]
        print(" ---------- ")
        print(f"Datos del cliente con DNI {dni}:")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido: {cliente['apellido']}")
        print(f"Correo: {cliente['correo']}")
        print(" ---------- ")
    else:
        print(" ---------- ")
        print(f"No se encontró ningún cliente con DNI {dni}.")
        print(" ---------- ")


def vaciarDiccionario(diccionario):
    diccionario.clear()
    print(" ---------- ")
    print("Diccionario vaciado correctamente.")
    print("Estado actual del diccionario:")
    print(diccionario)
    print("Hasta luego!")
    print(" ---------- ")


def main():
    diccionario_clientes = {}

    while True:
        print("*** Menú de opciones ***")
        print("1- Añadir cliente")
        print("2- Eliminar cliente")
        print("3- Mostrar cliente")
        print("4- Terminar")

        op = input("Seleccione una opción (1,2,3,4): ")

        if op == '1':
            dni = input("Ingrese el DNI del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            correo = input("Ingrese el correo electrónico del cliente: ")
            agregarCliente(dni, nombre, apellido, correo, diccionario_clientes)

        elif op == '2':
            dni = input("Ingrese el DNI del cliente que desea eliminar: ")
            eliminarCliente(dni, diccionario_clientes)

        elif op == '3':
            dni = input("Ingrese el DNI del cliente que desea mostrar: ")
            mostrarCliente(dni, diccionario_clientes)

        elif op == '4':
            vaciarDiccionario(diccionario_clientes)
            break

        else:
            print(" ---------- ")
            print("Opción inválida. Por favor seleccione una opción válida.")
            print(" ---------- ")

main()
