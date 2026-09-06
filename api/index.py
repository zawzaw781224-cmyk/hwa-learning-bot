import os

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler

from app.handlers.start import start
from app.handlers.menu import menu_callback
from telegram.ext import MessageHandler, filters
from app.handlers.ai import ai_handler


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

telegram_app = (
    Application.builder()
    .token(BOT_TOKEN)
    .updater(None)
    .build()
)

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CallbackQueryHandler(menu_callback))
telegram_app.add_handler(
    MessageHandler(filters.Mention("HWA_Learning_Bot"), ai_handler)
)

app = FastAPI()


@app.post("/api/telegram")
async def telegram_webhook(request: Request):
    data = await request.json()

    update = Update.de_json(
        data=data,
        bot=telegram_app.bot,
    )

    await telegram_app.initialize()

    try:
        await telegram_app.process_update(update)
    finally:
        await telegram_app.shutdown()

    return PlainTextResponse("OK")