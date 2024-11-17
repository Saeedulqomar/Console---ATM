import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

API_TOKEN = '7977496493:AAEeDTaL7x-pLx6kBhJbgna7iPaIu7k4wts'


async def start(update: Update, context):
    await update.message.reply_text("Hello! I am CodeMentor, your coding assistant bot. How can I help you today?")


async def help_command(update: Update, context):
    await update.message.reply_text("Use /start to begin. Ask me any coding-related questions!")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)


if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()
