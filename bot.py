from telegram.ext import Application, CommandHandler
from handlers.start import start
from handlers.profile import profile
from handlers.opencase import opencase

TOKEN = "8563555273:AAGcDgH9BgdeMdGH0fSCa3pEd9CJpSUwzPg"

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("opencase", opencase))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
