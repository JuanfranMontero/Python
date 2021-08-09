
"""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def calcularMayorDeDos(primerValor, segundoValor):

    if primerValor > segundoValor:

        print("El primero valor (",int(primerValor),") es mayor que el segundo valor (",int(segundoValor),")")

    elif  primerValor <  segundoValor:

        print("El segundo valor (",segundoValor,") es mayor que el primer valor (",primerValor,")")

    else:

        print("Los dos valores son iguales")

calcularMayorDeDos(4,12)


"""
2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def calcularMayorDeTres(primerValor, segundoValor, tercerValor):

    valorMayor = primerValor

    if segundoValor > valorMayor:

        valorMayor = segundoValor

    if tercerValor > valorMayor:

        valorMayor = tercerValor

    print("El valor mayor es: ", valorMayor)

calcularMayorDeTres(1,2,3)


"""
3- Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def contadorCaracteres(nombre):

    caracteresTotales = 0

    for caracteres in nombre:

        caracteresTotales += 1

    print(nombre + " tiene ", caracteresTotales," caracteres.")

contadorCaracteres("Juanfran")
 
"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def encontrarVocal(caracter):

    if (caracter == 'a' or caracter == 'A' or caracter == 'e' or caracter == 'E' or caracter == 'i' or caracter == 'I' or caracter == 'o' or caracter == 'O' or caracter == 'u' or caracter == 'U'):

        print(f"El carácter {caracter} es una vocal.")
    
    else:
        print(f"El carácter {caracter} no es una vocal.")
    

encontrarVocal('O')

"""
5- Escribir una función sum() y una función multip()
 que sumen y multipliquen respectivamente todos los números de una lista. 
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

lista = [1,2,3,4,5]

def suma(lsita):

    contadorSuma = 0
    for numero in lista:

        contadorSuma += numero

    return contadorSuma

def multi(lista):

    contadorMulti = 1

    for numero in lista:
        
        contadorMulti *= numero
        
    return contadorMulti

resultadoSuma  = suma(lista)
resultadoMulti = multi(lista)

print(f"El resultado de la suma es de: {resultadoSuma} || El resultado de la multiplicación es de: {resultadoMulti}")


"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(texto):

    for letras in reversed(texto):

        print(letras, end="")


cadena = input("Introduce el texto: ")

inversa(cadena)

"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
 ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(palabra):

    if palabra == ''.join(reversed(palabra)):

        return True
    
    else:

        return False


texto = input("Introduce la palabra para sabre si es palíndromo: ")

resultadoPali = es_palindromo(texto)

print(resultadoPali)


"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.
"""

lista1 = [1,2,54,6,20]
lista2 = [4,5,7,6,5,7]

def superPosicion(lista1, lista2):

    for numLista1 in lista1:

        for numLista2 in lista2:

            resultado = numLista2 in lista1

            if resultado:

                return True

        return False

resultado = superPosicion(lista1,lista2)

print(resultado)


"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(numeroVeces, caracter):

    print(numeroVeces * caracter)

generar_n_caracteres(5,'x ')

"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******
"""

lista = [5,2,5,12]

for i in lista:
    print (i * 'X ')
