from aiogram import Bot, executor, Dispatcher, types
from config import token

bot = Bot(token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("the bot is working")


if __name__ == "__main__":
    executor.start_polling(dp)