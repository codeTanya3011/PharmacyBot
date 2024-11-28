import asyncio
from config import bot, dp  # Импортируем bot и dp из config
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router

ALLOWED_UPDATES = ['message, edited_message']


async def main():
    # Регистрируем роутеры
    dp.include_router(user_private_router)
    dp.include_router(user_group_router)

    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


