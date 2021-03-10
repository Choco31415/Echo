"""
Imports and holds the conf file. Nothing else.
"""
# Handle imports
import configparser
import sqlite3
import discord

# Define values
conf_file = "Data/conf.ini"
app_db_file = 'Data/app.db'

testing = True

# Run code
config = configparser.ConfigParser()
config.read(conf_file)

app_db = sqlite3.connect(app_db_file)

client = discord.Client()