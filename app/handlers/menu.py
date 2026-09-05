from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import (
    main_menu_keyboard,
    python_menu_keyboard,
)
from app.keyboards.main_menu import (
    main_menu_keyboard,
    python_menu_keyboard,
    fastapi_menu_keyboard,
    sql_menu_keyboard,
    frontend_menu_keyboard,
    security_menu_keyboard,
    deployment_menu_keyboard,
    roadmap_menu_keyboard,
    projects_menu_keyboard,
    quiz_menu_keyboard,
    resources_menu_keyboard,
    knowledge_menu_keyboard,
    error_fix_menu_keyboard
)

async def menu_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    if query.data == "python":

        await query.edit_message_text(
            "🐍 Python Learning\n\n"
            "Choose a topic:",
            reply_markup=python_menu_keyboard(),
        )

    elif query.data == "back_main":

        await query.edit_message_text(
            "🤖 HWA Learning Bot\n\n"
            "👋 Welcome to Backend Journey by HWA!\n\n"
            "What do you want to learn?",
            reply_markup=main_menu_keyboard(),
        )

    elif query.data == "fastapi":

        await query.edit_message_text(
            "⚡ FastAPI / Backend\n\n"
            "FastAPI learning section.",
        reply_markup=fastapi_menu_keyboard(),
        )

    

    elif query.data == "frontend":
        await query.edit_message_text(
            "🌐 Frontend\n\n"
            "Choose a topic:",
            reply_markup=frontend_menu_keyboard(),
        )

    elif query.data == "security":
        await query.edit_message_text(
            "🔐 Security\n\n"
            "Choose a topic:",
            reply_markup=security_menu_keyboard(),
        )

    elif query.data == "deployment":
        await query.edit_message_text(
            "🚀 Deployment\n\n"
            "Choose a topic:",
            reply_markup=deployment_menu_keyboard(),
        )

    elif query.data == "roadmap":
        await query.edit_message_text(
            "📚 Learning Roadmap\n\n"
            "Choose a roadmap:",
            reply_markup=roadmap_menu_keyboard(),
        )

    elif query.data == "projects":
        await query.edit_message_text(
            "🛠 Practice Projects\n\n"
            "Choose a category:",
            reply_markup=projects_menu_keyboard(),
        )

    elif query.data == "quiz":
        await query.edit_message_text(
            "🧠 Quiz\n\n"
            "Choose a quiz:",
            reply_markup=quiz_menu_keyboard(),
        )

    elif query.data == "resources":
        await query.edit_message_text(
            "📖 Resources\n\n"
            "Choose a resource category:",
            reply_markup=resources_menu_keyboard(),
        )

    elif query.data == "knowledge":
        await query.edit_message_text(
            "💡 Knowledge Share\n\n"
            "Choose a category:",
            reply_markup=knowledge_menu_keyboard(),
        )

    elif query.data == "error_fix":
        await query.edit_message_text(
            "🛠 Common Error Fix\n\n"
            "Choose an error category:",
            reply_markup=error_fix_menu_keyboard(),
        )

    elif query.data == "sql":
        await query.edit_message_text(
            "🗄 SQL / PostgreSQL\n\n"
            "Choose a topic:",
            reply_markup=sql_menu_keyboard(),
        )