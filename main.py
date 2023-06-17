from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from inline import *
from Keyboard import *
from config import token

#44556677

bot = Bot(token)
dp = Dispatcher(bot=bot)

user_input = 0


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Starting bot"),
            types.BotCommand("help", "I will tell you what this bot does and how it will help you")
        ]
    )


@dp.message_handler(commands='help')
async def lng_uk(msg: types.Message):
    await dp.bot.send_message(msg.from_user.id, "This bot will help you determine the lifecell tariff that will suit you! If you are ready to start, click on the button.",reply_markup=srt)


@dp.callback_query_handler(text='start')
async def hlp(call: types.CallbackQuery):
    await call.message.answer("/start")


class St(StatesGroup):
    minutes = State()
    MB = State()
    message = State()


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
    user_input = 0


@dp.message_handler(text='commençons!')
async def start_selection_fr(msg: types.Message):
    await msg.answer("Combien de minutes par mois utilisez-vous habituellement ?")
    global user_input
    user_input = 0


@dp.message_handler(text='let\'s start!')
async def start_selection_en(msg: types.Message):
    await msg.answer("How many minutes per month do you usually use?")

    global user_input
    user_input = 0


@dp.message_handler()
async def save_user_input(msg: types.Message):



    global user_input
    user_input = msg.text

    if user_input.isdigit():
        await msg.answer("Let's go to the next stage!")
    else:
        await msg.answer("Try again")


@dp.callback_query_handler(text='start')
async def start_after_inline_button(call: types.CallbackQuery):
    await start(call.message)  # Викликати команду /start


def main():
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)


if __name__ == "__main__":
    main()
