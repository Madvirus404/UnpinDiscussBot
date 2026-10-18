import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# Запрашиваем токен из переменной окружения хостинга
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    sys.exit(
        "Ошибка: Переменная окружения 'BOT_TOKEN' не найдена. Укажите её в настройках хостинга."
    )

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Перехватываем все сообщения, автоматически пересланные из привязанного канала
@dp.message(F.is_automatic_forward)
async def unpin_channel_post(message: Message):
    try:
        # Открепляем пересланный пост
        await bot.unpin_chat_message(
            chat_id=message.chat.id, message_id=message.message_id
        )
    except Exception as e:
        print(f"Не удалось открепить сообщение {message.message_id}: {e}")


async def main():
    print("Бот успешно запущен и отслеживает посты...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())