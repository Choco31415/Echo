"""
The main entry point to the program.
"""
# Handle imports
from config import config, bot
import logging_config
import discord_helpers
import events
import generic_commands

# Handle vars

# Run code
bot.run(config["tokens"]["discord_token"])