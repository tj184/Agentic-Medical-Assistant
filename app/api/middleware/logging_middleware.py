import time

from starlette.middleware.base import BaseHTTPMiddleware

from loguru import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        logger.info(
            f"Incoming Request: "
            f"{request.method} {request.url.path}"
        )

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"Completed "
            f"{request.method} {request.url.path} "
            f"in {process_time:.4f} sec"
        )

        return response