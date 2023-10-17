from aiogram import types
from aiogram.filters import Command

@dp.message(Command('pic'))
async def pic(message: types.Message):
    file = types.FSInputFile('images/kesha.jpg')
    await message.answer_photo(file)