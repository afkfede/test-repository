"""En este proyecto, vas a desarrollar un sistema simple para gestionar el inventario de productos en 
una tienda. El sistema permitirá agregar nuevos productos, actualizar la cantidad en stock, 
eliminar productos del inventario y buscar detalles de productos específicos. Además, deberás escribir 
pruebas unitarias utilizando pytest para asegurarte de que todas las funciones del sistema funcionan 
correctamente."""

"""
*agregar_producto(nombre, cantidad, precio): Agrega un nuevo producto al inventario con su nombre, 
cantidad en stock y precio.
*actualizar_stock(nombre, nueva_cantidad): Actualiza la cantidad en stock de un producto existente.
*eliminar_producto(nombre): Elimina un producto del inventario.
*buscar_producto(nombre): Devuelve los detalles de un producto específico, como su 
cantidad en stock y su precio.
"""
productos={}

def agregar_producto():
    try:
        nombre=str(input("Ingrese el nombre del producto "))
        if nombre in productos: #Si el nombre ingresado ya existe
            print ("Error, vuelva a intentarlo")
            return agregar_producto() #Vuelve a preguntar el nombre
        cantidad=int(input("Ingrese la cantidad de dicho producto "))
        precio=float(input("Ingrese el precio del producto "))

#se ingresan los datos a añadir sobre el producto

        items= {
            'nombre':nombre,
            'cantidad':cantidad,
            'precio': precio,
        }

        productos[nombre]=items #Usamos el nombre como clave para acceder a su precio y cantidad de stock
    except ValueError:
        print ("Error de tipo valor")



def actualizar_stock():
    nombre=input("Ingrese el nombre del producto ")
    if nombre in productos: #si el producto está en la lista de productos
        nueva_cantidad=int(input("Ingrese la cantidad actual en stock ")) #Se escribe la cantidad nueva de objetos
        stock_actual={'cantidad':nueva_cantidad} #para actualizar el diccionario se necesita crear un diccionario a parte
        productos[nombre].update(stock_actual) #con .update actualizamos el diccionario original
    else:
        print ("Error")


def eliminar_producto():
    nombre=input("Ingrese el nombre del producto que desee eliminar ")
    if nombre in productos: #Si el producto está en la lista de productos
        print ("Eliminando producto...")
        del productos[nombre] #Se elimina el producto con dicho nombre
        print (f"Producto llamado {nombre} eliminado correctamente")
    else:
        print ("Error, nombre incorrecto")


def buscar_producto():
    nombre=input ("Ingrese el nombre del producto que desee ver ")
    if nombre in productos: #Si el nombre del producto está
        datos=productos[nombre] #Se crea una lista provisoria para que funcione la función
        print (f"Datos del objeto llamado {nombre}")
        print (f"Stock: {datos['cantidad']}")
        print (f"Precio: {datos['precio']}")
    else:
        print ("Error")



def terminar_programa():
    productos.clear()
    print ("Base de datos de productos vaciada.")
    print ("Base de datos actualizada")
    print (productos)
    print ("¡Hasta luego!")

def MenuPrincipal():
    while True:
        print("-----------------------------")
        print("\n--- Menú de opciones ---")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Terminar programa")
        print("-----------------------------")

        opcion=input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            actualizar_stock()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            buscar_producto()
        elif opcion == '5':
            terminar_programa()
            break
        else:
            print ("Opcion no válida. Por favor, seleccione una opcion válida (1-4).")
            MenuPrincipal()

MenuPrincipal()