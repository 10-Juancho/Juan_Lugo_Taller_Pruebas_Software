import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base import Base
from auth import register_user,authenticate_user
from models import User

@pytest.fixture
def db_session():
    """
    Crear una base de datos en memoria pra cada prueba.

    """
    engine = create_engine("sqlite:///:memory:", echo=False)
    TestingSessionLocal = sessionmaker(bind = engine)

    # Crear las tablas.
    Base.metadata.create_all(engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_register_user(db_session):
    """
    Prueba de integracion para registrar un usuario, 
    verificar que se guarde en la base de datos y 
    verificar la autenticacion correcta.

    """
    # Registrar un usuario 

    user = register_user(db_session, username = "juan123", email = "juan@example.com")

    # Asegurar que el usuario se creo correctamente
    assert user.id is not None
    assert user.username == "juan123"
    assert user.email == "juan@example.com"
    
    # Intento de autenticacion con las credenciales 
    auth_user = authenticate_user(db_session, username = "juan123", email = "juan@example.com")

    # verificar que el sistema autentica correcatamente

    assert auth_user is not None
    assert auth_user.username == user.username
    assert auth_user.email == user.email