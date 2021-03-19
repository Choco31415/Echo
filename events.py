"""
This is the primary Discord file for handling events as they come in.
"""
# Imports
from config import client, logger
from discord_helpers import setup_bot
import sys
import traceback
import functools

# Variables

# Functions
def error_handler(func):
    """
    Encases a function in the default error catcher.
    :return: Wrapped function
    """
    @functools.wraps(func) # Preserves method signatures for discord library
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except:
            logger.error("Uh oh, an error has happened! " + \
                         traceback.format_exc())
            sys.exit(0)

    return wrapper

@client.event
@error_handler
async def on_ready():
    """
    This function is called when the bot is initialized.
    :return: NA
    """
    logger.info("The bot is launching!")
    await setup_bot()
    logger.info("The bot has launched!")

@client.event
@error_handler
async def on_member_join(member):
    """
    This function is called when a member joins a server.
    :param member: Member object.
    :return: NA
    """
    pass

@client.event
@error_handler
async def on_voice_state_update(member, before, after):
    """
    This function is called when a member's voice state has changed.
    For example joining or leaving a voice chat.
    :param member: Member object.
    :param before: Previous state.
    :param after: Current state.
    :return: NA
    """
    pass

@client.event
@error_handler
async def on_guild_join(guild):
    """
    This function is called when the bot joins a new server.
    :param guild: The server/guild object.
    :return: NA
    """
    pass