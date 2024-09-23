import requests
from bs4 import BeautifulSoup
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from connectTele import create_application  
from emoji import get_emoji
import genre as tag 
from findBot import GenRandCode  

# Create App and State 
app = create_application() 
running = True   # Controls bot state

# Define conversation states
WAITING_FOR_CODE = range(1)

# Start Command Handler
async def start(update: Update, context: CallbackContext): 
    global running
    if not running:
        await update.message.reply_text(f"Restarting the bot {get_emoji('cat_kissing')}")
        running = True  # Set running to True to allow commands to work again
    else:
        await update.message.reply_text(f"Bot Is Online {get_emoji('cat_smile')}, Use /menu")

# Menu Command Handler
async def menu(update: Update, context: CallbackContext): 
    if running:
        await update.message.reply_text(f"""
Menu {get_emoji('smiley')}:

    /Site {get_emoji('smirk')}: Suggestion Sites
    
    /Genre {get_emoji('cat_heart')}: Category of Doujinshi
    
    /InputCode {get_emoji('relaxed')}: Enter Code
    
    /Random {get_emoji('open_mouth')}: Random code
    
    /NhRandom {get_emoji('astonished')}: Random Nhentai Content
    
    /Top5 {get_emoji('beaming')}: Top 5 
    
    /End {get_emoji('pleading')}: Close Bot
    """)
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Site Suggestions Handler
async def site(update: Update, context: CallbackContext): 
    if running:
        await update.message.reply_text(f""" 
Best Doujin Site {get_emoji('heart_eyes')}: 

    1. /Nhentai {get_emoji('smiley')}
    
    2. /Hitomi {get_emoji('smirk')}
    
    """)
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Nhentai Link Handler
async def nhentai(update: Update, context: CallbackContext): 
    if running:
        await update.message.reply_text(f"https://nhentai.net/ {get_emoji('cat_heart')}")
        # Call the menu function after replying
        await menu(update, context)
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Hitomi Link Handler
async def hitomi(update: Update, context: CallbackContext): 
    if running:
        await update.message.reply_text(f"https://hitomi.la/ {get_emoji('smirk')}")
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Genre Command Handler
async def genre(update: Update, context: CallbackContext): 
    if running:
        # Create inline keyboard with genres in 3 columns
        keyboard = []
        row = []
        for i, genre in enumerate(tag.genre_tag.keys()):
            row.append(InlineKeyboardButton(genre, callback_data=genre))
            if (i + 1) % 3 == 0:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)  # Add remaining buttons in the last row

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(f"Select a genre {get_emoji('smiley')}: ", reply_markup=reply_markup)
        # Call the menu function after replying
        await menu(update, context)
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Handle individual genre callback queries
async def handle_genre_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    genre = query.data
    url = tag.genre_tag.get(genre.lower())

    if url:
        await query.answer()  # Acknowledge the callback
        await query.edit_message_text(f"{genre}: {url} {get_emoji('cat_smile')}")
    else:
        await query.answer()  # Acknowledge the callback
        await query.edit_message_text(f"'{genre}' not found! {get_emoji('dizzy')}")

# Input Code Handler
async def start_code_input(update: Update, context: CallbackContext) -> int:
    if running:
        await update.message.reply_text(f"Enter Code {get_emoji('wink')}:")
        return WAITING_FOR_CODE
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")
        return ConversationHandler.END

async def receive_code(update: Update, context: CallbackContext) -> int:
    user_message = update.message.text
    
    if user_message.isdigit() and len(user_message) == 6:
        nhentai_url = f"https://nhentai.net/g/{user_message}/"
        await update.message.reply_text(f"{nhentai_url} {get_emoji('cat_heart')}")
    else:
        await update.message.reply_text(f"Invalid code {get_emoji('dizzy')}. Please enter a 6-digit code!!")
    
    return ConversationHandler.END

# Top 5 Command Handler
async def top5(update: Update, context: CallbackContext):
    if running:
        try:
            response = requests.get("https://nhentai.net/")
            soup = BeautifulSoup(response.text, 'html.parser')
            popular_items = soup.select('div.index-popular .gallery')[:5]

            for item in popular_items:
                link = item.find('a', class_='cover')['href']
                img_url = item.find('img', class_='lazyload')['data-src']
                caption = item.find('div', class_='caption').text
                full_url = f"https://nhentai.net{link}"
                
                await update.message.reply_photo(
                    photo=img_url,
                    caption=f"{caption}\n{full_url} {get_emoji('heart_eyes')}"
                )
            # Call the menu function after replying
            await menu(update, context)
        except Exception as e:
            await update.message.reply_text(f"An error occurred {get_emoji('dizzy')}: {e}")
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# NhRandom Command Handler
async def nhrandom(update: Update, context: CallbackContext):
    if running:
        try:
            response = requests.get("https://nhentai.net/random/")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the random item
            random_item = soup.find('div', class_='gallery')
            if random_item:
                link = random_item.find('a', class_='cover')['href']
                img_url = random_item.find('img', class_='lazyload')['data-src']
                code = link.split('/')[2]
                full_url = f"https://nhentai.net/g/{code}/"
                
                await update.message.reply_photo(
                    photo=img_url,
                    caption=f"{full_url} {get_emoji('astonished')}"
                )
            else:
                await update.message.reply_text(f"Could not fetch random content {get_emoji('dizzy')}.")
            # Call the menu function after replying
            await menu(update, context)
        except Exception as e:
            await update.message.reply_text(f"An error occurred {get_emoji('dizzy')}: {e}")
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Unknown Command Handler
async def unknown(update: Update, context: CallbackContext): 
    if running:
        await update.message.reply_text(
            f"Sorry '{update.message.text}' is not a valid command {get_emoji('dizzy')}")
    else:
        await update.message.reply_text(f"Bot is offline {get_emoji('no_mouth')}. Please restart using /start.")

# Shutdown Command Handler
async def shutdown(update: Update, context: CallbackContext):
    global running
    running = False
    await update.message.reply_text(f"Shutting down {get_emoji('smiling')}. Use /start to restart.")

# Add handlers using ConversationHandler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('InputCode', start_code_input)],
    states={
        WAITING_FOR_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_code)],
    },
    fallbacks=[],
)

# Add handlers
app.add_handler(CommandHandler('start', start)) 
app.add_handler(CommandHandler('menu', menu)) 
app.add_handler(CommandHandler('Site', site)) 
app.add_handler(CommandHandler('Nhentai', nhentai))  
app.add_handler(CommandHandler('Hitomi', hitomi))  
app.add_handler(CommandHandler('Genre', genre)) 
app.add_handler(CommandHandler('Random', GenRandCode))  
app.add_handler(CommandHandler('Top5', top5))
app.add_handler(CommandHandler('NhRandom', nhrandom))
app.add_handler(CommandHandler('End', shutdown))
app.add_handler(conv_handler)  # Add conversation handler

# Handle genre callback query
app.add_handler(CallbackQueryHandler(handle_genre_callback))

# Handle unknown commands
app.add_handler(MessageHandler(filters.COMMAND, unknown))

# Start the bot
if __name__ == '__main__':
    app.run_polling()
    
if __name__ == '__main__':
    create_application()  # Assuming `create_application()` is the function to start the bot

