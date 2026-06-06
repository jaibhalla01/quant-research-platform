from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.settings import settings

# Convert to string so that it can be read by SQLAlchemy
SQLALCHEMY_DATABASE_URL = str(settings.database_url)

# Create the DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates database sessions on demand.
# Each request or operation typically gets its own session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency function that provides sessions to our routes
def get_db():
    with SessionLocal() as db:
        yield db
