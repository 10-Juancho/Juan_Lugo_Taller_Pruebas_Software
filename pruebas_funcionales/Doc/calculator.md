# 🧮 PRUEBAS DE REGRESIÓN - CALCULADORA BASICA.
Se desarrolló una calculadora básica en Python con las siguientes funcionalidades:
- Suma-
- Resta
- Multiplicación (por implementar)
- División (por implementar)

El objetivo es aplicar pruebas de regresión para garantizar que, a medida que se agregan nuevas funciones, las anteriores continúen funcionando correctamente.

## 🎯 QUE SON LAS PRUEBAS DE REGRESIÓN.
Las pruebas de regresión tienen como finalidad:
- Comprobar que cambios recientes en el código no rompen funcionalidades ya existentes.
- Detectar errores introducidos mientras evoluciona el software.
- Mantener estabilidad en cada versión.
- Son especialmente útiles cuando el sistema irá creciendo de forma iterativa.

## ⚙️ CODIGO CALCULADORA.
```python
class Calculator:
    # Clase Calculator que agrupa operaciones matemáticas básicas

    def add(self, a, b):
        # Método para sumar dos números
        # Retorna la suma de 'a' y 'b'
        return a + b
    
    def subtract(self, a, b):
        # Método para restar dos números
        # Retorna el resultado de 'a' menos 'b'
        return a - b

    def multiply(self, a, b):
        # Método para multiplicar dos números
        # Retorna el producto de 'a' por 'b'
        return a * b
    
    def divide(self, a, b):
        # Método para dividir dos números
        # Primero valida que el divisor no sea cero
        if b == 0:
            # Si b es 0, lanza un error indicando que la división entre cero no es válida
            raise ValueError("No se puede dividir entre 0")
        # Si no hay error, retorna el resultado de la división de 'a' entre 'b'
        return a / b    
```

## 🧪 TEST CALCULADORA  (PYTEST).
```python
from calculator import Calculator
import pytest

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 3) == 1
    assert calc.add(0, 0) == 0

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 10) == 0

def test_division():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(-6, 3) == -2

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)

```

### 🔁 ESTRATEGIA DE LAS PRUEBAS DE REGRESIÓN.  

Cada vez que se agregue una nueva funcionalidad (por ejemplo, multiplicación o división):
1. Ejecutar todas las pruebas existentes.

2. Garantizar que:
    - No fallan las pruebas anteriores.
    - No se introducen efectos secundarios.

3. Añadir nuevas pruebas para las funcionalidades recientemente desarrolladas.

Ejecutar las pruebas: 
> pytest pruebas_funcionales/prueba_regresion/test_calculator.py -v  