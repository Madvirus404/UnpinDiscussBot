import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# 1. Токен получаем из переменной окружения
TOKEN = os.getenv("BOT_TOKEN", "ВСТАВЬТЕ_ВАШ_ТОКЕН_ЗДЕСЬ")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Ловим все сообщения, пришедшие из привязанного канала
@dp.message(F.is_automatic_forward)
async def unpin_channel_post(message: Message):
    try:
        # Открепляем пост
        await bot.unpin_chat_message(
            chat_id=message.chat.id, message_id=message.message_id
        )
    except Exception as e:
        print(f"Ошибка открепа: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())