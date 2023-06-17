from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_comand import *
from inline import *
from Keyboard import *
from config import token

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class St(StatesGroup):
    language = State()
    minutes = State()
    MB = State()
    message = State()

@dp.message_handler(commands='help')
async def lng_uk(msg: types.Message):
    await dp.bot.send_message(msg.from_user.id, "This bot will help you determine the lifecell tariff that will suit you! If you are ready to start, click on the button.", reply_markup=srt)

@dp.callback_query_handler(text='start')
async def hlp(call: types.CallbackQuery):
    await call.message.answer("/start")

@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("Select language", reply_markup=ikb1)

@dp.callback_query_handler(text='українська')
async def lng_uk(call: types.CallbackQuery):
    await call.message.answer("Ласкаво просимо до нашого Telegram-бота Lifecell! Ми готові допомогти вам підібрати ідеальний тарифний план, який повністю задовольнить ваші потреби в спілкуванні. Наш бот пропонує зручний спосіб отримати персоналізовані рекомендації на основі звичного використання послуг зв’язку. Почнемо?", reply_markup=Keyboard2)
    await St.language.set()

@dp.callback_query_handler(text='французька')
async def lng_fr(call: types.CallbackQuery):
    await call.message.answer("Bienvenue sur notre bot Lifecell Telegram ! Nous sommes prêts à vous aider à trouver le plan tarifaire idéal qui répondra pleinement à vos besoins de communication. Notre bot offre un moyen pratique d'obtenir des recommandations personnalisées en fonction de votre utilisation habituelle des services de communication. Allons-nous commencer?", reply_markup=Keyboard3)
    await St.language.set()

@dp.callback_query_handler(text='english')
async def lng_en(call: types.CallbackQuery):
    await call.message.answer("Welcome to our Lifecell Telegram bot! We are ready to help you find the ideal tariff plan that will fully meet your communication needs. Our bot offers a convenient way to get personalized recommendations based on your usual use of communication services. Shall we begin?", reply_markup=Keyboard1)
    await St.language.set()

@dp.message_handler(state=St.language)
async def start_selection(msg: types.Message, state: FSMContext):
    language = msg.text.lower()
    await state.update_data(language=language)

    if language == 'українська':
        question = "Скільки хвилин на місяць ви зазвичай використовуєте?"
    elif language == 'французька':
        question = "Combien de minutes par mois utilisez-vous habituellement ?"
    else:
        question = "How many minutes per month do you usually use?"

    await msg.answer(question)
    await St.minutes.set()

@dp.message_handler(state=St.minutes)
async def save_user_minutes(msg: types.Message, state: FSMContext):
    user_minutes = msg.text

    if user_minutes.isdigit():
        await state.update_data(minutes=user_minutes)

        user_data = await state.get_data()
        language = user_data.get('language')

        if language == 'українська':
            question = "Скільки мегабайт на місяць ви зазвичай використовуєте?"
        elif language == 'французька':
            question = "Combien de mégaoctets utilisez-vous habituellement par mois?"
        else:
            question = "How many megabytes per month do you usually use?"

        await msg.answer(question)
        await St.MB.set()
    else:
        await msg.answer("Try again")

@dp.message_handler(state=St.MB)
async def save_user_MB(msg: types.Message, state: FSMContext):
    user_MB = msg.text

    if user_MB.isdigit():
        await state.update_data(MB=user_MB)
        await state.finish()

        await msg.answer("Thank you for providing the information!")
    else:
        await msg.answer("Try again")

def main():
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)

if __name__ == "__main__":
    main()
