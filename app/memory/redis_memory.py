import redis
import json

from loguru import logger


class RedisMemory:

    def __init__(
        self,
        host="localhost",
        port=6379,
        db=0
    ):

        try:
            self.redis_client = redis.Redis(
                host=host,
                port=port,
                db=db,
                decode_responses=True
            )

            logger.info("Redis connection established")

        except Exception as e:

            logger.error(f"Redis Connection Error: {e}")

    def save_memory(
        self,
        key: str,
        value: dict
    ):

        try:
            self.redis_client.set(
                key,
                json.dumps(value)
            )

            logger.info(f"Memory saved: {key}")

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Redis Save Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def get_memory(self, key: str):

        try:
            data = self.redis_client.get(key)

            if not data:

                return {
                    "success": False,
                    "message": "Memory not found"
                }

            return {
                "success": True,
                "data": json.loads(data)
            }

        except Exception as e:

            logger.error(f"Redis Get Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def delete_memory(self, key: str):

        try:
            self.redis_client.delete(key)

            logger.info(f"Memory deleted: {key}")

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Redis Delete Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }