from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Dictionary to store user data
user_data = {}

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data[user_id] = {
        'coins': 0,
        'level': 1,
        'league': 'Bronze I',
        'trophies': 0
    }
    update.message.reply_text('Welcome to the Chocolate Tapper Game! Tap to earn chocolate coins.')

# Function to handle tapping
def tap(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data[user_id]['coins'] += 1
    update.message.reply_text(f'You tapped! You now have {user_data[user_id]["coins"]} chocolate coins.')

# Command to check status
def status(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user = user_data[user_id]
    update.message.reply_text(f'Coins: {user["coins"]}\nLevel: {user["level"]}\nLeague: {user["league"]}\nTrophies: {user["trophies"]}')

def main() -> None:
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    updater = Updater("7203476648:AAGYZNX8kAcV90yOLREKfgztaIXsCeQpz94")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tap", tap))
    dispatcher.add_handler(CommandHandler("status", status))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
