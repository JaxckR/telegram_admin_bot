import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv


# Create .env file and write your api
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("TG_API"))
dp = Dispatcher()

# banwords
ban_words = ['delete', 'hate', 'goodbye']

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message) -> None:
    print("Bot is working")


@dp.message()
async def message_filter(message: Message) -> None:
    # await message.answer("Comment test")
    if message.text in ban_words:
        await message.delete()


if __name__ == '__main__':
    dp.run_polling(bot)
