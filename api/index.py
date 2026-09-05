import os

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
)

from app.handlers.start import start
from app.handlers.menu import menu_callback


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

application = (
    Application.builder()
    .token(BOT_TOKEN)
    .updater(None)
    .build()
)

application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(menu_callback))


async def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed",
        }

    data = await request.json()

    update = Update.de_json(data, application.bot)

    await application.initialize()

    try:
        await application.process_update(update)
    finally:
        await application.shutdown()

    return {
        "statusCode": 200,
        "body": "OK",
    }