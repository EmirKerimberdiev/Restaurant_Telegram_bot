import asyncio
import logging

from handlers.start import start_router
from handlers.pic import pic_router
from handlers.my_info import myinfo_router
from handlers.other import other
from handlers.randomy import randomaizer_router
from bot_config import bot, dp


async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(other)
    dp.include_router(randomaizer_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
