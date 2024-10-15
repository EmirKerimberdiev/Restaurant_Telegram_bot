from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

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


@review_router.message(Command('review'))
async def review_handler(message: types.Message, state: FSMContext):
    # Выставляем состояние диолога на review.name
    await state.set_state(RestourantReview.name)
    await message.answer("Как вас зовут?")

    if message.from_user.id not in list_tg_ids:
        list_of_clients.append(message.from_user.id)
    else:
        await state.clear()
        await message.answer("Вы уже проходили опрос!")


@review_router.message(Command('stop'))
@review_router.message(F.text == "стоп")
async def stop_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен !")


@review_router.message(RestourantReview.name)
async def review_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Введите ваш номер телефона")


@review_router.message(RestourantReview.phone_number)
async def review_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего посещения нашего заведения -День/Месяц/Год-")


@review_router.message(RestourantReview.visit_date)
async def review_age(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="★"),
                types.KeyboardButton(text="★ ★"),
                types.KeyboardButton(text="★ ★ ★"),
                types.KeyboardButton(text="★ ★ ★ ★"),
                types.KeyboardButton(text="★ ★ ★ ★ ★")
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Оцените наше меню и вкус нашего кофе", reply_markup=kb)


@review_router.message(RestourantReview.food_rating)
async def review_age(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await state.set_state(RestourantReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="★"),
                types.KeyboardButton(text="★ ★"),
                types.KeyboardButton(text="★ ★ ★"),
                types.KeyboardButton(text="★ ★ ★ ★"),
                types.KeyboardButton(text="★ ★ ★ ★ ★")
            ]
        ],
        resize_keyboard=True,
    )
    await message.answer("Оцените чистоту и обстоновку нашего заведения", reply_markup=kb)


@review_router.message(RestourantReview.cleanliness_rating)
async def review_gender(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Это дополнительный комментарий здесь вы можете написать всё что угодно.")


@review_router.message(RestourantReview.extra_comments)
async def review_genre(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)

    data = await state.get_data()
    list_of_clients.append(data)
    print(list_of_clients)

    await state.clear()
    await message.answer("Спасибр за пройденный опрос!!!")
