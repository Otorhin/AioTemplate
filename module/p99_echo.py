import aiogram
from aiogram import types


def init(dp: aiogram.Dispatcher):

    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)
