import logging
import asyncio
from aiogram import Bot, Dispatcher
from app.config import bot, dp, TOKEN
from app.handler import router
from aiogram.fsm.storage.memory import MemoryStorage

dp = Dispatcher(storage=MemoryStorage())
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())