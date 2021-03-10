"""
This file stores helper functions related to Discord.
"""
# Handle imports
from config import config, client
import discord

# Define functions
async def setup_bot(guild):
    """
    Setup the bot user.
    This includes profile picture and status.
    :return:
    """
    avatar_file = config["general"]["avatar_file"]
    name = config["general"]["name"]
    activity = config["general"]["activity"]

    with open(avatar_file, 'rb') as f:
        await client.user.edit(avatar=f.read())

    await set_status(discord.Game(activity))

async def set_status(activity=None):
    await client.change_presence(activity=activity)

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