
"""
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

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



"""
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). 
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

"""

def calculaInteres(cantidadDinero, tasaInteres, anios):

     resultado = cantidadDinero * ( 1 + tasaInteres / 100) ** anios

     return resultado


print("El interés anual se converte en: {0:.2f}".format(calculaInteres(10000,4.5,20)),"€ en un plazo de 20 años")

"""
