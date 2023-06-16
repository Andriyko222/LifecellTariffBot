from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import CallbackQuery
from inline import *
from Keyboard import *
from config import token

bot = Bot(token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("select language", reply_markup=ikb1)

@dp.callback_query_handler(text='english')
async def lng(call: CallbackQuery):
    await call.message.answer("Welcome to our Lifecell Telegram bot! We are ready to help you find the ideal tariff plan that will fully meet your communication needs. Our bot offers a convenient way to get personalized recommendations based on your usual use of communication services. Shall we begin?", reply_markup=Keyboard1)


@dp.message_handler()
async def go(msg: types.Message):
    if msg.text == "let's start!":
        await msg.answer("How many minutes per month do you usually use?")

if __name__ == "__main__":
    executor.start_polling(dp)