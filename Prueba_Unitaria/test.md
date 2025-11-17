# 🧪 TEST DE LA FUNCIÓN 
Este documento explica cómo se realizan las pruebas unitarias para verificar que la función ***es_armstrong()***,  funciona correctamente utilizando **pytest**.
## 📌 ¿Qué es pytest?
pytest es un framework de pruebas para Python que permite:
- Escribir tests simples y legibles
- Automatizar casos de prueba
- Probar múltiples valores con **@pytest.mark.parametrize**
- Generar reportes rápidos y claros

## ▶ ¿CÓMO EJECUTAR LAS PRUEBAS?
1. Instalar pytest:
```bash 
    pip install pytest
```
2. Ejecutar todas ls pruebas del proyecto:
```bash 
    pytest -v 
```
3. Ejecutar el archivo especifico: 
```bash 
    pytest test_num_armstrong.py
```
## 🧑‍💻 CÓDIGO DE PRUEBAS.
```python
import pytest
from src.num_armstrong import es_armstrong

# ------------------------------
# Casos positivos: números Armstrong válidos
# ------------------------------
@pytest.mark.parametrize("numero", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                    153, 370, 371, 407,
                                    1634, 8208, 9474])
def test_numeros_armstrong(numero):
    assert es_armstrong(numero) == True

# ------------------------------
# Casos negativos: números que NO son Armstrong
# ------------------------------
@pytest.mark.parametrize("numero", [10, 100, 123, 200, 250, 300, 400,
                                    500, 600, 700, 800, 900,
                                    154, 3710, 9475])
def test_numeros_no_armstrong(numero):
    assert es_armstrong(numero) == False

# ------------------------------
# Casos de entrada no válida
# ------------------------------
@pytest.mark.parametrize("numero", [-1, -153, 3.14, "153", None, [], {}])
def test_entrada_no_valida(numero):
    assert es_armstrong(numero) == False

# ------------------------------
# Límite superior
# ------------------------------
def test_limite_superior():
    numero = 9999999  # Número grande que NO es Armstrong
    assert es_armstrong(numero) == False

# ------------------------------
# Límite inferior
# ------------------------------
def test_limite_inferior():
    numero = 0  # El menor número Armstrong
    assert es_armstrong(numero) == True

# ------------------------------
# Caso especial: número Armstrong con muchos dígitos
# ------------------------------
def test_numero_muchos_digitos():
    numero = 9926315  # Número Armstrong grande y verificado
    assert es_armstrong(numero) == True
```
## 🧠 EXPLICACIÓN DE LOS TIPOS DE PRUEBAS.
- PRUEBAS POSITIVAS : Comprueban que la función **True** para valores que si son asmstrong.

- PRUEBAS NEGATIVAS: Verificar que la función devuelve **False** para números que no cumplan la función.
- ENTRADAS INVALIDAS.<br>
Se comprueban valores que no seberian ser aceptados:
    - Negativos.
    - Flotantes.
    - Cadenas.
    - None.
    - Listas y diccionarios.
    > La funcion debe manejar estos errores.

- LIMITES: Se prueban los extremos del algoritmo.
    - El numero mas pequeño posible (0).
    - Numeros grandes donde podria fallar la logica.

- CASO ESPECIAL: Se prueba un número Armstrong de muchos digitos para asegurar que la función escale bien. 