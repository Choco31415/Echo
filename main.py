"""
The main entry point to the program.
"""
# Handle imports
import discord
import logging_config
from config import config, client
from discord_helpers import get_embed

# Handle vars

# Run code
logger = logging_config.get_logger("app")

@client.event
async def on_message(message):
    await message.channel.send("", embed=get_embed("title2", [("title", "author")]))

client.run(config["tokens"]["discord_token"])