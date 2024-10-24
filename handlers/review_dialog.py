from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database

review_router = Router()
list_of_clients = []
list_tg_ids = []


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == "review")
async def review_handler(callback: types.CallbackQuery, state: FSMContext):
    # if callback.from_user.id in list_tg_ids:
    #     await callback.message.answer("Вы уже проходили опрос!")
    #     return
    # else:
    #     list_tg_ids.append(callback.from_user.id)

    await state.set_state(RestourantReview.name)
    await callback.message.answer("Как вас зовут?")
    await callback.answer()


@review_router.message(RestourantReview.name)
async def review_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Введите ваш номер телефона")


@review_router.message(RestourantReview.phone_number)
async def review_phone_number(message: types.Message, state: FSMContext):
    num = message.text
    if not num.isdigit():
        await message.answer("Вводите только цифры")
        return
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата посещения нашего заведения (День/Месяц/Год)")


@review_router.message(RestourantReview.visit_date)
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


@review_router.message(RestourantReview.food_rating)
async def review_food_rating(message: types.Message, state: FSMContext):
    rating = message.text
    star_to_number = {
        "★": 1,
        "★ ★": 2,
        "★ ★ ★": 3,
        "★ ★ ★ ★": 4,
        "★ ★ ★ ★ ★": 5
    }
    if rating not in star_to_number:
        await message.answer("Выберите один из пяти звёзд")
        return

    await state.update_data(food_rating=star_to_number[rating])
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


@review_router.message(RestourantReview.cleanliness_rating)
async def cleanliness_rating(message: types.Message, state: FSMContext):
    rating = message.text
    star_to_number = {
        "★": 1,
        "★ ★": 2,
        "★ ★ ★": 3,
        "★ ★ ★ ★": 4,
        "★ ★ ★ ★ ★": 5
    }
    if rating not in star_to_number:
        await message.answer("Выберите один из пяти звёзд")
        return

    await state.update_data(cleanliness_rating=star_to_number[rating])
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительный комментарий: здесь вы можете написать всё, что угодно.")


@review_router.message(RestourantReview.extra_comments)
async def extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(review_extra_comments=message.text)

    data = await state.get_data()
    list_of_clients.append(data)
    print(list_of_clients)
    print(list_tg_ids)
    tg_id = message.from_user.id

    database.execute(
        query=("\n"
               "INSERT INTO database_for_data (name, phone_number, visit_date, food_rating, cleanliness_rating, "
               "review_extra_comments, tg_id)\n"
               "            VALUES (?, ?, ?, ?, ?, ?, ?)\n"
               "        "),
        params=(
            data['name'],
            data['phone_number'],
            data['visit_date'],
            data['food_rating'],
            data['cleanliness_rating'],
            data['review_extra_comments'],
            tg_id
        )
    )

    await state.clear(),
    await message.answer("Спасибо за пройденный опрос!")
