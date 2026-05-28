from fastapi import APIRouter
from fastapi import HTTPException

from passlib.context import CryptContext

import jwt
import datetime

from loguru import logger


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

SECRET_KEY = "SUPER_SECRET_KEY"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Demo user database
fake_users = {
    "admin": {
        "username": "admin",
        "password": pwd_context.hash("admin123")
    }
}


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(username: str):

    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(hours=24)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token


@router.post("/login")
async def login(payload: dict):

    try:
        username = payload.get("username")
        password = payload.get("password")

        user = fake_users.get(username)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        valid = verify_password(
            password,
            user["password"]
        )

        if not valid:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token = create_access_token(username)

        logger.info(f"User logged in: {username}")

        return {
            "success": True,
            "access_token": token
        }

    except Exception as e:

        logger.error(f"Login Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }