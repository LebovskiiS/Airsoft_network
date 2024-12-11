from flask import Flask
from .auth import auth
from .events import events
from config import TEMPLATES_PATH
from logger import logger

app = Flask(__name__, template_folder= TEMPLATES_PATH)
app.register_blueprint(auth, url_prefix= '/auth')
app.register_blueprint(events, url_prefix= '/events')
logger.debug('The app started')