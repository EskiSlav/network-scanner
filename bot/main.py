from modules import User, Msg
import logging
from typing import OrderedDict
from database import Database
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.environ.get("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    
    user = User(
        tg_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    msg = Msg(
        user_id=message.from_user.id,
        text=message.text,
        direction='from',
        message_id=message.message_id
    )
    db.insert_user(user)
    db.insert_message(msg)
    print(user)
    print(msg)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    user = User(
        tg_id=message.from_user.id,
        is_bot=message.from_user.is_bot,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    msg = Msg(
        user_id=message.from_user.id,
        text=message.text,
        direction='from',
        message_id=message.message_id
    )

    db.insert_user(user)
    db.insert_message(msg)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)