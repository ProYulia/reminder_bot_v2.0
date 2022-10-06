from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('/Создать_напоминание')
btn2 = KeyboardButton('/Отменить')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(btn1).add(btn2)