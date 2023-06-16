from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

button1 = KeyboardButton("let's start!")
Keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1)

button2 = KeyboardButton("Давайте розпочнемо!")
Keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button2)

button3 = KeyboardButton("commençons!")
Keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3)