from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from rbot_handlers import client as cl
from rbot_handlers.states import FSMAdmin


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cl.command_start, commands=['start', 'help'])
    dp.register_message_handler(cl.command_create, commands='Создать_напоминание', state=None)
    dp.register_message_handler(cl.cancel, state="*", commands='Отменить')
    dp.register_message_handler(cl.cancel, Text(equals='Отменить', ignore_case=True), state="*")
    dp.register_message_handler(cl.set_text, state=FSMAdmin.text)
    dp.register_message_handler(cl.set_date, state=FSMAdmin.date)