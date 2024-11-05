import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router


from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']


async def delete_commands(bot: Bot):
    # Удаление всех команд
    await bot.delete_my_commands()
    # Установка пустого списка команд на случай, если команды не удаляются полностью
    await bot.set_my_commands([])

bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await delete_commands(bot)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES, none_stop=True)


if __name__ == '__main__':
    asyncio.run(main())
