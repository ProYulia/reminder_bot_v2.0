from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    text = State()
    date = State()
