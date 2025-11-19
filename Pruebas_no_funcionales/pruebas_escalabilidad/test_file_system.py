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