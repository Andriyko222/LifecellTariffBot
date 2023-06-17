from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from inline import *
from Keyboard import *
from config import token
from  parsVilnLife import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

user_input = {}


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Starting bot"),
        types.BotCommand("help", "I will tell you what this bot does and how it will help you")
    ])


@dp.message_handler(commands='help')
async def help_command(msg: types.Message):
    await dp.bot.send_message(msg.from_user.id, "This bot will help you determine the lifecell tariff that will suit you! If you are ready to start, click on the button.", reply_markup=srt)


@dp.callback_query_handler(text='start')
async def start_callback(call: types.CallbackQuery):
    await call.message.answer("/start")


class St(StatesGroup):
    minutes = State()
    MB = State()


@dp.message_handler(commands='start')
async def start_command(msg: types.Message):
    await msg.answer("Select language", reply_markup=ikb1)


@dp.callback_query_handler(text='українська')
async def lang_uk_callback(call: types.CallbackQuery):
    await call.message.answer("Ласкаво просимо до нашого Telegram-бота Lifecell! Ми готові допомогти вам підібрати ідеальний тарифний план, який повністю задовольнить ваші потреби в спілкуванні. Наш бот пропонує зручний спосіб отримати персоналізовані рекомендації на основі звичного використання послуг зв’язку. Почнемо?", reply_markup=Keyboard2)


@dp.callback_query_handler(text='французька')
async def lang_fr_callback(call: types.CallbackQuery):
    await call.message.answer("Bienvenue sur notre bot Lifecell Telegram ! Nous sommes prêts à vous aider à trouver le plan tarifaire idéal qui répondra pleinement à vos besoins de communication. Notre bot offre un moyen pratique d'obtenir des recommandations personnalisées en fonction de votre utilisation habituelle des services de communication. Allons-nous commencer?", reply_markup=Keyboard3)


@dp.callback_query_handler(text='english')
async def lang_en_callback(call: types.CallbackQuery):
    await call.message.answer("Welcome to our Lifecell Telegram bot! We are ready to help you find the ideal tariff plan that will fully meet your communication needs. Our bot offers a convenient way to get personalized recommendations based on your usual use of communication services. Shall we begin?", reply_markup=Keyboard1)


@dp.message_handler(text=['Давайте розпочнемо!', 'commençons!', "let's start!"])
async def start_selection(msg: types.Message):
    if msg.text == 'Давайте розпочнемо!':
        await msg.answer("Скільки хвилин на місяць ви зазвичай використовуєте?")
        await St.minutes.set()
    elif msg.text == 'commençons!':
        await msg.answer("Combien de minutes par mois utilisez-vous habituellement ?")
        await St.minutes.set()
    elif msg.text == "let's start!":
        await msg.answer("How many minutes per month do you usually use?")
        await St.minutes.set()


@dp.message_handler(state=St.minutes)
async def process_minutes(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    user_input[user_id] = {'minutes': msg.text}
    await msg.answer("Скільки мегабайт на місяць ви зазвичай використовуєте?")
    await St.MB.set()


@dp.message_handler(state=St.MB)
async def process_MB(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    user_input[user_id]['MB'] = msg.text

    await state.finish()
    await msg.answer("Дякуємо за відповіді! Отримані дані:\n"
                     f"Хвилини: {user_input[user_id]['minutes']}\n"
                     f"Мегабайти: {user_input[user_id]['MB']}\n"
                     "Зачекайте декілька секунд, і ми напишемо який тариф вам підходить.")


@dp.message_handler(state=St.MB)
async def process_MB(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    user_input[user_id]['MB'] = int(msg.text)

    await state.finish()

    minutes = user_input[user_id]['minutes']
    mb = user_input[user_id]['MB']
    tariff = ""

    if minutes <= 100 and mb <= 500:
        tariff = "Просто Лайф"
    elif minutes <= 300 and mb <= 1000:
        tariff = "Смарт Лайф"
    elif minutes <= 500 and mb <= 2000:
        tariff = "Вільний Лайф"
    elif minutes <= 1000 and mb <= 5000:
        tariff = "Platinum Лайф"
    else:
        tariff = "Шкільний Лайф"

    await msg.answer(f"Рекомендуємо вам обрати тариф: {tariff}")


def main():
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)


if __name__ == "__main__":
    main()
