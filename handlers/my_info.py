from aiogram import Router
from aiogram.filters.command import Command

myinfo_router = Router()


@myinfo_router.message(Command(commands=['myinfo']))
async def myinfo_handler(message):
    name = message.from_user.first_name
    await message.answer(
        f'Ваше имя: {name}\nВаш id: {message.from_user.id}\nВаш username: {message.from_user.username}')
