
"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

nombre = input("Introduce su nombre: ")

contrasena = input("Introduzca su contraseña: ")

confirmacionContrasena = input("Confirme su contraseña: ")

if contrasena == confirmacionContrasena:

    print("¡Bienvenido {}!".format(nombre))

else:

    print("Lo sentimos, la contraseña no coincide.")


"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

numero = int(input("Introduzca un número: "))


if numero % 2 == 0:

    print(numero,"es PAR")

else:

    print(numero,"es IMPAR")


"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
 Escribir un programa que pregunte al usuario su edad y 
 sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

edad = int(input("Introduce su edad: "))

ingresos = int(input("Introduce sus ingresos: "))

if edad >= 16 and ingresos >= 1000:

    print("Debes tributar")

else:

    print("Aún no debes tributar.")

"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo (M o H)? ")

if genero == "M":

    if nombre.lower() < "m":

        grupo = "A"

    else:
        grupo = "B"

else:

    if nombre.lower() > "n":

        grupo = "A"

    else:

        grupo = "B"
        
print("Tu grupo es " + grupo)


"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

"""

rentaAnual =  int(input("Introduzca su renta anual: "))

if rentaAnual < 10000:

    print("Su impostivo es de 5%.")

elif 10000 < rentaAnual < 20000:

    print("Su impostivo es de 15%.")

elif 20000 < rentaAnual < 35000:

    print("Su impostivo es de 20%.")

elif 35000 < rentaAnual < 60000:

    print("Su impostivo es de 30%.")

else:

    print("Su impostivo es de 45%.")


"""
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

puntuacion = input("Introduce su puntuación: ")


if int(puntuacion.split('.')[1]) == 0:

    print("Su rendimiento es {}, la cantidad de dinero a percibir es de {}€".format('INACEPTABLE',2400))

elif int(puntuacion.split('.')[1]) == 4:

    print("Su rendimiento es {}, la cantidad de dinero a percibir es de {}€".format('ACEPTABLE',(2400 * int(puntuacion))))

elif int(puntuacion.split('.')[1]) >= 6:

    print("Su rendimiento es {}, la cantidad de dinero a percibir es de {}€".format('MERITORIO',(2400 * int(puntuacion))))


"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

opcionPizza = input("¿Deseas pizza vegetariana? (S/N): ")

opcionPizza = opcionPizza.lower()

if opcionPizza == 's':

    print("Eliga un ingrediente para su pizza (Mozarella y Tomate ya incluido)")
    eleccionIngrediente = input("- Pimiento  - Tofu : ")

    print("Has elegido una pizza vegetariana con los siguientes ingredientes: Mozzarela, Tomate y {}.".format(eleccionIngrediente))

elif opcionPizza == 'n':

    print("Eliga un ingrediente para su pizza (Mozarella y Tomate ya incluido)")
    eleccionIngrediente = input("- Peperoni  - Jamón  - Salmón :")

    print("Has elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarela, Tomate y {}.".format(eleccionIngrediente))