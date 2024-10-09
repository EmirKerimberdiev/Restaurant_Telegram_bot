from aiogram import Router, types
from aiogram.filters.command import Command

pic_router = Router()

@pic_router.message(Command(commands=['pic']))
async def pic_handler(message):
    # image = types.FSInputFile(rC:\Users\User\PycharmProjects\Restaurant_Telegram_bot\images\img.png
    # await message.answer_photo(image)
    await message.answer_photo(photo=types.FSInputFile(r'C:\Users\User\PycharmProjects\Restaurant_Telegram_bot\images\img.png'))


