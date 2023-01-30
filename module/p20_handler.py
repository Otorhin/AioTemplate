import aiogram
from aiogram import types


def init(dp: aiogram.Dispatcher, bot: aiogram.Bot):

    @dp.message_handler(commands=["test"])
    async def handle(message: types.Message):
        nm = aiogram.types.Message()
        nm.from_user = message.from_user
        nm.chat = message.chat
        nm.text = "/start"
        await dp.message_handlers.notify(nm)

    @dp.callback_query_handler(text="test")
    async def handle(query: types.CallbackQuery):
        nq = aiogram.types.CallbackQuery()
        nq.from_user = query.from_user
        nq.message = query.message
        nq.data = "start"
        await dp.callback_query_handlers.notify(nq)
