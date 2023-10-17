from aiogram import types, Router, F
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Наше местополоежение", url="https://web.telegram.org")],
            [
                types.InlineKeyboardButton(
                    text="Наш твиттер", url="https://twitter.com"
                )
            ],
            [types.InlineKeyboardButton(text="О нас", callback_data="about_us")],
        ]
    )
    await message.reply(f"Привет {message.from_user.first_name}!", reply_markup=kb)


'about_us'.startswith('about')
'about_us'.endswith('us')


@start_router.callback_query(F.data.startswith("about"))
async def show_about_us(call: types.CallbackQuery):
    await call.message.answer('О нас: мы очень уважамая компания основание: 1398 год до н.э')
