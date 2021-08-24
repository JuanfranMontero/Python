

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



"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

fecha = input("Introduce una fecha (dd/mm/aaaa): ")


fecha =  fecha.split("/")

mes = ""

if fecha[1] == '1' or fecha[1] == '01':
    
    mes = "Enero"

elif fecha[1] == '2' or fecha[1] == '02':
    
    mes = "Febrero"

elif fecha[1] == '3' or fecha[1] == '03':
    
    mes = "Marzo"

elif fecha[1] == '4' or fecha[1] == '04':
    
    mes = "Abril"

elif fecha[1] == '5' or fecha[1] == '05':
    
    mes = "Mayo"

elif fecha[1] == '6' or fecha[1] == '06':
    
    mes = "Junio"

elif fecha[1] == '7' or fecha[1] == '07':
    
    mes = "Julio"

elif fecha[1] == '8' or fecha[1] == '08':
    
    mes = "Agosto"

elif fecha[1] == '9' or fecha[1] == '09':
    
    mes = "Septiembre"

elif fecha[1] == '10':
    
    mes = "Octubre"

elif fecha[1] == '11':
    
    mes = "Noviembre"


elif fecha[1] == '12':
    
    mes = "Dicimbre"


print("{} de {} de {}.".format(fecha[0], mes, fecha[2]))

