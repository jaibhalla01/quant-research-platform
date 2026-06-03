from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings


SQLALCHEMY_DATABASE_URL = settings.database_url

# Connection to the DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates database sessions on demand.
# Each request or operation typically gets its own session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency function that provides sessions to our routes
def get_db():
    with SessionLocal() as db:
        yield db
