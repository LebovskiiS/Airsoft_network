import os
from logger import logger
from dotenv import load_dotenv


TEMPLATES_PATH = os.getcwd() + '/templates'

load_dotenv(override= False)

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")
SECRET_WORD=os.getenv("SECRET_WORD")


logger.debug('config loaded')
logger.debug(f'{DB_HOST},{DB_NAME},{DB_USER},{DB_PORT},{DB_PASSWORD}')
