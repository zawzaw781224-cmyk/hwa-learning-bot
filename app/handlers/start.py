from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import main_menu_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 HWA Learning Bot\n\n"
        "👋 Welcome to Backend Journey by HWA!\n\n"
        "What do you want to learn?",
        reply_markup=main_menu_keyboard(),
    )