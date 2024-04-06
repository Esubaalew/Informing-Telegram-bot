from telegram.ext.updater import Updater #upm package(python-telegram-bot)

from telegram import Update, ChatMember #upm package(python-telegram-bot),
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
from telegram.error import BadRequest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

CHANNEL_USERNAME = "@esubalewbots"

def start(update: Update, context: CallbackContext):
  name=update.message.from_user.first_name
  say="Welcome, " +name
  update.message.reply_text(
    say
    )
  update.message.reply_text(
       " I will give you any information about the user. To do that you only forward a text message from the user you need info about.\n\
    or use the following commands: "+
"""
/start - starts the bot
/myinfo - possible informarion about your account
/help - for all commands list
/about - to know about bot designer
/others- list of other bots made bot developer
"""
    )
  update.message.reply_text("Now forward anything from your friends message you need information about or use /myinfo to get your information ")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""USE THE FOLLOWING COMMANDS :-
/start - starts the bot
/myinfo - possible informarion about your account
/help - for all commands list
/about - to know about bot designer

  """)
def about(update: Update, context: CallbackContext):
    update.message.reply_text("""
My name is Esubalew Chekol currently Learning in department of IS Addis Ababa University, Ethiopia.
I am developing telegram bots mainly for learning more.
see @esubalewbots for more bots
""")
def others(update: Update, context: CallbackContext):
    update.message.reply_text("""
    Other bots by @Esubaalew
    @belahdictionarybot
    @MeaningRobot
    @AllFunctionsbot
    @AAU_Robot

""")
def send_join_channel_button(chat_id, context):
  button = InlineKeyboardButton("Join Channel",
                                url="https://t.me/esubalewbots")
  keyboard = [[button]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  context.bot.send_message(chat_id=chat_id,
                           text="To use this bot, please join our channel:",
                           reply_markup=reply_markup)

def check_user_status(update: Update, context: CallbackContext) -> str:
  user_id = update.effective_user.id
  try:
    chat_member = context.bot.get_chat_member(chat_id=CHANNEL_USERNAME,
                                              user_id=user_id)
    user_status = chat_member.status

    return user_status

  except BadRequest as e:
    print(f"Error: {e}")
    return "error"

def unknown(update: Update, context: CallbackContext):

    update.message.reply_text(

        "Sorry '%s' is not a valid command" % update.message.text)

import json

def getInfo(update: Update, context: CallbackContext):
    user_status = check_user_status(update, context)
    if user_status == "error":
        update.message.reply_text("An error occurred. Please try again later.")
        return
    if user_status not in [
      ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.CREATOR
  ]:
      update.message.reply_text(
      f"Your current status: {user_status}\nPlease join {CHANNEL_USERNAME} before using the bot."
    )
      send_join_channel_button(update.message.chat_id, context)
      return
    try:
        userID = str(update.message.forward_from.id)
        userFirst = str(update.message.forward_from.first_name)
        userLast = str(update.message.forward_from.last_name)
        userFull = str(update.message.forward_from.last_name)
        userName = str(update.message.forward_from.username)

        response = {
            "ID": userID,
            "First Name": userFirst,
            "Last Name": userLast,
            "Full Name": userFull,
            "Username": userName
        }

        update.message.reply_text(json.dumps(response, indent=4))
    except Exception as e:
        username = update.message.forward_sender_name
        name = update.message.from_user.first_name
        sorry = 'Dear ' + name + ', This user restricted his account privacy. So some of the informations are not accessible'

        response = {
            "Message": sorry,
            "Name": username
        }

        update.message.reply_text(json.dumps(response, indent=4))

def myinfo(update: Update, context: CallbackContext):
    user_status = check_user_status(update, context)
    if user_status == "error":
        update.message.reply_text("An error occurred. Please try again later.")
        return
    if user_status not in [
      ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.CREATOR
  ]:
      update.message.reply_text(
      f"Your current status: {user_status}\nPlease join {CHANNEL_USERNAME} before using the bot."
    )
      send_join_channel_button(update.message.chat_id, context)
      return
    userID = str(update.message.from_user.id)
    userFirst = str(update.message.from_user.first_name)
    userLast = str(update.message.from_user.last_name)
    userFull = str(update.message.from_user.full_name)
    userName = str(update.message.from_user.username)

    response = {
        "ID": userID,
        "First Name": userFirst,
        "Last Name": userLast,
        "Full Name": userFull,
        "Username": userName
    }

    update.message.reply_text(json.dumps(response, indent=4))

def myinfo(update: Update, context: CallbackContext):
    user_status = check_user_status(update, context)
    if user_status == "error":
        update.message.reply_text("An error occurred. Please try again later.")
        return
    if user_status not in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.CREATOR]:
        update.message.reply_text(
            f"Your current status: {user_status}\nPlease join {CHANNEL_USERNAME} before using the bot."
        )
        send_join_channel_button(update.message.chat_id, context)
        return

    userID = str(update.message.from_user.id)
    userFirst = str(update.message.from_user.first_name)
    userLast = str(update.message.from_user.last_name)
    userFull = str(update.message.from_user.full_name)
    userName = str(update.message.from_user.username)

    response = {
        "ID": userID,
        "First Name": userFirst,
        "Last Name": userLast,
        "Full Name": userFull,
        "Username": userName
    }

    update.message.reply_text(json.dumps(response, indent=4))


def main():
  updater = Updater("TOKEN")

  #updater = Updater(TOKEN, use_context=True)
  disp = updater.dispatcher
  #some=update.message.text
  disp.add_handler(CommandHandler('start', start))
  disp.add_handler(CommandHandler('myinfo', myinfo ))
  disp.add_handler(CommandHandler('help', help ))
  disp.add_handler(CommandHandler('others', others))
  disp.add_handler(CommandHandler('about', about ))
  disp.add_handler(MessageHandler(
    Filters.all & (~Filters.command), getInfo))
  disp.add_handler(MessageHandler(Filters.command, unknown))
  #disp.add_handler(MessageHandler(Filters.some, myinfo))


  updater.start_polling()
#   app.run(host='0.0.0.0', port=8080)
#updater.start_polling()

#updater.idle()
#updater.idle()
#app.run(host='0.0.0.0', port=8080)
if __name__ == '__main__':
    main()
