from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Добро пожаловать в *NFT Case Bot*!\n\n"
        "Команды:\n"
        "/profile — Профиль\n"
        "/opencase 1-10 — открыть кейсы\n"
    )
