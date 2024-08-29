#definir diccionario vacio
persona = {}

#funcion añadir persona
def agregar_persona():
    dni = int(input("Ingrese numero de dni"))
    nombre = str(input("Ingrese nombre"))
    apodo = str(input("Ingrese apodo"))
    telefono = int(input("Ingrese telefono"))
    
    #creamos el diccionario con los datos de la persona
    datos_personal = {
    "nombre":nombre,
    "apodo": apodo,
    "telefono": telefono
    }
    
    #agregamos los datos personal al diccionario principal
    persona[dni] = datos_personal
    
    #mostramos el diccionario con los datos cargados
    print("Datos personales cargados correctamente")
    print(persona)

#llamamos a la funcion para agregar personas
cantidad_registro = int(input("Ingrese la cantidad de personas a registrar"))
for numero in range(cantidad_registro):    
    agregar_persona()
    
#opcion 2 while cargar hasta tener una respuesta negativa
continuar = True
while continuar:
    agregar_persona()
    respuesta = input("Desea agregar otra persona(s/n)")
    if respuesta == 'n':
        continuar = False