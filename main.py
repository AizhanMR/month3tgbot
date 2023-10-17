import asyncio
from aiogram.types import BotCommand
from logging import basicConfig


from bot import dp, bot
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.tourist_agency import agency_router


async def main():
    await bot.set_my_commands(
        [
            BotCommand(command='start', description='Главная'),
            BotCommand(command='pic', description='Картинка')
        ]
    )

    # роутеры
    dp.include_router(start_router)
    dp.include_router(agency_router)

    # в самом конце
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    basicConfig(level='INFO')
    asyncio.run(main())