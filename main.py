import asyncio
import logging

from handlers.start import start_router
from handlers.pic import pic_router
from handlers.my_info import myinfo_router
from handlers.other import other
from handlers.random import randomaizer
from bot_config import bot, dp


async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(other)
    dp.include_router(randomaizer)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
