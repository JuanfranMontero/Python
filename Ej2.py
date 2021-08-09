
"""
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

"""

def max_in_list(list):

    print(max(list))

max_in_list([1,2,3,4,5])

"""


"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

"""

def mas_larga(primeraPalabra, segundaPalabra, terceraPalabra):

    if primeraPalabra >= segundaPalabra <= terceraPalabra:

        return primeraPalabra

    elif segundaPalabra <= segundaPalabra >= terceraPalabra:

        return segundaPalabra

    else:

        return terceraPalabra

print(mas_larga("JuanfranciscoMonteroTriviño", "Juanfran", "JuanfranciscoMontero"))

"""

"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
"""

"""

def filtrar_palabras(listaPalabras, numEntero):

    for palabras in listaPalabras:

        if len(palabras) == numEntero:

            print(palabras)


filtrar_palabras(["Juanfran", "Maria", "Isabel", "Juani"], 8) 

"""


"""
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

"""

cadenaPalabras = input("Introduce su cadena de texto: ")

contador = 0

for letra in cadenaPalabras:

    for i in letra:

        if i.isupper():

            contador += 1


print("Su cadena tiene ",contador," letras mayúsculas.")

"""


"""
Construir un pequeño programa que convierta números binarios en enteros.
"""

"""

numeros = int(input("Introduce un número: "))

print(bin(numeros))

"""


"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

"""

anioActual = int(input("Introduce el año en el que estamos: "))

datosUsuarios = {}

for edad in range(3):

    datos = input("Introduce su nombre y su año de nacimiento: ")
    
    informacionUsuario = datos.split(" ")
    
    anioNacimiento = int(informacionUsuario[1])

    datosUsuarios[informacionUsuario[0]] = anioActual - anioNacimiento

print("")

for usuario in datosUsuarios:

    print(usuario,"cumple:",datosUsuarios[usuario],"años.")

"""


"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

"""

listaEdades = []

for i in range(10):

    edad = (input("Introduce la edad de la persona: "))

    if int(edad) > 20:

        listaEdades.append(edad)

print(tuple(listaEdades))

"""

"""
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

"""

conjuntoNombres = ["Juanfran", "Maria", "Isabel", "Juani", "Antonio"]

caracter = input("Introduce la letra por la que desee buscar el nombre: ")

for nombre in conjuntoNombres:

    if nombre[0] == caracter or nombre[0] == caracter:

       print(nombre, end=" ")

""" 


"""
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

"""

def contarVocales(palabra):

    palabra = palabra.lower()

    print("La palabra ("+palabra.capitalize()+") tiene ", palabra.count('a') ,"vocales A, ",palabra.count('e') ,"vocales E, ", palabra.count('i') ,"vocales I, ", palabra.count('o') ,"vocales O y ", palabra.count('u') ," vocales U")


contarVocales("JUANFRAN MONTERO TRIVIÑO")

"""

"""
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""

"""

def esBisiesto(anio):

    anio = int(anio)

    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):

        print("El año ",anio," es bisiesto.")

    else:

        print("El año ",anio," NO es bisiesto.")

esBisiesto(2020)

"""