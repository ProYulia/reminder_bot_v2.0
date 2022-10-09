import sqlite3
import aiosqlite
import datetime

file = 'database/reminder_bot.db'


def create_table():
   connect = sqlite3.connect(file)
   cursor = connect.cursor()
   cursor.execute(
       """
        CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user INTEGER,
        text VARCHAR(100),
        time INTEGER
        )"""
   )


async def add_reminder(task):
    async with aiosqlite.connect(file) as connect:
        await connect.execute(
            "INSERT INTO tasks (user, text, time) VALUES (?, ?, ?)",
            (
                str(task['user_id']),
                str(task['text']),
                str(task['time'])
            )
        )
        await connect.commit()


async def select_reminder():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    async with aiosqlite.connect(file) as connect:
        async with connect.cursor() as cursor:
            await cursor.execute("SELECT * FROM tasks WHERE time = ?", (current_time, ))
            result = await cursor.fetchall()
            result = [{"id": i[0],
                       "user_id": i[1],
                       "time": i[2],
                       "text": i[3]} for i in result]
            await connect.commit()
            return result


async def delete_reminder(id):
    async with aiosqlite.connect(file) as connect:
        await connect.execute("DELETE FROM tasks WHERE id == ?", (id, ))
        await connect.commit()

