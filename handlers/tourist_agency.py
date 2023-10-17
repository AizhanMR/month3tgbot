from aiogram import types, Router, F
from aiogram.filters import Command
from handlers.start import start

agency_router = Router()

@agency_router.message(Command("travel"))
async def agency(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Тюрьма")],
            [
                types.KeyboardButton(text="Канализация"),
                types.KeyboardButton(text="комната"),
                types.KeyboardButton(text='назад')
            ],
        ],
        resize_keyboard=True,
    )
    await message.answer("Выберите локацию:", reply_markup=kb)

@agency_router.message(F.text.lower() == "назад")
async def start(message: types.Message):
    await start(message)

@agency_router.message(F.text.lower() == "тюрьма")
async def prison(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Наша тюрьма:', reply_markup=kb)
    file = types.FSInputFile('images/prison.jpg')
    await message.answer_photo(file)

@agency_router.message(F.text.lower() == "канализация")
async def sewer(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Канализация:', reply_markup=kb)
    file = types.FSInputFile('images/sewer.jpg')
    await message.answer_photo(file)

@agency_router.message(F.text.lower() == "комната")
async def room(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Комната:', reply_markup=kb)
    file = types.FSInputFile('images/room.jpg')
    await message.answer_photo(file)