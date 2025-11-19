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