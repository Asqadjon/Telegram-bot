import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Bot tokeningiz
BOT_TOKEN = "8786970733:AAHrqdlfmAv3VGndTJxPE9sZY7lIU2aCP8U"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Salom! Bot muvaffaqiyatli ishga tushdi va ishlashga tayyor.")

async def main():
    print("Bot Render'da ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
