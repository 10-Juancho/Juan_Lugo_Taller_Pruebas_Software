# 📂 PRUEBA DE ESCALBILIDAD - SISTEMA DE GESTIÓN DE ARCHIVOS.
Se desarrolló un sistema básico para gestionar archivos en memoria, simulando una estructura sencilla donde se almacenan nombres de archivos.
- Características actuales:
- Permite agregar archivos al sistema.
- Simula una carga creciente para evaluar rendimiento.

El objetivo principal es realizar pruebas de escalabilidad para determinar si el rendimiento se mantiene cuando el número de archivos aumenta masivamente.

## 🌐 QUE SON LAS PRUBAS DE ESCALABILIDAD.
Las pruebas de escalabilidad permiten:
1. Evaluar cómo responde el sistema cuando la cantidad de datos o usuarios aumenta.
2. Identificar posibles cuellos de botella.
3. Comprobar si el sistema mantiene tiempos aceptables con grandes volúmenes de carga.

En este caso, se analiza el tiempo requerido para añadir 10.000 archivos a la estructura.

## ⚙️ IMPLEMENTACIÓN DEL SISTEMA.
``` Python
class FileSystem:
    # Clase FileSystem que representa un sistema simple para manejar archivos

    def __init__(self):

        # Constructor de la clase
        # Inicializa una lista vacía donde se almacenarán los archivos

        self.files = []

    def add_file(self, file):
        
        # Método para agregar un archivo al sistema
        # 'file' representa el archivo que se desea guardar
        # El archivo se añade a la lista 'files'

        self.files.append(file)
```
> Se está utilizando una lista en memoria como almacenamiento temporal.

## 🧪 PRUEBAS AUTOMATIZADAS DE ESCALABILIDAD (PYTEST).
``` Python
import time
from file_system import FileSystem

def test_scalability():
    fs = FileSystem()
    
    start_time = time.time()
    for i in range(10000):
        fs.add_file(f"file_{i}.txt")
    end_time = time.time()

    duration = end_time - start_time
    print(f"Tiempo requerido para añadir 10000 archivos: {duration} segundos")

    # Afirmación opcional: debe ejecutarse debajo de 1 segundo en entornos normales
    assert duration < 1.5

test_scalability ()
``` 
🏗️ Estrategia de la prueba:
- Crea una instancia del sistema de archivos.
- Inserta 10.000 archivos simulados.
- Mide el tiempo requerido.
- Opcionalmente valida que el tiempo sea aceptable

Se ejecuta : 
> python pruebas_no_funcionales/pruebas_escalabilidad/test_file_system.py 

o tambien.

> pytest pruebas_no_funcionales/pruebas_escalabilidadtest_file_system.py -v 