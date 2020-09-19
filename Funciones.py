# -*- coding: utf-8 -*-


def basic_ops(a, b, c):  # Funcion basicops, recibe como entrada dos operandos
    # los cuales son #numeros: a y b, y la entrada c se refiere al tipo de
    # operacion que se desea realizar
    if a < -127 or a > 127 or b < -127 or b > 127:  # Primero se toma en cuenta
        # el caso en el que los numeros sean muy grandes o pequenos
        return "Error: El numero es de mas de 8 bits"
    elif a != int(a) or b != int(b):  # Este es el caso en el que los numeros
        # ingresados no son enteros
        return "Error: El numero ingresado no es entero"
    else:  # En este caso los operandos a y b de entrada si cumplen co los
        # requerimientos y se procede a realizar la operacion
        if c == "op_suma":
            return a + b
        elif c == "op_resta":
            return a - b
        elif c == "op_and":
            return a & b
        elif c == "op_or":
            return a | b
        else:
            return "Error: Operacion invalida"
        # la funcion retorna la operacion de los numeros a y b que se desee,
        # si se ingresa una operacion invalida retorna Error


def array_ops(a, b, c):  # Funcion arrayops se encarga de hacer lo mismo que
    # la anterior pero con arreglos de una lista
    # las variables a b y c corresponden a arreglos
    if len(a) != len(b):
        return "Error: Arreglos de distinto tamano"
    else:
        cont = 0  # inicializa contador para el ciclo en 0
        array_out = []  # declara arreglo array_out
        while cont < len(a):  # este ciclo se encarga de realizar la operacion
            # con cada uno de los elementos de las listas
            i = a[cont]
            j = b[cont]
            operacion = basic_ops(i, j, c)  # llamamos a la operacion basicops,
            # para las variables que se refieren al espacio de la lista
            array_out.append(operacion)  # se ingresa el resultado de operacion
            # a la lista operacion
            if operacion == "Error: El numero ingresado no es entero":  # en
                # estos cuatro casos, se verifica que los requerimientos de
                # cada uno de los elementos de la lista se cumplan
                # Si los requerimientos no se cumplen, el correspondiente
                # codigo de error sera retornado por la funcion
                return "Error: El arreglo posee numeros no enteros"
                break
            elif operacion == "Error: El numero es de mas de 8 bits":
                return "Error: El arreglo posee numeros de mas de 8 bits"
                break
            elif operacion == "Error: Operacion invalida":
                return "Error: Operacion invalida"
                break
            cont = cont + 1
        return array_out
