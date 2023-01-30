import module
import logging
import config
import aiogram
from tortoise import Tortoise, run_async


logging.basicConfig(level=logging.INFO)
bot = aiogram.Bot(token=config.TG_TOKEN)
dp = aiogram.Dispatcher(bot)


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['database']}
    )
    await Tortoise.generate_schemas()
    logging.info("Tortoise inited!")


if __name__ == '__main__':
    module.init(bot=bot, dp=dp)
    run_async(init_db())
    aiogram.executor.start_polling(dp, skip_updates=True)
