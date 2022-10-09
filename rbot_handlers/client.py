from aiogram import types
from aiogram.dispatcher import FSMContext
import keyboard as kb
from create_bot import bot
import asyncio
from database import sqlite_db as sql
from rbot_handlers.states import FSMAdmin


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
        await sql.add_reminder(
            dict(user_id=message.from_user.id,
                 text=data['text'],
                 time=data['date']))
        # await message.answer()
        await state.finish()


async def check_tasks():
    for task in await sql.select_reminder():
        await bot.send_message(task["user_id"], task['time'])
        await sql.delete_reminder(task["id"])


def repeat_check_tasks(loop):
    asyncio.ensure_future(check_tasks(), loop=loop)
    loop.call_later(2, repeat_check_tasks, loop)


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Добавление записи отменено')


