from aiogram import Bot, Dispatcher, executor, types

from inline import *
from Keyboard import *
from config import token

bot = Bot(token)
dp = Dispatcher(bot=bot)

user_input = ""


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("Select language", reply_markup=ikb1)


@dp.callback_query_handler(text='українська')
async def lng_uk(call: types.CallbackQuery):
    await call.message.answer("Ласкаво просимо до нашого Telegram-бота Lifecell! Ми готові допомогти вам підібрати ідеальний тарифний план, який повністю задовольнить ваші потреби в спілкуванні. Наш бот пропонує зручний спосіб отримати персоналізовані рекомендації на основі звичного використання послуг зв’язку. Почнемо?", reply_markup=Keyboard2)


@dp.callback_query_handler(text='французька')
async def lng_fr(call: types.CallbackQuery):
    await call.message.answer("Bienvenue sur notre bot Lifecell Telegram ! Nous sommes prêts à vous aider à trouver le plan tarifaire idéal qui répondra pleinement à vos besoins de communication. Notre bot offre un moyen pratique d'obtenir des recommandations personnalisées en fonction de votre utilisation habituelle des services de communication. Allons-nous commencer?", reply_markup=Keyboard3)


@dp.callback_query_handler(text='english')
async def lng_en(call: types.CallbackQuery):
    await call.message.answer("Welcome to our Lifecell Telegram bot! We are ready to help you find the ideal tariff plan that will fully meet your communication needs. Our bot offers a convenient way to get personalized recommendations based on your usual use of communication services. Shall we begin?", reply_markup=Keyboard1)


@dp.message_handler(text='Давайте розпочнемо!')
async def start_selection(msg: types.Message):
    await msg.answer("Скільки хвилин на місяць ви зазвичай використовуєте?")
    global user_input
    user_input = ""


@dp.message_handler(text='commençons!')
async def start_selection_fr(msg: types.Message):
    await msg.answer("Combien de minutes par mois utilisez-vous habituellement ?")
    global user_input
    user_input = ""


@dp.message_handler(text='let\'s start!')
async def start_selection_en(msg: types.Message):
    await msg.answer("How many minutes per month do you usually use?")
    global user_input
    user_input = ""


@dp.message_handler()
async def save_user_input(msg: types.Message):
    global user_input
    user_input = msg.text
    print(user_input)  

if __name__ == "__main__":
    executor.start_polling(dp)
