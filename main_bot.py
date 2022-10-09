from aiogram.utils import executor
from create_bot import dp, loop
from rbot_handlers import client
from rbot_handlers import handlers


if __name__ == '__main__':
    async def on_startup(_):
        print("Бот готов к работе")

    handlers.register_handlers_client(dp)
    loop.call_later(5, client.repeat_check_tasks, loop)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, loop=loop)


