from telegram import Update
from telegram.ext import ContextTypes
from storage.users import get_user

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    nft_list = "\n".join(
        [f"> • {n['name']} — {n['value']}💰" for n in user["nfts"]]
    ) or "> Пусто…"

    text = (
        "> *Профиль игрока:*\n"
        f"> Баланс: **{user['balance']} 💰**\n"
        f"> NFT:\n{nft_list}"
    )

    await update.message.reply_text(text, parse_mode="Markdown")
