from telegram import Update
from telegram.ext import ContextTypes

from app.services.ai_service import ask_ai


async def ai_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    message = update.effective_message

    if not message or not message.text:
        return

    question = message.text

    # Remove bot mention
    bot_username = context.bot.username

    if bot_username:
        question = question.replace(f"@{bot_username}", "").strip()

    if not question:
        await message.reply_text(
            "မေးခွန်းထည့်ပြီး Bot ကို mention လုပ်ပေးပါ 🤖"
        )
        return

    try:
        answer = ask_ai(question)

        await message.reply_text(answer)

    except Exception:
        await message.reply_text(
            "⚠️ AI response ရယူရာမှာ error ဖြစ်သွားပါတယ်။"
        )