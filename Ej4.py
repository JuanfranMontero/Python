
"""
Este programa pide primeramente la cantidad total de compras de una persona. 
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. 
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. 
Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. 
Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, 
sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, 
de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
"""

"""

import random

numElegido = 1

while numElegido != 0: 

    totalCompra = int(input("Introduce la cantidad de su compra: "))

    if totalCompra >= 100:

        print("Su gasto iguala o supera los 100€ y por tanto participa en la promoción.")

        print("         COLOR                DESCUENTO")
        print("")
        print("       BOLA BLANCA            NO TIENE")
        print("       BOLA ROJA                 10%")
        print("       BOLA AZUL                 20%")
        print("       BOLA VERDE                25%")
        print("       BOLA AMARILLA             50%")


        numAleatorio = random.randrange(1,6)

        if numAleatorio == 1:

            print("")
            print("NO HAS OBTENIDO NINGÚN DESCUENTO")
            print("")
            print("EL IMPORTE A PAGAR ES: ",totalCompra,"€.")

        elif numAleatorio == 2:

            print("")
            print("FELICIDADES, HAS OBTENIDO UN DESCUENTO DEL 10%")
            print("")
            print("EL IMPORTE A PAGAR ES: ", totalCompra - totalCompra * 0.10,"€.")

        elif numAleatorio == 3:

            print("")
            print("FELICIDADES, HAS OBTENIDO UN DESCUENTO DEL 20%")
            print("")
            print("EL IMPORTE A PAGAR ES: ", totalCompra - totalCompra * 0.20,"€.")

        elif numAleatorio == 4:

            print("")
            print("FELICIDADES, HAS OBTENIDO UN DESCUENTO DEL 25%")
            print("")
            print("EL IMPORTE A PAGAR ES: ", totalCompra - totalCompra * 0.25,"€.")

        elif numAleatorio == 5:

            print("")
            print("FELICIDADES, HAS OBTENIDO UN DESCUENTO DEL 50%")
            print("")
            print("EL IMPORTE A PAGAR ES: ", totalCompra - totalCompra * 0.50,"€.")

    else:

        print("Su compra no ha llegado al minimo para poder aplicar al descuento.")


    print(" ")
    numElegido = int(input("SI DESEA SALIR PRESIONE 0 O DE LO CONTRARIO PRESIONE OTRO NÚMERO: "))

"""

"""
De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. 
El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes 
códigos de productos con sus respectivas cantidades, 
y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras.
 Te animas??

"""


"""

importeFinal = 0
salir = False

while not salir:

    print("ELIJA UN PRODUCTO")
    print("")
    print("PRODUCTO         CÓDIGO")
    print("Camiseta-------------1")
    print("Pantalon-------------2")
    print("Zapatillas-----------3")
    print("Gorra----------------4")
    print("Pulsera--------------5")

    print("")

    codigoElegido =  int(input("Introduce el código: "))

    if codigoElegido == 1:

        precioProducto = 10
    
    elif codigoElegido == 2:

        precioProducto = 15
    
    elif codigoElegido == 3:

        precioProducto = 20

    elif codigoElegido == 4:

        precioProducto = 25
    
    elif codigoElegido == 5:

        precioProducto = 30

    else:

        print("El código introducido no se encuentra disponible.")

    
    cantidadProducto = int(input("¿Cuantas unidades deseas?: "))


    if cantidadProducto != 0:

        importeTotal = precioProducto * cantidadProducto
        importeFinal += importeTotal

    print("")
    eleccion = input("Si desea continuar pulse S, si desea salir pulse N: ")
    print("")

    if eleccion == 'N' or eleccion == 'n':

        salir = True

        print("")
        print("--- FACTURA ---")
        print("El total de su pedido es: ", importeFinal,"€.")
        print("")

"""