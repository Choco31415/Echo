"""
Imports and holds the conf file. Nothing else.
"""
# Handle imports
import configparser
import sqlite3
import logging
from discord.ext import commands
from db import *

# Define values
conf_file = "Data/conf.ini"
db_file = 'Data/app.db'
schema_file = 'Data/schema.sql'

testing = True

# Run code
config = configparser.ConfigParser()
config.read(conf_file)

app_db = get_db(db_file)

logger = logging.getLogger("app")

bot = commands.Bot(command_prefix='.')