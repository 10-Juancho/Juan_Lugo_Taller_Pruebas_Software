import pytest
from user_service import UserService

# ---------------------------
# PRUEBAS CONTRA SQL INJECTION
# ---------------------------

def test_sql_injection_prevention():
    user_service = UserService()

    # Intento de SQL Injection
    payload = "user'; DROP TABLE users; --"

    with pytest.raises(ValueError):
        user_service.add_user(payload)

# ---------------------------
# PRUEBAS CONTRA XSS
# ---------------------------

def test_xss_prevention_script_tag():
    user_service = UserService()

    payload = "<script>alert('xss')</script>"

    with pytest.raises(ValueError):
        user_service.add_user(payload)

def test_xss_prevention_html_js():
    user_service = UserService()

    payload = "<img src=x onerror=alert('hack')>"

    with pytest.raises(ValueError):
        user_service.add_user(payload)

# ---------------------------
# PRUEBA DE INSERTAR DATOS VALIDOS
# ---------------------------

def test_valid_user_addition():
    user_service = UserService()

    username = "juan123"
    user_service.add_user(username)

    assert username in user_service.get_users()