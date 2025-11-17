from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# Base de datos en memoria para las pruebas o SQlite local

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=False)
sessionLocal = sessionmaker(bind=engine)