from sqlmodel import create_engine, SQLModel, Session
from env_configuration import settings
import os

sql_file = f"{settings.path}/{str(settings.database_file_name)}"

connect_args = {"check_same_thread": False}
sqlite_url = f"sqlite:///{sql_file}"
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
