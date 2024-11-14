from flask import Flask
from .auth import auth
from config import TEMPLATES_PATH

app = Flask(__name__, template_folder= TEMPLATES_PATH)
app.register_blueprint(auth, url_prefix= '/auth')