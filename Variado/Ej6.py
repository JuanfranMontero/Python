"""
Realice un programa que enumere los paises de la siguiente lista
paises = ['Canada', 'USA', 'Mexico', 'Australia']
"""

def enumerarPaises(listaPaises):

    for i in range(len(listaPaises)):

        print(i+1,"-", listaPaises[i])


paises = ['Canada', 'USA', 'Mexico', 'Australia']

enumerarPaises(paises)


"""
Crear un ciclo for que cuente de 0 a 100
"""

for i  in range(100):

    print(i+1, end=" ")


"""
Haz una tabla de multiplicar utilizando el ciclo for
"""

def tablaMultiplicar(numero):

    print("TABLA DE MÚLTIPLICAR DEL NÚMERO ",numero)

    for i in range(10):

        print(numero,"x",i+1,"= ",numero*(i+1))

tablaMultiplicar(2)

"""
Imprima los números del 1 a 10 al revés utilizando el ciclo for
"""

for i  in reversed(range(10)):

    print(i+1, end=" ")


"""
Crear un bucle que cuente todos los números pares hasta el 100
"""

sumaTotal = 0

for i in range(100):

    if i % 2 == 0:

        sumaTotal += i

print("La suma total de los número pares es de ", sumaTotal)


"""
Dado un número, cuente el número total de dígitos de un número
Por ejemplo, el número es 75869, por lo que la salida debería ser 5.
"""

def contarDigitos(numero):

    print(len(str(numero)))

contarDigitos(123456789)




"""
Imprima el siguiente patrón con el ciclo for:

*
**
***
****
*****
****
***
**
*
"""

tamanio = 5



for i in range(tamanio):
    
    for j in range(tamanio):

        if i >= j:

            print('*', end=" ")

        else: 

            print(' ', end=" ")

    print(" ")

for i in reversed(range(tamanio)):
    
    for j in range(tamanio):

        if i <= j:

            print(' ', end=" ")

        else: 

            print('*', end=" ")

    

    print("")