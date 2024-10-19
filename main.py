import asyncio
import logging

from handlers.randomy import random_router
from handlers.start import start_router
from handlers.pic import pic_router
from handlers.my_info import myinfo_router
from handlers.admin_add_food import admin_Food_router
from handlers.other import other
from handlers.review_dialog import review_router
from bot_config import bot, dp, database
from aiogram import Bot


async def on_startup():
    print("База данных созданнна")
    database.create_table()


async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)
    dp.include_router(admin_Food_router)

    dp.include_router(other)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
