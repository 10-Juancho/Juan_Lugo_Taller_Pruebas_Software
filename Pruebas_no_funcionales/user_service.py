import re

class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        # Detectar caracteres peligrosos o patrones SQL/XSS
        if re.search(r"('|;|--|<script>|</script>|<|>)", username):
            raise ValueError("Input contains invalid characters.")

        self.users.append(username)

    def get_users(self):
        return self.users