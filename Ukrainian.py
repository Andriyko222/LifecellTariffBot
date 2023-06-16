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

@dp.callback_query_handler(text='українська')
async def lng(call: CallbackQuery):
    await call.message.answer("Ласкаво просимо до нашого Telegram-бота Lifecell! Ми готові допомогти вам підібрати ідеальний тарифний план, який повністю задовольнить ваші потреби в спілкуванні. Наш бот пропонує зручний спосіб отримати персоналізовані рекомендації на основі звичного використання послуг зв’язку. Почнемо?", reply_markup=Keyboard2)


@dp.message_handler()
async def go(msg: types.Message):
    if msg.text == "Давайте розпочнемо!":
        await msg.answer("Скільки хвилин на місяць ви зазвичай використовуєте?")

if __name__ == "__main__":
    executor.start_polling(dp)