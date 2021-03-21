"""
This file stores helper functions related to Discord.
"""
# Handle imports
from config import config, bot, app_db
import discord
from discord.utils import get

# Define functions
async def setup_bot(update_avatar=False):
    """
    Setup the bot user.
    This includes profile picture and status.
    :return:
    """
    # Setup the account
    avatar_file = config["general"]["avatar file"]
    name = config["general"]["name"]
    activity = config["general"]["activity"]

    if update_avatar:
        with open(avatar_file, 'rb') as f:
            await bot.user.edit(avatar=f.read())

    await set_status(discord.Game(activity))

    # Next we synchronize the database

    # Check that guilds are recorded
    for guild in bot.guilds:
        if app_db.execute('SELECT * FROM guild WHERE guild_id = ?', (guild.id,)).fetchone() is None:
            print(guild.id)
            app_db.execute(
                'INSERT INTO guild (guild_id)'
                ' VALUES (?)',
                (guild.id,)
            )
            app_db.commit()

    # And only those guilds
    for guild in app_db.execute('SELECT * FROM guild', ).fetchall():
        _ = get_guild(guild["guild_id"])

async def set_status(activity=None):
    await bot.change_presence(activity=activity)

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

def get_guild(guild_id):
    """
    Get a guild based on id.

    Returns None on failure.
    :param server_id: int
    :return: A guild object or None
    """
    guild = get(bot.guilds, id=guild_id)

    # Check for desync condition
    if guild is None:
        # Remove the server from the db
        app_db.execute('DELETE FROM guild WHERE guild_id = ?', (guild_id,))
        app_db.commit()