import random






from telegram.ext import Updater, CommandHandler



Token = "1285306305:AAGV3V7WO_w-RERgTfmhVJCmp8hYjr4ZBeE"

mess = ('''🔰Hotstar VIP Account🔰
————————————————
Email :- lokesh_eca@yahoo.co.in

Password :- https://gplinks.co/tSs6FC

Please don't Change Password

Send screenshot to :- @Darkpromoter''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- atiface1992@gmail.com

Password :- https://gplinks.co/tSs6FC

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- anandsinha65@gmail.com

Password :- https://gplinks.co/fZUCR1

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- sujikrishnan.95@gmail.com

Password :- https://gplinks.co/UL3aac4

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- harshbaberwal@gmail.com

Password :- https://gplinks.co/H7UD

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- zakkamwvr@gmail.com

Password :- https://gplinks.co/Iymo

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- shrishailbhat@gmail.com

Password :- https://gplinks.co/YRGw9LHY

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- singh.pratyush6@gmail.com

Password :- https://gplinks.co/EOt9I0wb

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- ayaankatoch@gmail.com

Password :- https://gplinks.co/2xDSmtvz

Please don't Change Password

Send screenshot to :- @Darkpromoter ''' ,'''🔰Hotstar VIP Account🔰
————————————————
Email :- iinfi1@gmail.com

Password :- https://gplinks.co/Jnawa87Y

Please don't Change Password

Send screenshot to :- @Darkpromoter ''')


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name, ))


def hi(update, context):
    update.message.reply_text(format(random.choice(mess)))

        



updater = Updater(Token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.dispatcher.add_handler(CommandHandler('help', hi))


updater.start_polling()
updater.idle()
