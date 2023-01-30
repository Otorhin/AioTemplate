import aiogram
from aiogram import types
from database import User


def init(dp: aiogram.Dispatcher):

    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        user_id: int = message.from_user.id

        user: User = await User.get_or_none(id=user_id)
        if user:
            await message.reply("WoW! Я тебя помню!")
            print(user.id)
        else:
            await message.reply("UwU! Я тебя запомнил!")
            await User.create(id=user_id)
