def mostrar_menu():
    print("CREADOR DE PILAS ¿Que quiere hacer?")
    print("0. Salir")
    print("1. Apilar")
    print("2. Desapilar")
    print("3. Numero de elementos")
    
def pedir_opcion():
    print("Ingrese la opcion (0-1-2-3): ")
    opcion = int(input())
    while opcion < 0 or opcion > 3:
        print("Opcion incorrecta. Ingrese una valida: ")
        opcion = int(input())
    return opcion

def apilar_elemento():
    print("Ingrese el elemento a apilar: ")
    elemento = input()
    pila.push(elemento)
    
def desapilar_elemento():
    print("Eliminando el siguiente elemento . . .")
    print(pila.pop())
    
def mostrar_tamaño():
    print("Mostrando tamaño . . .")
    print(pila.size())
    
def creador_pila():
    mostrar_menu()
    opcion = pedir_opcion
    hacer_accion(opcion)
    print("Presione ENTER par continuar . . .")
    input()
    
def hacer_accion(opcion):
    if opcion == 1:
        apilar_elemento()
    elif opcion == 2:
        desapilar_elemento()
    elif opcion == 3:
        mostrar_tamaño()
        
pila = Pila()

mostrar_menu()
opcion = pedir_opcion()
hacer_accion(opcion)
print("Presione ENTER para continuar . . .")
input()
while opcion != 0:
    mostrar_menu()
    opcion = pedir_opcion()
    hacer_accion(opcion)
    print("Presione ENTER para continuar . . .")
    input()