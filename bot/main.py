import logging
from typing import OrderedDict

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5792605370:AAHH5pdOxnhumdC90LKJo_meooKGuoKajgo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    
    user = OrderedDict(
        id=message.from_user.id,
        is_bot=message.from_user.is_bot,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )
    msg = OrderedDict(
        user_id=message.from_user.id,
        text=message.text
    )
    print(user)
    print(msg)

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.parse_entities(as_html=True) + ". Дякую!")
    user = OrderedDict(
        id=message.from_user.id,
        is_bot=message.from_user.is_bot,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )
    msg = OrderedDict(
        user_id=message.from_user.id,
        text=message.text
    )
    print(user)
    print(msg)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)