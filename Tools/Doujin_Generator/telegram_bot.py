from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
from connectTele import create_application  # Import the function to create the Application
from emoji import get_emoji
import genre as tag 

app = create_application()  # Create the Application instance

# Start 
async def start(update: Update, context: CallbackContext): 
    await update.message.reply_text(
        f"Bot Is Online {get_emoji('cat_kissing')}, Use /menu")

# Menu
async def menu(update: Update, context: CallbackContext): 
    await update.message.reply_text("""Menu :
    /Site : Suggestion Sites
    /Nhentai : Top Site
    /Genre : Category of Doujinshi
    /1Gen : Generate 1 Random Sauce 
    /5Gen : Generate 5 Random Sauce 
    /End : Close Bot""")

# Site Suggestions
async def site(update: Update, context: CallbackContext): 
    await update.message.reply_text(""" Best Doujin Site : 
    1. /Nhentai
    2. /Hitomi               
                                    """)

# Originated source
async def nhentai(update: Update, context: CallbackContext): 
    await update.message.reply_text("https://nhentai.net/")

# Another site
async def hitomi(update: Update, context: CallbackContext): 
    await update.message.reply_text("https://hitomi.la/")

# Genre
async def genre(update: Update, context: CallbackContext): 
    await update.message.reply_text("""Gener : 
    /incest     /netorare       /lolicon        /xray
    /milf       /shotacon       /mindcontrol    /impregnation                                
                                    """)

# Remove the genre /
async def handle_genre(update: Update, context: CallbackContext):
    command = update.message.text[1:]  
    url = tag.genre_tag.get(command.lower())  
    if url:
        await update.message.reply_text(url)
    else:
        await update.message.reply_text(f"Genre '{command}' not found!")

# Warning
async def unknown(update: Update, context: CallbackContext): 
    await update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

# Shutdown
async def shutdown(update: Update, context: CallbackContext):
    global running
    running = False
    await update.message.reply_text(f"Shutdown {get_emoji("smiling")}")
    await app.stop()

# Add handlers
app.add_handler(CommandHandler('start', start)) 
app.add_handler(CommandHandler('menu', menu)) 
app.add_handler(CommandHandler('Site', site)) 
app.add_handler(CommandHandler('Nhentai', nhentai))  
app.add_handler(CommandHandler('Hitomi', hitomi))  
app.add_handler(CommandHandler('Genre', genre)) 
app.add_handler(CommandHandler('End', shutdown)) 

# Add all handler to Genre
for genre in tag.genre_tag:
    app.add_handler(CommandHandler(genre, handle_genre))

# Command filters
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
app.add_handler(MessageHandler(filters.COMMAND, unknown))  

# Start the Bot
app.run_polling()
