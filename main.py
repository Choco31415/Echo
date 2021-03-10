"""
The main entry point to the program.
"""
# Handle imports
import discord
from config import config, client, logger
from discord_helpers import get_embed, setup_bot, set_status
import traceback
import logging_config
import sys

# Handle vars

# Run code
@client.event
async def on_ready():
    try:
        await setup_bot()
        a = 1
        a /= 0
        logger.info("The bot has launched!"+a)
    except:
        logger.error("Uh oh, an error has happened! " + \
                     traceback.format_exc())
        sys.exit(0)

client.run(config["tokens"]["discord_token"])