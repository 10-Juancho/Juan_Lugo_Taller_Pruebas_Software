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