"""def factorial(num):
    if num <= 1:
        resultado = 1
        print(resultado)
    else:
        resultado = num*factorial(num-1)
        print(resultado)
    return resultado
    
numero = int(input("Ingrese el numero del que desee saber el valor de su factorial: "))
calculo = factorial(numero)
print(f"El factorial de {numero} es: {calculo}")"""

def jugar(intento=1):
    respuesta = input ("De que color es un naranja")
    if respuesta != "naranja":
        if intento < 3:
            print("Fallaste, intentalo de nuevo")
            intento += 1
            jugar(intento)
        else:
            print("Has perdido")
    else:
        print("Felicitaciones, ganaste")
        
jugar()