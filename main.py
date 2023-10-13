import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
from logging import basicConfig


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}')

@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await message.answer(f'your id is: {message.from_user.id}')
    await message.answer(f'your first name is: {message.from_user.first_name}')
    await message.answer(f'your username: {message.from_user.username}')


@dp.message(Command('pic'))
async def pic(message: types.Message):
    file = types.FSInputFile('images/sewer.jpg')
    await message.answer_photo(file)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())