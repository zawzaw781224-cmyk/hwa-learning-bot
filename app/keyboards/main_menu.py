from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐍 Python",
                callback_data="python",
            ),
            InlineKeyboardButton(
                "⚡ FastAPI",
                callback_data="fastapi",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 SQL / PostgreSQL",
                callback_data="sql",
            ),
            InlineKeyboardButton(
                "🌐 Frontend",
                callback_data="frontend",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔐 Security",
                callback_data="security",
            ),
            InlineKeyboardButton(
                "🚀 Deployment",
                callback_data="deployment",
            ),
        ],
        [
            InlineKeyboardButton(
                "📚 Roadmap",
                callback_data="roadmap",
            ),
            InlineKeyboardButton(
                "🛠 Projects",
                callback_data="projects",
            ),
        ],
        [
            InlineKeyboardButton(
                "🧠 Quiz",
                callback_data="quiz",
            ),
            InlineKeyboardButton(
                "📖 Resources",
                callback_data="resources",
            ),
        ],
        [
            InlineKeyboardButton(
                "💡 Knowledge Share",
                callback_data="knowledge",
            ),
        ],
        [
            InlineKeyboardButton(
                "🛠 Common Error Fix",
                callback_data="error_fix",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def python_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐣 Basics",
                callback_data="python_basics",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔄 Control Flow",
                callback_data="python_control_flow",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ Functions",
                callback_data="python_functions",
            ),
        ],
        [
            InlineKeyboardButton(
                "🏗 OOP",
                callback_data="python_oop",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)

def fastapi_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 FastAPI Basics",
                callback_data="fastapi_basics",
            ),
        ],
        [
            InlineKeyboardButton(
                "🛣 Routing",
                callback_data="fastapi_routing",
            ),
        ],
        [
            InlineKeyboardButton(
                "📦 Pydantic",
                callback_data="fastapi_pydantic",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 Database",
                callback_data="fastapi_database",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔐 Authentication",
                callback_data="fastapi_auth",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)

def sql_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📌 SQL Basics",
                callback_data="sql_basics",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔍 SELECT & WHERE",
                callback_data="sql_select",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔗 JOIN",
                callback_data="sql_join",
            ),
        ],
        [
            InlineKeyboardButton(
                "📊 GROUP BY & Aggregate",
                callback_data="sql_group",
            ),
        ],
        [
            InlineKeyboardButton(
                "🐘 PostgreSQL",
                callback_data="postgresql",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def frontend_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🧱 HTML",
                callback_data="frontend_html",
            ),
        ],
        [
            InlineKeyboardButton(
                "🎨 CSS",
                callback_data="frontend_css",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚡ JavaScript",
                callback_data="frontend_javascript",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚛️ React",
                callback_data="frontend_react",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔗 API Integration",
                callback_data="frontend_api",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def security_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🔑 Authentication",
                callback_data="security_auth",
            ),
        ],
        [
            InlineKeyboardButton(
                "🪪 JWT",
                callback_data="security_jwt",
            ),
        ],
        [
            InlineKeyboardButton(
                "🛡️ CORS",
                callback_data="security_cors",
            ),
        ],
        [
            InlineKeyboardButton(
                "🚨 XSS",
                callback_data="security_xss",
            ),
        ],
        [
            InlineKeyboardButton(
                "💉 SQL Injection",
                callback_data="security_sql_injection",
            ),
        ],
        [
            InlineKeyboardButton(
                "🛡️ CSRF",
                callback_data="security_csrf",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def deployment_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐳 Docker",
                callback_data="deployment_docker",
            ),
        ],
        [
            InlineKeyboardButton(
                "☁️ Cloud",
                callback_data="deployment_cloud",
            ),
        ],
        [
            InlineKeyboardButton(
                "🚀 Render",
                callback_data="deployment_render",
            ),
        ],
        [
            InlineKeyboardButton(
                "▲ Vercel",
                callback_data="deployment_vercel",
            ),
        ],
        [
            InlineKeyboardButton(
                "🌐 Nginx",
                callback_data="deployment_nginx",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔒 HTTPS / SSL",
                callback_data="deployment_https",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def roadmap_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐍 Python Roadmap",
                callback_data="roadmap_python",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚡ Backend Roadmap",
                callback_data="roadmap_backend",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 Database Roadmap",
                callback_data="roadmap_database",
            ),
        ],
        [
            InlineKeyboardButton(
                "🚀 Deployment Roadmap",
                callback_data="roadmap_deployment",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def projects_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🟢 Beginner Projects",
                callback_data="projects_beginner",
            ),
        ],
        [
            InlineKeyboardButton(
                "🟡 Intermediate Projects",
                callback_data="projects_intermediate",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔴 Advanced Projects",
                callback_data="projects_advanced",
            ),
        ],
        [
            InlineKeyboardButton(
                "🏆 Portfolio Projects",
                callback_data="projects_portfolio",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def quiz_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐍 Python Quiz",
                callback_data="quiz_python",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚡ FastAPI Quiz",
                callback_data="quiz_fastapi",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 SQL Quiz",
                callback_data="quiz_sql",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔐 Security Quiz",
                callback_data="quiz_security",
            ),
        ],
        [
            InlineKeyboardButton(
                "🌐 Web / HTTP Quiz",
                callback_data="quiz_web",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def resources_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📚 Documentation",
                callback_data="resources_docs",
            ),
        ],
        [
            InlineKeyboardButton(
                "🎥 Learning Videos",
                callback_data="resources_videos",
            ),
        ],
        [
            InlineKeyboardButton(
                "📄 Cheat Sheets",
                callback_data="resources_cheatsheets",
            ),
        ],
        [
            InlineKeyboardButton(
                "💻 GitHub Resources",
                callback_data="resources_github",
            ),
        ],
        [
            InlineKeyboardButton(
                "🌐 Useful Websites",
                callback_data="resources_websites",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def knowledge_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 Web Development",
                callback_data="knowledge_web",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ Backend Tips",
                callback_data="knowledge_backend",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 Database Tips",
                callback_data="knowledge_database",
            ),
        ],
        [
            InlineKeyboardButton(
                "🔐 Security Tips",
                callback_data="knowledge_security",
            ),
        ],
        [
            InlineKeyboardButton(
                "💡 General Knowledge",
                callback_data="knowledge_general",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
def error_fix_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "🐍 Python Errors",
                callback_data="error_python",
            ),
        ],
        [
            InlineKeyboardButton(
                "⚡ FastAPI Errors",
                callback_data="error_fastapi",
            ),
        ],
        [
            InlineKeyboardButton(
                "🗄 Database Errors",
                callback_data="error_database",
            ),
        ],
        [
            InlineKeyboardButton(
                "🌐 Frontend Errors",
                callback_data="error_frontend",
            ),
        ],
        [
            InlineKeyboardButton(
                "🚀 Deployment Errors",
                callback_data="error_deployment",
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_main",
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)