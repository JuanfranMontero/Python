
"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
 en una lista y la muestre por pantalla.
"""
listaAsignaturas = []

salir = False

while not salir:

    asignatura = input("Ingrese una asignatura, 'N' para salir: ")


    if asignatura.lower() != 'n':

        listaAsignaturas.append(asignatura)

    else:

        salir = True 

print(listaAsignaturas)


"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
 Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""

lista = ["Matemáticas", "Lengua", "Química", "Historia"]

for i in range(len(lista)):

    print("Yo estudio {}.".format(lista[i]))



"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura, 
 y después las muestre por pantalla con el mensaje 
 En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista 
 y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""


listaAsignaturas = ["Matemáticas", "Lengua", "Química", "Historia"]
listaNotas = []

for i in range(len(listaAsignaturas)):

    nota =  int(input("¿Qué nota has sacado en {}: ".format(listaAsignaturas[i])))

    listaNotas.append(nota)

print("")

for i in range(len(listaAsignaturas)):

    print("{}- En {} has sacado un {}.".format((i+1),listaAsignaturas[i],listaNotas[i]))


"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
 los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

numerosGanadores = []

for i in range(5):

    num = int(input("Introduce un número ganador: "))

    numerosGanadores.append(num)

numerosGanadores.sort()

print("Números Ganadores - ",numerosGanadores)


"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

lista = [1,2,3,4,5,6,7,8,9,10]

for i in reversed(lista):

    if i == 1:

        print(i,end=".")

    else:

        print(i, end=", ")

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
 Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

listaAsignaturas = ["Matemáticas", "Lengua", "Química", "Historia"]
asingaturasPendientes = []

for i in range(len(listaAsignaturas)):

    nota = int(input("Introduzca la nota de la asignatura {}: ".format(listaAsignaturas[i])))

    if nota < 5:

        asingaturasPendientes.append(listaAsignaturas[i])


print("")

if len(asingaturasPendientes) > 0:

    print("Tienes que recuperar las asignaturas: ",asingaturasPendientes)

else:

    print("No tienes que recuperar ninguna asignatura.")



"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
 y muestre por pantalla la lista resultante.
"""
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t']
listaAbecedario = []

for i in range(len(abecedario)):

    if i % 3 == 0:

       listaAbecedario.append(abecedario[i])


print(listaAbecedario)



"""
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
 y muestre por pantalla el menor y el mayor de los precios.
"""

listaNumeros = [50, 75, 46, 22, 80, 65, 8]

print("El número mayor de la lista es el '{}' y el menor es el '{}'".format(max(listaNumeros),min(listaNumeros)))