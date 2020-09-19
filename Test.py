from Funciones import basic_ops, array_ops  # importar las funciones basic_ops
# y array_ops del archivo Funciones.py


def test_suma1():  # se testea que al sumar 2 numeros la respuesta sea correcta
    assert basic_ops(3, 2, "op_suma") == 5


def test_resta1():  # probando que al restar 2 numeros la respuesta es correcta
    assert basic_ops(8, 2, "op_resta") == 6


def test_or1():  # se testea que al aplicarle una operacion OR a 2 numeros
    # la respuesta sea correcta
    assert basic_ops(5, 3, "op_or") == 7


def test_and1():  # se testea que al aplicarle una operacion AND a 2 numeros
    # la respuesta sea correcta
    assert basic_ops(3, 4, "op_and") == 0


def test_suma2():  # se testea que al sumar 2 arreglos de numeros la respuesta
    # sea correcta
    assert array_ops([1, 2, 3], [3, 4, 5], "op_suma") == [4, 6, 8]


def test_resta2():  # se testea que al restar 2 arreglos de numeros la
    # respuesta sea correcta
    assert array_ops([1, 2, 3], [3, 1, 8], "op_resta") == [-2, 1, -5]


def test_or2():  # se testea que al aplicarle una operacion or a 2 arreglos
    # de numeros la respuesta sea correcta
    assert array_ops([3, 2, 5], [3, 7, 9], "op_or") == [3, 7, 13]


def test_and2():  # se testea que al aplicarle una operacion AND a 2 arreglos
    # de numeros la respuesta sea correcta
    assert array_ops([1, 15, 3], [12, 4, 5], "op_and") == [0, 4, 1]


def test_error_noentero1():  # se testea que al ingresar un numero no entero,
    # ya sea en a o b, salte el mensaje de error correcto
    assert basic_ops(12.8, 2, "op_suma") == 5


def test_error_no8bits1():  # se testea que al ingresa un numero mayor a 8
    # bits, ya sea en a o b, salte el mensaje de error correcto
    assert basic_ops(130, 2, "op_suma") == 5


def test_error_operacion1():  # se testea que al ingresa una operacion
    # incorrecta salte el mensaje de error correcto
    assert basic_ops(1, 2, "op_multiplicacion") == 3


def test_error_noentero2():  # se testea que al ingresar los arreglos de
    # numeros ninguno sea un numero no entero, y que el mensaje de error
    # en caso contrario sea correcto
    assert array_ops([12.4, 4, 5], [1, 2, 3], "op_suma") == [5, 0, 1]


def test_error_no8bits2():  # se testea que al ingresar los arreglos de
    # numeros ningnuo sea mayur a 8 bits y que el mensaje de error en
    # caso contrario sea correcto
    assert array_ops([140, 4, 5], [1, 2, 3], "op_suma") == [5, 0, 1]


def test_error_operacion2():  # se testea que al ingresar una operacion
    # invalida se muestre el mensaje de error correcto
    assert array_ops([12, 4, 5], [1, 2, 3], "op_multiplicacion") == [5, 0, 1]
