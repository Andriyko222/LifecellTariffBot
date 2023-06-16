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

@dp.callback_query_handler(text='французька')
async def lng(call: CallbackQuery):
    await call.message.answer("Bienvenue sur notre bot Lifecell Telegram ! Nous sommes prêts à vous aider à trouver le plan tarifaire idéal qui répondra pleinement à vos besoins de communication. Notre bot offre un moyen pratique d'obtenir des recommandations personnalisées en fonction de votre utilisation habituelle des services de communication. Allons-nous commencer?", reply_markup=Keyboard3)


@dp.message_handler()
async def go(msg: types.Message):
    if msg.text == "commençons!":
        await msg.answer("Combien de minutes par mois utilisez-vous habituellement ?")

if __name__ == "__main__":
    executor.start_polling(dp)