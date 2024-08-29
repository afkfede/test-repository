def agregarPersona(dni, nombre, apodo, telefono, diccionario):
    diccionario[dni] = {
        'nombre': nombre,
        'apodo': apodo,
        'telefono': telefono
    }
    print("Persona agregada")
    print(diccionario)

def main():
    diccionarioPersona = {}
    
    while True:
        print("1- Agregar persona")
        print("2- Salir")
        
        op = input("Ingresar opcion (1, 2): ")
        
        if op == '1':
            dni = int(input("Ingrese su dni: "))
            nombre = input("Ingrese su nombre: ")
            apodo = input("Ingrese su apodo(si no tiene ingrese '-'): ")
            if apodo == '-':
                apodo = "No tiene"
            telefono = int(input("Ingrese su numero de telefono: "))
            agregarPersona(dni, nombre, apodo, telefono, diccionarioPersona)
        
        elif op == '2':
            break
        
        else:
            print("Opcion invalida")
            
main()