"""
This file stores helper functions related to Discord.
"""
# Handle imports
from config import config, bot, logger
import discord

# Define functions
async def setup_bot(update_avatar=False):
    """
    Setup the bot user.
    This includes profile picture and status.
    :return:
    """
    avatar_file = config["general"]["avatar file"]
    name = config["general"]["name"]
    activity = config["general"]["activity"]

    if update_avatar:
        with open(avatar_file, 'rb') as f:
            await bot.user.edit(avatar=f.read())

    await set_status(discord.Game(activity))

async def set_status(activity=None):
    await bot.change_presence(activity=activity)

def get_embed(title, sections):
    """
    Create and format a standard Discord embed.
    :param title:
    :param sections:
    :return:
    """
    c = int(config["general"]["message color"], 16)
    embed = discord.Embed(title=title, color=c)
    for s in sections:
        embed.add_field(
        name=s[0],
        value=s[1],
        inline=False)

    return embed

async def get_dm_channel(user):
    """
    Get the dm channel of a user.
    :param user:
    :return:
    """
    dm_channel = user.dm_channel
    if dm_channel is None:
        dm_channel = await user.create_dm()
    return dm_channel