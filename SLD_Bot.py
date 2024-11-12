import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, CallbackContext, filters

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your bot token
api_key = 'AAHpfQCdpepcFayBIWfx3xwQXmJ6Bm2lUWg'

# Start command with both inline and reply keyboards
async def start(update: Update, context: CallbackContext) -> None:
    # Inline Keyboard
    inline_keyboard = [
        [InlineKeyboardButton("Inline Button 1", callback_data='1'),
         InlineKeyboardButton("Inline Button 2", callback_data='2')],
    ]
    inline_reply_markup = InlineKeyboardMarkup(inline_keyboard)

    # Reply Keyboard
    reply_keyboard = [['Option 1', 'Option 2']]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    # Send both keyboards
    await update.message.reply_text(
        "Choose an option from both inline or reply keyboards:",
        reply_markup=inline_reply_markup
    )
    await update.message.reply_text(
        "You can also select from the inline options:",
        reply_markup=inline_reply_markup
    )

# Handle button clicks (from inline buttons)
async def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    # Respond based on button clicked
    if query.data == '1':
        await query.edit_message_text(text="You clicked Inline Button 1!")
    elif query.data == '2':
        await query.edit_message_text(text="You clicked Inline Button 2!")

# Handle reply button clicks (from custom reply keyboard)
async def reply_button(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == 'Option 1':
        await update.message.reply_text("You chose Option 1 from the reply keyboard!")
    elif text == 'Option 2':
        await update.message.reply_text("You chose Option 2 from the reply keyboard!")

# Create the Application and add handlers
def main():
    application = Application.builder().token(api_key).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_button))

    # Run the bot until you stop it
    application.run_polling()

if __name__ == '__main__':
    main()
