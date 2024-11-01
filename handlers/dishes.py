from aiogram import F, Router, types
from aiogram.filters import Command

from bot_config import database

catalog_router = Router()

@catalog_router.message(Command("catalog"))
async def show_all_dishes(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Супы"),
                types.KeyboardButton(text="Вторые"),
            ],
            [
                types.KeyboardButton(text="Горячие напитки"),
                types.KeyboardButton(text="Холодные напитки"),
                types.KeyboardButton(text="Гарниры")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите категорию"
    )
    await message.answer("Выберите категорию блюда", reply_markup=kb)

def filter_category(message: types.Message):
    category1 = message.text
    categories = database.fetch(
        query="""SELECT * FROM category WHERE name = ? """,
        params=(category1,)
    )
    if categories:
        return {"category": category1[0]["name"]}
    else:
        return False

@catalog_router.message(filter_category)
async def show_dishes_by_category(message: types.Message):
    category = message.text
    print(f"Категория: {category}")

    dishes = database.fetch(
        query="""
            SELECT * FROM dishes 
            JOIN category ON dishes.category_id = category.id 
            WHERE category.name = ?
        """,
        params=(category,)
    )
    print(f"Блюда: {dishes}")

    if not dishes:
        await message.answer(f"Нет блюд в категории {category}")
        return

    await message.answer( f"{dish['name_of_Food']} - {dish['price']} ₽" for dish in dishes )
