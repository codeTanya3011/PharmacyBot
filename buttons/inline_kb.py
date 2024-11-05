from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


commands_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Предостережения! Обязательно к прочтению!", callback_data="show_warnings")],
    [InlineKeyboardButton(text="Симптомы", callback_data="show_symptoms"),
     InlineKeyboardButton(text="Лечение", callback_data="show_treatment")],
    [InlineKeyboardButton(text="Детям", callback_data="show_children"),
     InlineKeyboardButton(text="Сайт с инструкциями", url="https://tabletki.ua/ru/")],
    [InlineKeyboardButton(text="Отзывы", url="https://t.me/pharmacy_group5")],
    [InlineKeyboardButton(text="Обратная связь", url="https://t.me/sweet_girl_669")]
])


treatment_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Важно! Рекомендую к прочтению!", callback_data="important")],
    [InlineKeyboardButton(text="(1-5)", callback_data="numbering_one"),
     InlineKeyboardButton(text="(6-10)", callback_data="numbering_two")],
    [InlineKeyboardButton(text="(11-15)", callback_data="numbering_three"),
     InlineKeyboardButton(text="(16-20)", callback_data="numbering_four")],
    [InlineKeyboardButton(text="(21-25)", callback_data="numbering_five"),
     InlineKeyboardButton(text="(26-30)", callback_data="numbering_six")],
    [InlineKeyboardButton(text="(31-36)", callback_data="numbering_seven"),
     InlineKeyboardButton(text="(37-43)", callback_data="numbering_eight")],
    [InlineKeyboardButton(text="Вернуться к главному меню", callback_data="back_to_main")]
])


children_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Важно! Рекомендую к прочтению!", callback_data="important_kids")],
    [InlineKeyboardButton(text="(1-6)", callback_data="number_one"),
     InlineKeyboardButton(text="(7-12)", callback_data="number_two")],
    [InlineKeyboardButton(text="(13-18)", callback_data="number_three"),
     InlineKeyboardButton(text="(19-24)", callback_data="number_four")],
    [InlineKeyboardButton(text="(25-34)", callback_data="number_five"),
     InlineKeyboardButton(text="(35-42)", callback_data="number_seven")],
    [InlineKeyboardButton(text="Вернуться к главному меню", callback_data="back_to_main")]
])
