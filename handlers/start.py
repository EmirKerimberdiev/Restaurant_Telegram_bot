from aiogram import Router, types, F
from aiogram.filters import Command

start_router = Router()
list_of_clients = []
list_tg_ids = []


@start_router.message(Command(commands=['start']))
async def start_handler(message: types.Message):
    name = message.from_user.first_name

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/adriano_restobar/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Наш адрес",
                                           url="https://www.google.com/search?q=%D0%B0%D0%B4%D1%80%D0%B8%D0%B0%D0%BD%D0%BE")
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ]
        ]
    )

    await message.answer(f"Добро пожаловать, {name}, в бот Adriano! Этот бот был создан для вашего удобства. "
                         f"Вы можете узнать о нашем ресторане, оставить отзыв, а также ознакомиться с нашими вакансиями.",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    text = ("Этот ресторан был основан Люи Адриано много лет назад. "
            "Ресторан передавался из поколения в поколение, и теперь им управляю я, Тимур Адриано.")
    await callback.message.answer(text)


@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
    text = ("Возраст - от 18 до 25 лет.\nЗарплата - от 20000р до 30000р.\nДолжность - официант.\n"
            "Обязанности - обслуживание клиентов.\nТелефон - +996 000 000 000.")
    await callback.message.answer(text)
