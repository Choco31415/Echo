"""
The main entry point to the program.
"""
# Handle imports
from config import config, client
import logging_config
import discord_helpers
import events

# Handle vars

# Run code
client.run(config["tokens"]["discord_token"])