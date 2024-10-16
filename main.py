import asyncio
import logging

from handlers.randomy import random_router
from handlers.start import start_router
from handlers.pic import pic_router
from handlers.my_info import myinfo_router
from handlers.other import other
from handlers.review_dialog import review_router
from bot_config import bot, dp
from aiogram import Bot
from database.simpl_db import Database


async def on_startup(bot: Bot):
    await Database.create_table()


async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)

    dp.include_router(other)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
