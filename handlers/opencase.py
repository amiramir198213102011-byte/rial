import random
from telegram import Update
from telegram.ext import ContextTypes
from storage.users import get_user
from data.nfts import NFT_LIST

CASE_MIN = 15
CASE_MAX = 150

async def opencase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if not args or not args[0].isdigit():
        return await update.message.reply_text("Используй: /opencase 1-10")

    count = int(args[0])
    if not (1 <= count <= 10):
        return await update.message.reply_text("Можно открыть от 1 до 10 кейсов!")

    user = get_user(update.effective_user.id)

    total_currency = 0
    dropped_nfts = []

    for _ in range(count):
        reward = random.randint(CASE_MIN, CASE_MAX)
        total_currency += reward

        nft = random.choice(NFT_LIST)
        user["nfts"].append(nft)
        dropped_nfts.append(nft)

    user["balance"] += total_currency

    nft_text = "\n".join([f"• {n['name']} — {n['value']}💰" for n in dropped_nfts])

    await update.message.reply_text(
        f"🎉 Открыто кейсов: {count}\n"
        f"💰 Валюта: +{total_currency}\n"
        f"🖼 NFT:\n{nft_text}",
        parse_mode="Markdown"
    )
