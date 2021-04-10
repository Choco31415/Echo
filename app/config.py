"""
Imports and holds the conf file. Nothing else.
"""
# Handle imports
import configparser
import logging

from discord.ext import commands

from db import *

# Define values
conf_file = 'data/conf.ini'
db_file = 'data/app.db'
schema_file = 'data/schema.sql'

testing = True

# Run code
config = configparser.ConfigParser()
config.read(conf_file)

app_db = get_db(db_file)

logger = logging.getLogger("echo")

bot = commands.Bot(command_prefix='.')