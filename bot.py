from telegram.ext.updater import Updater #upm package(python-telegram-bot)

from telegram import Update #upm package(python-telegram-bot)
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from replit import db
from telegram.ext.filters import Filters
import os

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
def unknown(update: Update, context: CallbackContext): 

    update.message.reply_text( 

        "Sorry '%s' is not a valid command" % update.message.text) 

def getInfo(update: Update, context: CallbackContext):
    try:
        userID=str(update.message.forward_from.id)
        userFirst=str(update.message.forward_from.first_name)
        userLast=str(update.message.forward_from.last_name)
        userFull=str(update.message.forward_from.last_name)
        userName=str(update.message.forward_from.username)
        
  
        idd="The user's telegram ID is "+ userID
        Fname="The user's telegram First Name is "+ userFirst 
        Lname="The user's telegram Last Name is "+ userLast
        FuName="The user's telegram Full Name is "+ userFull
        userN="The user's telegram username is "+ userName
        see=False
        if userLast=='None':
            see=True
            if see is True:
                FuName="The user's Full Name is "+userFirst
                Lname="The user did not set last name to Telegram"
        if userFirst=='None':
            see=True
            if see is True:
                Fname="The user did not set first name to Telegram"
    

        if userName=='None':
            see=True
            if see is True:
                userN="The user did not set username to Telegram"


        update.message.reply_text(
        'ID: ' +idd+'\n'+ 'First Name: '+ Fname+ '\n'+ 'Last Name: '+
        Lname +'\n' + 'Full Name: '+ FuName + '\n'+ 'Username: ' +userN
          )
    except:
        username=update.message.forward_sender_name
        name=update.message.from_user.first_name
        sorry='Dear '+ name+ ', This user restricted his account privacy. So some of the informations are not accesible'

        update.message.reply_text(
            sorry+ " \n"+ 'The only inormation: \n Name of User: '+ username

        )
def myinfo(update: Update, context: CallbackContext):
    userID=update.message.from_user.id
    userFirst=update.message.from_user.first_name
    userLast=update.message.from_user.last_name
    userFull=update.message.from_user.full_name
    userName=update.message.from_user.username
    userID=str(userID)
    userFirst=str(userFirst)
    userLast=str(userLast)
    userFull=str(userFull)
    userName=str(userName)
    idd='Your telegram id is '+ userID
    Fname='Your First name is '+ userFirst 
    Lname='Your Last name is '+ userLast
    FuName='Your Full  name is '+ userFull
    userN='Your Telegram username is '+ userName
    
    see=False
    if userLast=='None':
        see=True
        if see is True:
            FuName="Your  Full Name is "+userFirst
            Lname="You did not set your last name to Telegram"
            
    if userFirst=='None':
        see=True
        if see is True:
            Fname="You did not set your first name to Telegram"
    

    if userName=='None':
        see=True
        if see is True:
            userN="You did not set your username to Telegram"
    



    update.message.reply_text(
       'ID: ' +idd+'\n'+ 'First Name: '+ Fname+ '\n'+ 'Last Name: '+
        Lname +'\n' + 'Full Name: '+ FuName + '\n'+ 'Username: ' +userN

    )

def main():
  updater = Updater(os.getenv("TOKEN"))
    
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
  app.run(host='0.0.0.0', port=8080)
#updater.start_polling()
                          
#updater.idle()
#updater.idle()
#app.run(host='0.0.0.0', port=8080)
if __name__ == '__main__':
    main()
