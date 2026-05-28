from datetime import datetime

from loguru import logger


class ConversationMemory:

    def __init__(self):

        self.conversations = {}

    def start_session(self, session_id: str):

        try:
            self.conversations[session_id] = []

            logger.info(
                f"Conversation session started: {session_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Session Start Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str
    ):

        try:
            if session_id not in self.conversations:
                self.start_session(session_id)

            self.conversations[session_id].append({
                "role": role,
                "message": message,
                "timestamp": str(datetime.now())
            })

            logger.info(
                f"Message added to session: {session_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Add Message Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def get_conversation(
        self,
        session_id: str
    ):

        try:
            conversation = self.conversations.get(
                session_id,
                []
            )

            return {
                "success": True,
                "conversation": conversation
            }

        except Exception as e:

            logger.error(f"Get Conversation Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def clear_conversation(
        self,
        session_id: str
    ):

        try:
            if session_id in self.conversations:
                del self.conversations[session_id]

            logger.info(
                f"Conversation cleared: {session_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Clear Conversation Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }