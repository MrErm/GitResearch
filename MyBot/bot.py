from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Вызван старт", update)
    await update.message.reply_text("Reality is overrated!")



def main():
    mybot = ApplicationBuilder().token("...............................").build()

   
    mybot.add_handler(CommandHandler("start", hello_user))

    mybot.run_polling()
   

main()



