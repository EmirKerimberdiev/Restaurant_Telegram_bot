from aiogram import Router, types, F
from aiogram.filters.command import Command

start_router = Router()


@start_router.message(Command(commands=['start']))
async def start_handler(message):
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
                                           url="https://www.google.com/search?sca_esv=fbf738c26e1a574b&rlz=1C1GCEA_enKG1025KG1025&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=ADLYWIIttH7f5OLdPFGiN2F6QxroPMJvsg:1728230649602&q=%D0%B0%D0%B4%D1%80%D0%B8%D0%B0%D0%BD%D0%BE&rflfq=1&num=10&sa=X&ved=2ahUKEwjakNbvkPqIAxWCFBAIHXYjKowQjGp6BAg5EAE&biw=1536&bih=738&dpr=1.25#rlfi=hd:;si:;mv:[[42.878836299999996,74.62437349999999],[42.820202099999996,74.58212]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!2m1!1e2!2m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:9")
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
            ]
        ]
    )

    await message.answer(f"Добро {name} пожаловать на бот Adriano, этот бот был создан для вашего удобста."
                         f"Этот бот был создан мной Тимуром Адриано.  Про то кто я и о истории нашего ресторанно "
                         f"почитайте в вкладке О нас.",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    text = ("Этот ресторан очень довно был основон человеком который ы называем Люи Адреано.\n\nОн оснавал этот "
            "ресторан очень давно, этот ресторан переходил поколение за поколением.\n\nТеперь же управляющий это я "
            "Тимур Адриано.")
    await callback.message.answer(text)


@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
    text = ("Возраст - от 18 до 25 лет.\nЗарплата - от 20000р. до 30000р.\nДолжность - "
            "официант.\nОбязанности - обслуживанник клиентов.\nУсловия - з/п, вакансии, обучение, повышение "
            "квалификации.\nТелефон - +996 000 000 000."
            "\n\n\nВсе вопросы по вакансиям можно задать Тимуру Адриано в личку или по телефону +996 000 000 000.")
    await callback.message.answer(text)
