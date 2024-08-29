"""def sumarDosNumeros(a,b):
    res = a + b
    print("La suma es", res)

def restarDosNumeros(a,b):
    res = a - b
    print ("La resta es", res)

def potenciaDeNumero(a,b):
    pot = a**b
    print ("La potencia es", pot)
    
    
num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))

sumarDosNumeros(num1, num2)
restarDosNumeros(num1, num2)
potenciaDeNumero(num1, num2)"""

"""num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1>num2:
    x = num1,'es mayor que',num2
else:
    x = num2,'es mayor que',num1
print(x)"""

"""x = str(input("Palabra: ")).capitalize()

if x == "Hola":
    print("Correcto")
else:
    print("Incorrecto")"""
    
"""acu = 0
for x in range (0, 101, 2):
    print(x)
    acu = acu + 1
    
print("Contador par: ", acu)"""

"""usuario = True
if usuario:  #if not
    print("Verdadero")
else:  
    print("Falso")"""
    
edad = 8
if edad > 9:
    print("La edad es1: ", edad)
elif edad > 5:    #elif solo confirma la primera condicion que se cumple
    print("La edad es2: ", edad)
elif edad > 6:
    print("La edad es3: ", edad)
else:
    print("La edad es4: ", edad)