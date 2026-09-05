import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from telegram.ext import CallbackQueryHandler
from app.handlers.menu import menu_callback

from app.handlers.start import start


load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def main():
    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))

    print("🤖 HWA Learning Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()