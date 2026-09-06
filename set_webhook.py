import os

from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

WEBHOOK_URL = "https://hwa-learning-bot-smt.vercel.app/api/telegram"


async def main():
    bot = Bot(TOKEN)

    await bot.set_webhook(url=WEBHOOK_URL)

    print("✅ Webhook set successfully")
    print(await bot.get_webhook_info())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())