from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

start_router = Router()
list_of_clients = []
list_tg_ids = []


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


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
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="otzyv")
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


@start_router.callback_query(F.data == "otzyv")
async def review_handler(callback: types.CallbackQuery, state: FSMContext):
    # Проверка, проходил ли пользователь опрос
    if callback.from_user.id in list_tg_ids:
        await callback.message.answer("Вы уже проходили опрос!")
        await callback.answer()
        return
    else:
        list_of_clients.append(callback.from_user.id)

    # Добавляем пользователя в список
    list_tg_ids.append(callback.from_user.id)

    # Устанавливаем состояние для RestourantReview.name
    await state.set_state(RestourantReview.name)
    await callback.message.answer("Как вас зовут?")
    await callback.answer()


@start_router.message(RestourantReview.name)
async def review_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Введите ваш номер телефона")


@start_router.message(RestourantReview.phone_number)
async def review_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата посещения нашего заведения (День/Месяц/Год)")


@start_router.message(RestourantReview.visit_date)
async def review_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="★"),
             types.KeyboardButton(text="★ ★"),
             types.KeyboardButton(text="★ ★ ★"),
             types.KeyboardButton(text="★ ★ ★ ★"),
             types.KeyboardButton(text="★ ★ ★ ★ ★")]
        ],
        resize_keyboard=True
    )
    await message.answer("Оцените наше меню и вкус нашего кофе", reply_markup=kb)


@start_router.message(RestourantReview.food_rating)
async def review_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await state.set_state(RestourantReview.cleanliness_rating)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="★"),
             types.KeyboardButton(text="★ ★"),
             types.KeyboardButton(text="★ ★ ★"),
             types.KeyboardButton(text="★ ★ ★ ★"),
             types.KeyboardButton(text="★ ★ ★ ★ ★")]
        ],
        resize_keyboard=True
    )
    await message.answer("Оцените чистоту и обстановку нашего заведения", reply_markup=kb)


@start_router.message(RestourantReview.cleanliness_rating)
async def review_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительный комментарий: здесь вы можете написать всё, что угодно.")


@start_router.message(RestourantReview.extra_comments)
async def review_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)

    # Сохраняем данные
    data = await state.get_data()
    list_of_clients.append(data)
    print(list_of_clients)

    await state.clear()
    await message.answer("Спасибо за пройденный опрос!", reply_markup=types.ReplyKeyboardRemove())
