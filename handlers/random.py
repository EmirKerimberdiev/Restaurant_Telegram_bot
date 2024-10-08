from aiogram import Router
from aiogram.filters.command import Command
from random import choice

randomaizer = Router()


def draniki_recipe():
    return """
    Драники (Картофельные оладьи):
    Ингредиенты:
    - 500 г картофеля
    - 1 луковица
    - 1 яйцо
    - 2 ст. ложки муки
    - Соль и перец по вкусу
    - Растительное масло для жарки

    Приготовление:
    1. Очистите картофель и лук. Натрите их на мелкой терке.
    2. Отожмите лишнюю жидкость из картофеля.
    3. Добавьте яйцо, муку, соль и перец. Хорошо перемешайте.
    4. Разогрейте сковороду с маслом и выкладывайте тесто ложкой, формируя небольшие лепешки.
    5. Обжаривайте с двух сторон до золотистой корочки. Подавать со сметаной.
    """


def pancakes_recipe():
    return """
    Панкейки (Американские блинчики):
    Ингредиенты:
    - 1 стакан муки
    - 1 стакан молока
    - 1 яйцо
    - 2 ст. ложки сахара
    - 1 ч. ложка разрыхлителя
    - Щепотка соли
    - Растительное масло для жарки

    Приготовление:
    1. Смешайте муку, сахар, разрыхлитель и соль.
    2. В отдельной миске взбейте яйцо с молоком.
    3. Добавьте жидкие ингредиенты к сухим и аккуратно перемешайте до однородной массы.
    4. Разогрейте сковороду и смажьте маслом. Выливайте тесто небольшими порциями.
    5. Обжаривайте на среднем огне с каждой стороны до появления пузырьков и золотистой корочки.
    """


def tort_three_chocolates_recipe():
    return """
    Торт "Три шоколада":
    Ингредиенты:
    - 200 г темного шоколада
    - 200 г молочного шоколада
    - 200 г белого шоколада
    - 600 мл сливок 33-35%
    - 3 ст. ложки сахара
    - 300 г печенья (для основы)
    - 100 г сливочного масла
    - Желатин (по 1 ч. ложке на каждый слой)

    Приготовление:
    1. Основа: Измельчите печенье и смешайте с растопленным сливочным маслом. Выложите массу в разъемную форму и утрамбуйте. Охладите.
    2. Темный слой: Растопите темный шоколад. Взбейте 200 мл сливок с сахаром и желатином, добавьте растопленный шоколад. Вылейте на основу и охладите.
    3. Молочный слой: Аналогично приготовьте слой из молочного шоколада, вылейте его на первый слой. Охладите.
    4. Белый слой: Повторите с белым шоколадом. Вылейте и оставьте торт в холодильнике до полного застывания.
    """


def frikase_recipe():
    return """
    Фрикасе (из курицы):
    Ингредиенты:
    - 500 г куриного филе
    - 200 г шампиньонов
    - 200 мл сливок
    - 1 луковица
    - 1 ст. ложка муки
    - 50 г сливочного масла
    - Соль, перец по вкусу

    Приготовление:
    1. Нарежьте куриное филе и обжарьте его до золотистого цвета.
    2. В отдельной сковороде обжарьте лук и шампиньоны.
    3. Добавьте сливочное масло и муку, готовьте 1-2 минуты.
    4. Постепенно добавляйте сливки, доводите до загустения.
    5. Верните курицу в сковороду, перемешайте, тушите 10 минут. Подавать с гарниром по вкусу.
    """


def zharovnya_recipe():
    return """
    Жаровня:
    Ингредиенты:
    - 500 г свинины или говядины
    - 4-5 картофелин
    - 1 луковица
    - 2 моркови
    - 2 зубчика чеснока
    - Растительное масло для жарки
    - Соль, перец, специи по вкусу

    Приготовление:
    1. Нарежьте мясо кусочками и обжарьте его до золотистой корочки.
    2. Добавьте нарезанный лук и морковь, обжаривайте еще несколько минут.
    3. Нарежьте картофель крупными кусочками и добавьте в сковороду.
    4. Добавьте специи, залейте водой, чтобы она слегка покрывала ингредиенты.
    5. Тушите на медленном огне до готовности картофеля. В конце добавьте чеснок.
    """


def lagman_recipe():
    return """
    Лагман:
    Ингредиенты:
    - 500 г говядины
    - 200 г лагманной лапши
    - 2 луковицы
    - 2 болгарских перца
    - 2 моркови
    - 2-3 помидора
    - 2-3 зубчика чеснока
    - Зелень (кинза, петрушка)
    - Растительное масло
    - Соль, специи по вкусу (зира, паприка, кориандр)

    Приготовление:
    1. Нарежьте мясо кусочками и обжарьте на масле.
    2. Добавьте нарезанный лук, перец и морковь, обжаривайте 5-7 минут.
    3. Нарежьте помидоры и добавьте их к мясу с овощами, тушите до мягкости.
    4. Добавьте специи, чеснок, залейте водой или бульоном и тушите до готовности мяса.
    5. Отварите лагманную лапшу отдельно.
    6. Подавайте мясо с овощами на лапше, украсьте зеленью.
    """


@randomaizer.message(Command(commands=['random']))
async def random_handler(message):
    foods = ["Драники", "Панкейки", "Торт три шоколада", "Фрикасе", "Жаровня", "Лагман"]
    random_food = choice(foods)

    if random_food == "Драники":
        await message.answer(draniki_recipe())
    elif random_food == "Панкейки":
        await message.answer(pancakes_recipe())
    elif random_food == "Торт три шоколада":
        await message.answer(tort_three_chocolates_recipe())
    elif random_food == "Фрикасе":
        await message.answer(frikase_recipe())
    elif random_food == "Жаровня":
        await message.answer(zharovnya_recipe())
    elif random_food == "Лагман":
        await message.answer(lagman_recipe())
    else:
        await message.answer("Неизвестное блюдо")
