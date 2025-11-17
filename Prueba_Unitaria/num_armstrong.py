def es_armstrong(numero):
    """
    Determina si un número es de Armstrong (narcisista).

    Un número de Armstrong es aquel que es igual a la suma de sus propios dígitos
    elevados a la potencia del número total de dígitos.
    """

    # Validar que sea un numero entero positivo
    if not isinstance(numero, int) or numero < 0:
        return False
    # Converir el numero  a una cadena de texto para poder iterar los digitos
    digitos = str(numero)
    cantidad = len(digitos)

    # Calcular la suma de cada digito elvado a la potencia de la cantidad de digitos

    suma = sum(int(digito)** cantidad for digito in digitos)

    # Comparar la suma con el numero original
    return suma == numero