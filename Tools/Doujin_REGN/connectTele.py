from telegram.ext import Application

# Bot Api Key
api_token = "" 

# Create app
def create_application():
    app = Application.builder().token(api_token).build()
    return app
