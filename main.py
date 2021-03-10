"""
The main entry point to the program.
"""
# Handle imports
import discord
import logging_config
from config import config, client

# Handle vars

# Run code
logger = logging_config.get_logger("app")

@client.event
async def on_message(message):
    print("Hey")

client.run(config["tokens"]["discord_token"])