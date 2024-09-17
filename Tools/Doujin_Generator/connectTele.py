from telegram.ext import Application

# Bot Api Key
api_token = "6977850415:AAFq18IifdiAFJG6VQIWGUkPaFNV9CcltN0"

# Create app
def create_application():
    app = Application.builder().token(api_token).build()
    return app
