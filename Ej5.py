
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


"""
Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente
 y devuelva False en caso contrario.
Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.
"""

def ordenada(listaNumeros):

    for i in range(len(listaNumeros)):

        if i < len(listaNumeros)-1:

            if listaNumeros[i] > listaNumeros[i+1]:

                return False
        
        elif i == len(listaNumeros):

            if listaNumeros[i] < listaNumeros[i-1]:

                return False

    return True


lista = [1,2,3,4,5]


print(ordenada(lista))


"""
Escribe una función que lea las palabras de un archivo de texto (texto.txt)
 y construya una lista donde cada palabra es un elemento de la lista.
"""

fichero =  open("texto.txt", "r")

datosFicheros = []

for words in fichero:

    datosFicheros.append(words.split())

fichero.close()

print(datosFicheros)


"""
Escribe una función llamada "inversa" que busque todas las palabras inversas de una lista.
Ejemplo de palabras inversas: radar, oro, rajar, rallar, salas, somos, etc...
"""


def inversa(palabra):

    if palabra == ''.join(reversed(palabra)):

        return True
    
    else:

        return False


texto = input("Introduce la palabra para sabre si es palíndromo: ")

print(inversa(texto))