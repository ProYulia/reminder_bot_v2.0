import time

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import keyboard as kb
from create_bot import dp, bot
import datetime


class FSMAdmin(StatesGroup):
    text = State()
    date = State()


async def command_start(message):
    try:
        await bot.send_message(message.from_user.id, f"Рад тебя видеть, {message.from_user.first_name}!",
                               reply_markup=kb.keyboard)
        await message.delete()
    except:
        await message.reply(r"Чтобы общаться с ботом, напиши ему в ЛС https://t.me/oh_my_reminder_bot")


async def command_create(message):
    await FSMAdmin.text.set()
    await message.answer("О чем напомнить?")


async def set_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await FSMAdmin.next()
    await message.answer('Когда напомнить? (время в формате HH:MM)')


async def set_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        while current_time <= str(data['date']):
            time.sleep(5)
            if current_time == str(data['date']):
                await bot.send_message(message.from_user.id, "Напоминание! " + str(data['text']))
                break
        await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Добавление записи отменено')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_create, commands='Создать_напоминание', state=None)
    dp.register_message_handler(cancel, state="*", commands='Отменить')
    dp.register_message_handler(cancel, Text(equals='Отменить', ignore_case=True), state="*")
    dp.register_message_handler(set_text, state=FSMAdmin.text)
    dp.register_message_handler(set_date, state=FSMAdmin.date)

