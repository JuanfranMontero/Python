

"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
 pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

nombreMoneda = input("Introduce la moneda {}: ".format(monedas.keys()))

if nombreMoneda in monedas:

    print(monedas[nombreMoneda])

else:

    print("La moneda introducida no esta almacenada.")

    aniadirMoneda = input("Deseas añadir la mondeda (S/N): ")

    if aniadirMoneda.lower() == 's':

        if nombreMoneda not in monedas:

            simboloMoneda = input("Introduce el simbolo de la moneda: ")

            monedas[nombreMoneda] = simboloMoneda

        else:

            print("La moneda ya existe.")
    
    else:

        print("Ok! Hasta luego!")


"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
 Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

datos = {}

nombre = input("Introduce su nombre: ")
edad = int(input("Introduce su edad: "))
direccion = input("Introduce su dirección: ")
telefono = int(input("Introduce su telefono: "))


datos["Nombre"] = nombre
datos["Edad"] =  edad
datos["Dirección"] = direccion
datos["Telefono"] = telefono

print("{} tiene {} años, vive en {} y su número de telefono es {}.".format(datos.get("Nombre"), datos.get("Edad"), datos.get("Dirección"), datos.get("Telefono")))


"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Platano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70

"""

precioFruta = {'Platano' : 1.35, 'Manzana' : 0.80, 'Pera' : 0.85, 'Naranja' : 0.70}

nombreFruta = input("Introduce el nombre de la fruta: ")

if nombreFruta in precioFruta.keys():

    peso = int(input("Introduce cuantos Kilos quieres: "))

    print("El importe a pagar las {} es de {}€.".format(nombreFruta, peso * precioFruta.get(nombreFruta)))
else:

    print("Actualmente no tenemos esa fruta disponible, Lo siento!")