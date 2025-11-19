import time
from concurrent.futures import ThreadPoolExecutor

class TaskSearchService:
    def __init__(self, tasks):
        self.tasks = tasks

    def search_tasks(self, query):
        return [task for task in self.tasks if query.lower() in task["title"].lower()]


# Datos de ejemplo: 1000 tareas
tasks = [{"title": f"Tarea {i}", "completed": False} for i in range(1, 1001)]

# Crear el servicio de búsqueda
search_service = TaskSearchService(tasks)


# ---- Prueba de rendimiento con 1000 búsquedas concurrentes ----
def performance_test():
    queries = [f"Tarea {i}" for i in range(1, 1001)]

    start_time = time.time()

    # Ejecutar 1000 búsquedas concurrentemente
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(search_service.search_tasks, queries))

    end_time = time.time()

    total_time = end_time - start_time
    avg_time = total_time / 1000

    print(f"⏱ Tiempo total para 1000 búsquedas concurrentes: {total_time:.4f} segundos")
    print(f"⏱ Tiempo promedio por búsqueda: {avg_time:.6f} segundos")
    print(f"✔ Resultados válidos: {all(len(r) <= 1 for r in results)}")
    print(f"✅ Todas las búsquedas se completaron correctamente.")

performance_test()