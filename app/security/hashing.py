import hashlib
from config import SECRET_WORD

def hash_password(password: str) -> str:
    result = hashlib.sha256(password.encode())
    return result.hexdigest()




