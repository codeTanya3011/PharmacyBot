import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

# Загружаем токен из переменных окружения
TOKEN = os.getenv("TOKEN")
PAYMENT_PROVIDER_TOKEN = os.getenv("PORTMONE_TOKEN")
MANAGER = os.getenv('MANAGER')

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()