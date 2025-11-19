# 📘 PRUEBAS DE INTEGRACIÓN CON SQLALCHEMY Y PYTEST
Este documento explica el proceso completo para implementar y ejecutar pruebas de integración en un sistema de gestión de usuarios utilizando SQLAlchemy como ORM y pytest como framework de pruebas.

La finalidad de estas pruebas es verificar que diferentes componentes del sistema funcionen correctamente en conjunto, especialmente los módulos de:
- Registro de usuarios
- Autenticación de usuarios
- Interacción con la base de datos
- ORM (SQLAlchemy)

## 🛠️ CONFIGURACIÓN DEL ENTORNO
Se creo el entorno virtual:
```bash 
python -m  venv  Pruebas_env 
```
Luego se activó:
```bash 
pruebas_env\Scripts\Activate
```
Instalación de dependecias principales.
```bash 
 pip install sqlalchemy 
 pip install pytest 
```
## ⚙️ CONFIGURACIÓN DE SQLALCHEMY
> 📄 data_base.py

Aqui se configura:
- El motor de la base de datos 
- La sesión
- El modelo base 

Para pruebas se usa SQLite en memoria:
```Python 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Base de datos en memoria para las pruebas o SQlite local

Base = declarative_base()
DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
```
## 🧱 DEFINICIÓN DEL MODELO 
>📄 models.py

Se creo el modelo **user**.
```Python
from sqlalchemy import Column, Integer, String
from src.data_base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
```
## 🔐 FUNCIONES DE REGISTRO Y UTENTICACIÓN
> 📄 auth.py

Se implementó:
- Registro de usuarios 
- Autenticación por **username** y **email** 
```Python
from sqlalchemy.orm import Session
from src.models import User

def register_user(db: Session, username: str, email: str):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, email: str):
    return db.query(User).filter_by(username=username, email=email).first()
```
## 🧪 PRUEAS DE INTEGRACIÓN
Archivo principal:
>📄 test_integration_auth.py

Incluye:
- Una base de datos en memoria por prueba.
- Creación del usuario.
- Verificación de persistencia en la base de datos.
- Autenticación correcta del usuario.
```Python
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
```

## ▶️ EJECUCIÓN DE LAS PRUEBAS.
Ejecuta todas las pruebas.
> Pytest -v

Ejecuta un archivo en especifico 
> pytest prueba_integracion/test_integration_auth.py -v

## 🏁Conclusiones 
Las pruebas de integración permiten validar que:
- SQLAlchemy se comunica correctamente con la base de datos
- El ORM funciona bien junto con las funciones de negocio
- El sistema es capaz de guardar y autenticar usuarios de forma integrada
- Los distintos módulos (database, models, auth) trabajan como un solo sistema

Gracias a estas pruebas, podemos asegurar que el flujo completo:
```
        Registro → Persistencisa → Consulta → Autenticación
```

funciona correctamente.