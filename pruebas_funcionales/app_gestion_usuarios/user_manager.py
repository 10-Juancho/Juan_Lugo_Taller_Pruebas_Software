class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, username, email):
        user = {"username": username, "email": email}
        self.users.append(user)
        return user

    def get_users(self):
        return self.users

    def delete_user(self, username):
        self.users = [u for u in self.users if u["username"] != username]