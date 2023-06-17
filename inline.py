from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton("English",callback_data='english')
button2 = InlineKeyboardButton("Українська",callback_data='українська')
button3 = InlineKeyboardButton("Français",callback_data='французька')


ikb1 = InlineKeyboardMarkup().add(button1,button2,button3)


