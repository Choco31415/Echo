"""
Handles generic commmands for the bot.
"""
# Imports
from config import bot

# Variables

# Functions
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")