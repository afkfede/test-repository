"""Escribir un codigo en el cual se comience con una lista vacia y se le pregunte al usuario el tratamiento que se le quiere dar. Si el usuario ingresa 'pila', se deberá eliminar y mostrar uno a uno en el orden convencional de la pila. 
Hacer lo mismo pero en el orden de la cola para el caso que ingrese 'cola'.
Pensar para que estructura utilizariamos una pila o cola en algun ejemplo cotidiano."""

def apilar_libro(elemento, lista):
    lista.append(elemento)
    print("Libro añadido")
    print(lista)
    
def desapilar_libro(lista):
    print("Eliminando el siguiente libro . . .")
    print(lista.pop())
    print(lista)

def mostrar_tamaño(lista):
    print("Mostrando tamaño . . .")
    print(len(lista))


def eliminar_cola(lista):
    print("Eliminando el siguiente libro . . .")
    print(lista.pop(0))
    print(lista)

def main():
    lista = []
    print("Bienvenido al sistema de gestion de libros de la biblioteca")
    print("¿De qué manera desea organizar sus libros?")
    op = input("Ingrese 'Pila' o 'Cola'.").capitalize()
    while True:
        if op == 'Pila':
            print("CREADOR DE PILAS ¿Qué desea hacer con sus libros?")
            print("0. Salir")
            print("1. Apilar")
            print("2. Desapilar (Se eliminará el libro más reciente que haya ingresado)")
            print("3. Numero de libros")
            op2 = input("Ingrese la opcion (0-1-2-3)")
            if op2 == '0':
                break
            elif op2 == '1':
                libro = input("Ingrese el elemento a apilar: ")
                apilar_libro(libro, lista)
            elif op2 == '2':
                desapilar_libro(lista)
            elif op2 == '3':
                mostrar_tamaño(lista)
                
        elif op == 'Cola':
            print("CREADOR DE COLAS ¿Qué desea hacer con sus libros?")
            print("0. Salir")
            print("1. Añadir")
            print("2. Eliminar (Se eliminará siempre el primer libro que haya ingresado)")
            print("3. Numero de libros")
            op2 = input("Ingrese la opcion (0-1-2-3)")
            if op2 == '0':
                break
            elif op2 == '1':
                libro = input("Ingrese el libro para agregar a la cola: ")
                apilar_libro(libro, lista)
            elif op2 == '2':
                eliminar_cola(lista)
            elif op2 == '3':
                mostrar_tamaño(lista)
                
main()

