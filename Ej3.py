
"""
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

print("------ ADIVINADOR DE RIMAS ------------")

primeraPalabra = input("Introduce la primera palabra: ")
segundaPalabra = input("Introduce la segunda palabra: ")

if primeraPalabra[-3] == segundaPalabra[-3] and primeraPalabra[-2] == segundaPalabra[-2] and primeraPalabra[-1] == segundaPalabra[-1]:

    print("RIMAN")

elif primeraPalabra[-2] == segundaPalabra[-2] and primeraPalabra[-1] == segundaPalabra[-1]:

     print("RIMAN UN POCO")

else:

     print("NO RIMAN NADA")


"""
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). 
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

def calculaInteres(cantidadDinero, tasaInteres, anios):

     resultado = cantidadDinero * ( 1 + tasaInteres / 100) ** anios

     return resultado


print("El interés anual se converte en: {0:.2f}".format(calculaInteres(10000,4.5,20)),"€ en un plazo de 20 años")


"""
Imprimir 10 veces la serie de números de 1 a 10.
"""

for i in range(10):

    for c in range(10):

        print(c+1, end=" ")
    
    print(" ")


"""
Para un número N imprimir su tabla de multiplicar.
"""

def tablaMultiplicar(num):

     for i in range(10):

          print("TABLA DE MÚLTIPLICAR DEL",num)
          print(num,"x",i+1,":",(i+1)*num)

tablaMultiplicar(2)


"""
Identificar si la suma de los dígitos de un numero es par o impar.
"""

def identificarParImpar(num1, num2):

     resultado = num1+num2

     if resultado % 2 == 0:

          print("El resultado de la suma es PAR")
     
     else:

          print("El resultado de la suma es IMPAR")


identificarParImpar(2,-2)


"""
Solicitar un número e imprimir los dígitos pares de este.
"""

def digitosNumero(num):


    for i in range(num):

          if i % 2 == 0:

               print(i, end=" ")

digitosNumero(100)


"""
Los números de las claves de dos cajas fuertes están mezcladas en un
número entero llamado clave maestra. Determine ambas claves, la primera
clave se construye con los dígitos impares de la clave maestra y la
segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135,
clave2=24.
"""

claveMaestra = input("Introduzca una clave númerica: ")
clave1 = ""
clave2 = ""

for i in range(len(claveMaestra)):

    if int(claveMaestra[i]) % 2 == 0:

        clave1 += claveMaestra[i]

    else:

        clave2 += claveMaestra[i]


print("Clave 1: ",clave1," || Clave 2: ",clave2)