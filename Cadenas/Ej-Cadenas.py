
"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre =  input("Ingrese su nombre: ")
repeticiones = int(input("Introduce un número mayor a 0: "))

for i in range(repeticiones):

    print(nombre)


"""
Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombreCompleto = input("Introduzca su nombre completo: ")

print(nombreCompleto.lower())
print(nombreCompleto.upper())
print(nombreCompleto.title())

"""
Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> 
es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

nombre = input("Introduce su nombre: ")

print(nombre.upper(),"tiene ",len(nombre),"letras")


"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
 donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
 Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo
  y la extensión.
"""

numTelefono = input("Introduce su número de télefono: ")

print(numTelefono.split('-')[1])


"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""

frase = input("Introduce una frase: ")

for i in reversed(frase):

    print(i,end="")


"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input("Introduce una frase: ")

vocal = input("Introduce una vocal: ")

for i in frase:

    if i.lower() == vocal.lower():

        print(i.upper(), end="")
    
    else:

        print(i, end="")


"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""

correo = input("Introduce su correo electrónico: ")

print(correo.split('@')[0]+"@ceu.es")


"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
 muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

precio = input("Introduce el precio: ")

print(precio.split('.')[0],"euros con",precio.split('.')[1],"céntimos")


"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
 el día, el mes y el año.
  Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha = input("Introduce una fecha (dd/mm/aaaa): ")

datosFecha = fecha.split('/')

print("Dia: ", datosFecha[0])

if len(datosFecha[1]) < 2:

    print("Mes: ",'0'+datosFecha[1])

else:

    print("Mes: ",datosFecha[1])


print("Año: ", datosFecha[2])


"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
 y muestre por pantalla cada uno de los productos en una línea distinta.
"""

productos = input("Introduce sus productos separados por ',' : ")

listadoProductos =  productos.split(',')

for i in range(len(listadoProductos)):

    print(listadoProductos[i])


