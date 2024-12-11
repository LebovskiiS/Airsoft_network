import jwt
import datetime
from config import SECRET_WORD
from app.models import session, User
from .hashing import hash_password

def generate_token(user_data: dict) -> str:
    token = jwt.encode(user_data, SECRET_WORD, algorithms= 'hs256')
    return token

def is_password_match(login_data: dict):
    username = login_data['login']
    password = hash_password(login_data['password'])
    result = session.get(User.password, User.username).match(password,username)
    if result:
        return True
    else:
        return False













