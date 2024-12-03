from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from config import DB_PASSWORD,DB_PORT,DB_USER,DB_HOST,DB_NAME
from logger import logger

class Base(DeclarativeBase):
    pass


engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Base.metadata.create_all(engine)
logger.debug('db initialized')