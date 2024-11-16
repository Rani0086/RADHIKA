import os
import sys
import asyncio
import importlib
from flask import Flask
import threading
from pyrogram import idle
from pyrogram.types import BotCommand
from RADHIKA import LOGGER, nexichat
from RADHIKA.plugins import ALL_MODULES
from RADHIKA.plugins.Clone import restart_bots

OWNER_ID = "7526369190"

async def anony_boot():
    try:
        await RADHIKA.start()
        
        # Start restart_bots in a separate background task
        asyncio.create_task(restart_bots())
        
    except Exception as ex:
        LOGGER.error(ex)

    for all_module in ALL_MODULES:
        importlib.import_module("RADHIKA.plugins." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    # Set bot commands
    try:
        await RADHIKA.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("clone", "Make your own chatbot"),
                BotCommand("ping", "Check if the bot is alive or dead"),
                BotCommand("lang", "Select bot reply language"),
                BotCommand("resetlang", "Reset to default bot reply lang"),
                BotCommand("id", "Get users user_id"),
                BotCommand("stats", "Check bot stats"),
                BotCommand("gcast", "Broadcast any message to groups/users"),
                BotCommand("chatbot", "Enable or disable chatbot"),
                BotCommand("status", "Check chatbot enable or disable in chat"),
                BotCommand("shayri", "Get random shayri for love"),
            
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{RADHIKA.username} Started.")
    try:
        await RADHIKA.send_message(int(OWNER_ID), f"{RADHIKA.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{RADHIKA.username} Started, please start the bot from owner id.")
    
    await idle()

# Flask Server Code for Health Check
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Start Flask server in a new thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start the bot asynchronously
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping RADHIKA Bot...")
