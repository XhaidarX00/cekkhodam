import logging
import re
import time
from os import execvp
from sys import executable

from aiohttp import ClientSession
from pyrogram import *
from pyrogram.handlers import *
from pyrogram.types import *

from app.config import *

aiosession = ClientSession()

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSError", "TimeoutError", "OSErno"]:
            if X in record.getMessage():
                gas()

logging.basicConfig(filename='bot.log', level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

LOGS = logging.getLogger(__name__)



class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ubot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            device_model="DarUbot",
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        LOGGER(__name__).info(
            f"@{usr_bot_me.username} "
        )
        

    async def stop(self, *args):
        await super().stop()
        LOGGER(__name__).info("Bot stopped. Bye.")

bot = Bot()