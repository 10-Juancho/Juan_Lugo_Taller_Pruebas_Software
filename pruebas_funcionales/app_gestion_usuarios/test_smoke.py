from user_manager import UserManager

def test_user_manager_smoke():
    user_manager = UserManager()
    
    # Crear usuario
    user = user_manager.create_user("user1", "user1@example.com")
    assert user["username"] == "user1"
    assert len(user_manager.users) == 1

    # Eliminar usuario
    user_manager.delete_user("user1")
    assert len(user_manager.users) == 0