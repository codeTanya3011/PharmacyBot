from aiogram.types import (ReplyKeyboardMarkup, KeyboardButtonPollType, KeyboardButton, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# TODO implements later
# # ЗАМЕТКИ

# def generate_main_menu() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text="")
#     builder.button(text="")
#     builder.button(text="")
#     builder.button(text="")
#     builder.adjust(1, 3)
#
#     return builder.as_markup(resize_keyboard=True)
#
# del_kbd = ReplyKeyboardRemove()
#
# start_kb3 = ReplyKeyboardBuilder()
# start_kb3.add(
#     KeyboardButton(text="Симптомы"),
#     KeyboardButton(text="Предостережения"),
#     KeyboardButton(text="Лечение"),
#     KeyboardButton(text="Детям"),
#     KeyboardButton(text="Отзывы"),
#     KeyboardButton(text="Обратная связь"),
# )
# start_kb3.adjust(2, 2, 2)

# button_symptoms = KeyboardButton(text="Симптомы")
# keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard.add(button_symptoms)

# start_kb3 = ReplyKeyboardBuilder()
# start_kb3.attach(start_kb2)
# start_kb3.row(KeyboardButton(text="Оставить отзыв"), )
#
# start_kb4 = ReplyKeyboardBuilder()
# start_kb4.attach(start_kb3)
# start_kb4.row(KeyboardButton(text="Обратная связь"), )

# test_kb = ReplyKeyboardMarkup(
#     _keyboard=[
#         [
#             KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
#         ],
#         [
#             KeyboardButton(text="Отправить номер ☎️", request_contact=True),
#             KeyboardButton(text="Отправить локацию 🗺️", request_location=True),
#         ],
#     ],
#     resize_keyboard=True
# )
# from aiogram.types import KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder
#
#
# def get_keyboard(
#         *btns: str,
#         placeholder: str = None,
#         request_contact: int = None,
#         request_location: int = None,
#         sizes: tuple[int] = (2,),
# ):

#     keyboard = ReplyKeyboardBuilder()
#
#     for index, text in enumerate(btns, start=0):
#
#         if request_contact and request_contact == index:
#             keyboard.add(KeyboardButton(text=text, request_contact=True))
#
#         elif request_location and request_location == index:
#             keyboard.add(KeyboardButton(text=text, request_location=True))
#         else:
#             keyboard.add(KeyboardButton(text=text))
#
#     return keyboard.adjust(*sizes).as_markup(
#         resize_keyboard=True, input_field_placeholder=placeholder)

# Логика на дальнейшее возможно для файла юзер

# # Для остальных кнопок можно оставить текущую логику

# elif callback_query.data == "show_reviews":
#     await callback_query.message.answer("Отзывы пользователей: все прошло отлично!")
#
# elif callback_query.data == "show_feedback":
#     await callback_query.message.answer("Свяжитесь с нами через форму обратной связи.")
#
# await callback_query.answer()  # Закрываем callback

# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f"номер получен")
#     await message.answer(str(message.contact))
#
#
# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f"локация получена")
#     await message.answer(str(message.location))
