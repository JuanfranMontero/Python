
"""
Una PyME, tiene la siguiente estructura de pagos para sus 10 empleados: 

    -Un sueldo base

    -Una bonificación del 1% del sueldo base, por cada mes trabajado

    -Una asignación familiar del 5% del sueldo base, por cada hijo

La suma de los tres valores anteriores, conforman la “base imponible”.
Todos los empleados están en FONASA, así que deben cotizar el 7% de la base imponible en salud. 
Los empleados están en una de dos: 
    AFPs, la primera cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que la segunda cobra el 11.4%

"""

"""
a) Pida el ingreso de datos de los 10 empleados
y los almacene. Debe pedir: nombre, apellido, sueldo base, afap, fecha de ingreso
y cantidad de hijos.
"""

datosTrabajador = []
listaTrabajadores = {}

for i in range(2):

    nombre = input("Introduce su nombre: ")
    datosTrabajador.append(nombre)

    apellido = input("Introduce su apellido: ")
    datosTrabajador.append(apellido)

    sueldoBase = int(input("Introduce su sueldo base: "))
    datosTrabajador.append(sueldoBase)

    organismo = input("Introduce a que organismo perteneces (AFPs o FONASA): ")
    organismo = organismo.lower()
    datosTrabajador.append(organismo)

    fechaIngreso = input("Introduce su fecha de ingreso (DD/MM/AAAA): ")
    datosTrabajador.append(fechaIngreso)

    cantidadHijos = int(input("Introduce la cantidad de hijos: "))
    datosTrabajador.append(cantidadHijos)

    listaTrabajadores = datosTrabajador

    print(" ")


