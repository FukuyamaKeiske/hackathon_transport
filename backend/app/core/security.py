from jose import (
    JWTError,
    jwt
)
from typing import (
    Dict,
    Any
)

from .config import Settings

ALGORITHM = "HS256"

def create_access_token(data: dict) -> str:
    return jwt.encode(data.copy(), Settings.SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return
