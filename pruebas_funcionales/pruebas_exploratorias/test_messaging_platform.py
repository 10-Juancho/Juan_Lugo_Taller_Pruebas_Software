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