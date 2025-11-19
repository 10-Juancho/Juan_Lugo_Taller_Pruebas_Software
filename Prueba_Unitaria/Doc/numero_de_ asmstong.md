# 🧮 NUMERO NARCISISTA.
El numero narcisita tambien llamado numero de (asmtrong), es un numero que es igual a la suma de sus propios digitos elevados a la potencia del numero total de digitos.
### Ejemplo.
Numero = 153 -> Tiene tres digitos <br>
#### Se calcula.
```text
13^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```
## 🧑‍💻 FUNCIÓN DE ARMSTRONG
```python
def es_armstrong(numero):
    """
    Determina si un número es de Armstrong (narcisista).

    Un número de Armstrong es aquel que es igual a la suma de sus propios dígitos
    elevados a la potencia del número total de dígitos.
    """

    # Validar que sea un número entero positivo
    if not isinstance(numero, int) or numero < 0:
        return False

    # Convertir el número a cadena para poder iterar sus dígitos
    digitos = str(numero)
    cantidad = len(digitos)

    # Calcular la suma de cada dígito elevado a la potencia de la cantidad de dígitos
    suma = sum(int(digito) ** cantidad for digito in digitos)

    # Comparar la suma con el número original
    return suma == numero
```
## 🧠 EXPLICACIÓN LOGICA DEL ALGORITMO.
1. Validación del numero -> Primero se verifica que el valor recibido sea: 
    - Un numero entero 
    - Mayor o igual a cero
        >si no cumple, retorna **False**   
2. Separación de digitos <br>
    Se convierte el numero en una cadena.
    ```python 
    digitos = str (numero)  
    ```
    Esto permite recorrer cada digito de manera individual.

3. Contar cuantos digitos tiene el numero.
    ```python
    Cantidad = len (digitos)
    ```
    Esto es necesario porque cada digito sera elevado a una potencia.
4. Elevar cada digito y sumarlos.
    ```python
    suma = sum(int(digito) ** cantidad for digito in digitos)
    ```
    Aqui ocurre la parte importante:
    - Se  toma cada dígito
    - Se convierte en entero
    - Se eleva al numero total de dígitos 
    - Se suman todos los resultados
5. Comparación final.
    ```python
    return suma == numero
    ``` 
    Si la suma coincide exactamente con el número original → ✔ es un número narcisista.<br>
    
    Si no coincide → ✘ no lo es.