
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("Introduce su edad: "))

for i in range(edad):

    print(i+1, end=" ")


"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números impares desde 1 hasta ese número separados por comas.
"""

numero = int(input("Introduce un número: "))

for i in range(numero):

    if i % 2 != 0:

        print(i, end=", ")



"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número 
hasta cero separados por comas.
"""

numero = int(input("Introduce un número positivo: "))


for i in reversed(range(numero)):

    print(i,end=", ")


"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

inversion = int(input("¿Cantidad a invertir?: "))
interes = int(input("¿Interés anual?: "))
anios = int(input("¿Durante cuantos años?: "))


cantidadTotal = ((inversion * interes) / 100) * anios

print("La cantidad a percibir es de {}€.".format(cantidadTotal))


"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.

*
**
***
****
*****

"""

altura = int(input("Introduce un número positivo: "))

for i in range(altura):

    for j in range(altura):

        if j <= i:

            print('*', end=" ")
        
        else: 

            print(' ', end=" ")  
        
    print(" ")


"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

"""

altura = int(input("Introduce un número positivo: "))

for i in range(1, altura + 1, 2):

    for j in range(i, 0, -2):

        print(j, end=" ")

    print("")


"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

correcto = False

contrasena = input("Introduce una contraseña: ")

while not correcto:

    contrasenaConfirmacion = input("Repite la contraseña: ")

    if contrasena == contrasenaConfirmacion:

        print("")
        print("¡Bienvenido al sistema!")
        print("")
        correcto = True

    else:
        print("")
        print("Contraseña incorrecta, intentelo de nuevo...")
        print("")


"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
 una a una las letras de la palabra introducida empezando por la última.
"""

palabra = input("Introduce una palabra: ")

for i in reversed(palabra):

    print(i, end="  ")


"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
 y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

frase = frase.lower()
letra =  letra.lower()

contador = frase.count(letra)

print("La letra '{}' aparece {} veces.".format(letra.upper(),contador))


"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

salir = False

while not salir:

    eco = input("Escribe aquí: ")

    if eco.lower() == "salir":

        salir = True

    else:

        print(eco)