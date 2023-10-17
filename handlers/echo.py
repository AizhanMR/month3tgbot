from aiogram import types, F, Router

echo_router = Router()

@echo_router.message(F.text == 'privet')
async def hi(message: types.Message):
    await message.answer('poka')

@echo_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)