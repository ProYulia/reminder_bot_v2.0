from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as c
import asyncio


storage = MemoryStorage()
bot = Bot(token=c.r_token)
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
