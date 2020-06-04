from telegram.ext import Updater
updater = Updater(token='1296488130:AAH_Qi3WpsvlHy8Q9A-CEqib1TLjSxIw0kI', use_context=True)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
