"""
The main entry point to the program.
"""
# Handle imports
from config import bot
from logging_config import *
import events
import generic_commands

# Handle vars

# Run code
bot.run(config["tokens"]["discord_token"])