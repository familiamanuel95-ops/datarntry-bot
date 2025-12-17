from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎶 Bienvenido a Datarntry Bot\n"
        "Usa comandos como:\n"
        "/sad /happy /love /motivation /party /chill"
    )

async def sad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💔 A veces irse también es quererse.")

async def happy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Sonríe, lo mejor aún viene.")

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❤️ El amor también es paz.")

async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 No te rindas, sigue.")

async def party(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Hoy se vive.")

async def chill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌿 Respira y fluye.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sad", sad))
app.add_handler(CommandHandler("happy", happy))
app.add_handler(CommandHandler("love", love))
app.add_handler(CommandHandler("motivation", motivation))
app.add_handler(CommandHandler("party", party))
app.add_handler(CommandHandler("chill", chill))

app.run_polling()
