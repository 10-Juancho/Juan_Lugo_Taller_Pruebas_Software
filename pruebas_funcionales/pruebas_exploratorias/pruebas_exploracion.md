#  🧩 PRUEBAS EXPLORATORIAS.
Se diseñó una plataforma simplificada de mensajería instantánea con las siguientes funcionalidades básicas:

- Envío de mensajes entre usuarios
- Registro interno de mensajes enviados
- Gestión inicial de contactos (simulada)
- Flujo básico de notificaciones (simulado)

El objetivo es validar el comportamiento del flujo principal “envío y recepción de mensajes” mediante pruebas exploratorias y pruebas automatizadas con pytest.

## 🎯 OBJETIVO DE LAS PRUEBAS.
Las pruebas buscan:
- Detectar errores funcionales y lógicos.
- Verificar que el flujo de envío y registro de mensajes funciona correctamente.
- Identificar posibles mejoras de usabilidad y consistencia.
- Evaluar posibles fallos en el manejo de contactos y notificaciones.

##  🧪 ALCANCE
        | METODO                      | CUBIERTO  |
        |-----------------------------|-----------| 
        | Envió de mensajes           | cumple    |
        | Almacenamiento de mensajes  | cumple    |
        | Gestión de contactos        | Basico    |
        | Notificaciones              | simuladas |
## ⚙️ CODIGO DE LA PLATAFORMA.
```Python
class MessagingPlatform:
    def __init__(self):
        self.messages = []
        self.contacts = set()
        self.notifications = []

    def add_contact(self, username):
        self.contacts.add(username)

    def send_message(self, user, message):
        # Validación: el usuario debe existir en contactos
        if user not in self.contacts:
            raise ValueError("Contact does not exist.")

        # Guardar mensaje
        self.messages.append({"user": user, "message": message})

        # Agregar notificación
        self.notifications.append(f"Nuevo mensaje de {user}")

    def get_messages(self):
        return self.messages

    def get_notifications(self):
        return self.notifications
```

### 🧠 ESTRATEGIA DE LAS PRUEBAS.

Se utilizó una aproximación de tipo Tours Testing, revisando funcionalidades desde diferentes ángulos:
- Tour del flujo principal: envío de mensajes desde el punto de vista del usuario.
- Tour de datos inválidos: mensajes vacíos, usuarios inexistentes, caracteres especiales.
- Tour de consistencia: verificar que el comportamiento sea coherente en cada acción.
- Tour de interfaz interna: analizar el estado interno (messages, contacts, notifications).

## 🧪 PRUEBAS (PYTEST).
```Python
from messaging_platform import MessagingPlatform
import pytest


# test envio correcto de mensaje.
def test_send_message():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    platform.send_message("user1", "Hola, ¿cómo estás?")
    
    assert len(platform.messages) == 1
    assert platform.messages[0]["message"] == "Hola, ¿cómo estás?"

# test envio de mensaje a contacto no existente.
def test_send_message_without_contact():
    platform = MessagingPlatform()

    with pytest.raises(ValueError):
        platform.send_message("user1", "Mensaje no permitido")

# test envio de mensaje vacio.  

def test_send_empty_message():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    platform.send_message("user1", "")

    assert platform.messages[-1]["message"] == ""

# test envio de mensaje muy largo.
def test_send_large_message():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    long_message = "A" * 10000
    platform.send_message("user1", long_message)

    assert len(platform.messages[-1]["message"]) == 10000

# test agregar contacto duplicado.
def test_add_duplicate_contact():
    platform = MessagingPlatform()
    platform.add_contact("user1")
    platform.add_contact("user1")

    assert len(platform.contacts) == 1

# test  validar las notificaciones 
def test_notifications_created():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    platform.send_message("user1", "Hola")

    assert platform.notifications[-1] == "Nuevo mensaje de user1"

# test para validar mensajes almacenados
def test_get_messages():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    platform.send_message("user1", "Primer mensaje")
    platform.send_message("user1", "Segundo mensaje")

    messages = platform.get_messages()

    assert len(messages) == 2
    assert messages[0]["message"] == "Primer mensaje"
    assert messages[1]["message"] == "Segundo mensaje"

# test validar la obtencion de notificaciones 
def test_get_notifications():
    platform = MessagingPlatform()
    platform.add_contact("user1")

    platform.send_message("user1", "Hola")

    notifications = platform.get_notifications()

    assert len(notifications) == 1
    assert notifications[0] == "Nuevo mensaje de user1"
```

Ejecución de las pruebas:

> pytest pruebas_funcionales/pruebas_exploratorias/test_messaging_platform.py -v