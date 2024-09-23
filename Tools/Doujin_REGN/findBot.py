import random
import json
from telegram import Update
from telegram.ext import CallbackContext

# Initialize CodeLib array
CodeLib = set()
running = True  # Global flag for bot state

def load_code_lib():
    """Load CodeLib from a JSON file."""
    global CodeLib
    try:
        with open('CodeLib.json', 'r') as file:
            CodeLib = set(json.load(file))
    except FileNotFoundError:
        CodeLib = set()  # File does not exist, start with an empty set
    except json.JSONDecodeError:
        CodeLib = set()  # File is empty or corrupt, start with an empty set

def save_code_lib():
    """Save CodeLib to a JSON file."""
    with open('CodeLib.json', 'w') as file:
        json.dump(list(CodeLib), file)

def generate_random_code() -> str:
    """Generate a random 6-digit code."""
    return f"{random.randint(0, 999999):06d}"

def create_code_url(code: str) -> str:
    """Create the URL with the provided code."""
    return f"https://nhentai.net/g/{code}"

async def GenRandCode(update: Update, context: CallbackContext) -> None:
    """Generate a random code, check if it's in CodeLib, and respond to the user."""
    global CodeLib, running

    if not running:
        await update.message.reply_text("Bot is offline. Please restart using /start.")
        return

    # Load CodeLib from file
    load_code_lib()

    # Generate a new random 6-digit code
    new_code = generate_random_code()

    if new_code in CodeLib:
        # If the code is already in CodeLib, notify the user
        await update.message.reply_text("This code is already in the library.")
    else:
        # Add the new code to CodeLib and send the URL to the user
        CodeLib.add(new_code)
        save_code_lib()  # Save CodeLib to file
        code_url = create_code_url(new_code)
        await update.message.reply_text(f"Here's your code: {new_code}\n{code_url}")
