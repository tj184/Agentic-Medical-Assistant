from starlette.middleware.base import BaseHTTPMiddleware

from fastapi.responses import JSONResponse

import jwt

from loguru import logger


SECRET_KEY = "SUPER_SECRET_KEY"


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        public_paths = [
            "/",
            "/docs",
            "/openapi.json",
            "/auth/login"
        ]

        if request.url.path in public_paths:
            return await call_next(request)

        auth_header = request.headers.get(
            "Authorization"
        )

        if not auth_header:

            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Authorization header missing"
                }
            )

        try:
            token = auth_header.split(" ")[1]

            jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

        except Exception as e:

            logger.error(f"JWT Error: {e}")

            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message": "Invalid token"
                }
            )

        response = await call_next(request)

        return response