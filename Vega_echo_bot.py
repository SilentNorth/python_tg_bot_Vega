from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher(bot)


@dp.message_handler(content_types=["dice", "animation", "text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "pinned_message", "poll_option", "poll_answer", "poll"])
async def echo_send(message: types.Message):

    await bot.copy_message(message.chat.id, message.chat.id, message.message_id)


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)