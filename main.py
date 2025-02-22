import asyncio
import logging


from bot_config import dp, database
from handlers import (
    start,
    other_message,
    info,
    review_dialog
)

async def main():
    start.register_handlers(dp)
    info.register_handlers(dp)
    review_dialog.register_handlers(dp)
    other_message.register_handlers(dp)
    database.create_tables()
    await dp.start_polling()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


