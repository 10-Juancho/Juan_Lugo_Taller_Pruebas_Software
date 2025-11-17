from sqlalchemy.orm import session
from models import User

def register_user(db: session, username: str, email: str):
    """
    Registrar un nuevo usuario y lo guarda en la base de datos.

    """
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def authenticate_user(db: session, username: str, email: str):
    """
    Verificar si un usuario existe conese username y email.
    """
    return db.query(User).filter_by(username=username,email=email).first()