l = [5, 2, 1, 4, 3]
print("Lista original: ", l)

def intercambia(i, j, lista):
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar
    
def minimos_sucesivos(l):
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                print(f"Comparamos el elemento 'i' {l[i]} con 'j' {l[j]}")
                intercambia(i, j, l)
                print("Nueva lista: ", l)
            else:
                print("No se realizaron intercambios")
                
minimos_sucesivos(l)


lista = [5, 2, 1, 4, 3, 6]
print(lista)

#k = indice
#v = valor del elemento que estan en ese indice 'k'

def inserta(lista, k, v):
    print("Indice: ", "[",k,"]")
    print("Elemento: ", v)
    for i in range(k):
        if v < lista[i]:
            print("Elemento eliminado: ", lista.pop(k))
            print(f"Insertar el elemento: {v}, en la posicion: {i}")
            lista.insert(i,v)
            print("iteracion")