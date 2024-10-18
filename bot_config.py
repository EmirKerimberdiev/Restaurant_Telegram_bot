from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from database.simpl_db import Database


token = dotenv_values(".env")['token']
bot = Bot(token=token)
dp = Dispatcher()
Database = Database("db.sqlite3")