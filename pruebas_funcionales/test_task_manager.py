from task_manager import TaskManager

def test_task_management_uat():
    task_manager = TaskManager()

    # --- UAT 1: Agregar una tarea ---
    task = task_manager.add_task("Comprar comida")
    assert task["title"] == "Comprar comida"
    assert task["completed"] is False
    assert task in task_manager.tasks

    # --- UAT 2: Editar una tarea ---
    edited_task = task_manager.edit_task(task, "Comprar comida y frutas")
    assert edited_task["title"] == "Comprar comida y frutas"

    # --- UAT 3: Completar una tarea ---
    completed_task = task_manager.complete_task(task)
    assert completed_task["completed"] is True

    # --- UAT 4: Eliminar una tarea ---
    result = task_manager.delete_task(task)
    assert result is True
    assert task not in task_manager.tasks
