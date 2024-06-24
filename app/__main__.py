import asyncio
from pyrogram import *
from pyrogram.errors import *

from app import bot, OWNER_ID
from app.src.core.plugins import loadPlugins

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()


async def main():
    await asyncio.gather(bot.start())
    await asyncio.gather(loadPlugins(), idle())



if __name__ == "__main__":
    # create_log_file()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())