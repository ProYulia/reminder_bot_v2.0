from aiogram.utils import executor
from create_bot import dp
from rbot_handlers import client

if __name__ == '__main__':
    async def on_startup(_):
        print("Бот готов к работе")

    client.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
