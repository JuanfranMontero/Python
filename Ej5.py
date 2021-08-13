
"""
Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, 
una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, 
el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, 
la suma acumulada de [1,2,3] es [1, 3, 6].
"""

def sumaListas(listaNumeros):

    listaFinal = []

    for i in range(len(listaNumeros)):

        if i == 0:

            listaFinal.append(listaNumeros[0])

        elif i != 0:

            listaFinal.append(listaFinal[i-1] + listaNumeros[i])

            

        
    print(listaFinal)


listaNumeros = [1,2,3,4,5]

sumaListas(listaNumeros)



"""
Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista
 y cree una nueva lista con los elementos que no fueron eliminados.
Luego escribe una función que se llame "media" que tome una lista y 
devuelva una nueva lista que contenga todos los elementos de la lista anterior menos el primero y el último.
"""


def eliminarElementosLista(listaNumeros):

    listaNumeros.pop(0)

    ultimoElemento = len(listaNumeros)
    listaNumeros.pop(ultimoElemento-1)

    listaFinal = listaNumeros
    
    print(listaFinal)

lista = [1,2,3,4,5]

eliminarElementosLista(lista)


