from fastapi import Depends
from sqlalchemy.orm import Session

from src.database.session import get_db, SessionLocal
from sqlalchemy import text
from typing import Annotated


def fastapi_query(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(text("SELECT 1"))

    return result


def practice_query(db=SessionLocal()):
    result = db.execute(text("SELECT 1"))

    return result


practice_query()

