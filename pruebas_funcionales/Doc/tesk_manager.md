# 📝 SISTEMA DE GESTIÓN DE TAREAS.
El sistema de gestión de tareas permite a los usaurios.
- Agregar tareas.
- Editar tareas.
- Completar tareas.
- Eliminar tareas.

El objetivo es validar que el flujo completo, cumpla con los requerimientos del usuario final.

## 🧪 PRUEBAS UAT (User Acceptance Testing).
Estas pruebas simulan el flujo real que seguiría un usuario final.

✔ Objetivo de las pruebas UAT
- Validar que el sistema es fácil de usar.
- Confirmar que permite agregar, editar, completar y eliminar correctamente.
- Validar que todo el flujo de trabajo es intuitivo y cumple los requisitos.

### PRUEBAS UAT PROPUESTAS.
```Python 
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

```

## 📌 EXPLICACIÓN DE CADA PRUEBA.

- UAT 1 - Agregar tarea.
    - EL usuario quiere registrar una nueva tarea.

- UAT 2 - Editar tarea.
    - El usuario se da cuenta que necesita modificar el titulo.
    - La prueba confirma que el cambio se aplique corretamente.

- UAT 3 - Completar tarea.
    - EL usuario marca la tarea como realizada.
    - La prueba asegura que el estado cambia a **true**
- UAT 4 - Eliminar tarea.

    - El usuario borra la tarea de su lista.
    - Se valida la tarea desaparece del sistema. 