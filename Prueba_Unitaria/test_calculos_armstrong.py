import pytest
from num_armstrong import es_armstrong
# Casos positivos de numeros Armstrong

@pytest.mark.parametrize("numero", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474])
def test_numeros_armstrong(numero):
    assert es_armstrong(numero) == True

# Casos negativos de numeros no Armstrong

@pytest.mark.parametrize("numero", [10, 100, 123, 200, 250, 300, 400, 500, 600, 700, 800, 900, 154, 3710, 9475])
def test_numeros_no_armstrong(numero):
    assert es_armstrong(numero) == False

# Casos de entrada no valida
@pytest.mark.parametrize("numero", [-1, -153, 3.14, "153", None, [], {}])
def test_entrada_no_valida(numero):
    assert es_armstrong(numero) == False

# limite superior
def test_limite_superior():
    numero = 9999999  # Numero grande que no es Armstrong
    assert es_armstrong(numero) == False

# limite inferior
def test_limite_inferior():
    numero = 0  # El menor numero Armstrong
    assert es_armstrong(numero) == True 

# Caso especial: numero con muchos digitos
def test_numero_muchos_digitos():
    numero = 9926315  # Número Armstrong grande y verificado
    assert es_armstrong(numero) == True

