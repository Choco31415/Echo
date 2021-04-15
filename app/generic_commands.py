"""
Handles generic commmands for the bot.
"""
# Imports
from datetime import date

from discord.ext import commands
from discord.utils import get

from discord_helpers import basic_embed
from config import bot, app_db

from modules.roles.main import setup_roles_for_server

# Variables

# Functions
@bot.command()
async def ping(ctx):
    """
    Basic ping command.
    :param ctx: Context
    :return: NA
    """
    await ctx.send("Pong!")

@bot.command()
@commands.is_owner()
async def announcement(ctx, channel, *, message):
    """
    Make a official looking announcement with the bot.
    :param ctx: Context
    :param channel: Where to make the announcement.
    :param message: What to post.
    :return: NA
    """
    guild = ctx.guild

    channel = get(guild.text_channels, name=channel)
    if channel is None:
        # The channel doesn't exist
        await ctx.send("That channel doesn't exist!")
    else:
        # The channel exists
        embed = basic_embed('Announcement', message)\
            .set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)\
            .set_footer(text=ctx.guild.me.name + " • " + str(date.today()), icon_url=ctx.guild.me.avatar_url)

        await channel.send(embed=embed)

        await ctx.send("Message sent!")

@bot.command()
@commands.is_owner()
async def toggle_module(ctx, module):
    modules = ["react_roles", "lounges", "twitch"]

    if not module in modules:
        ctx.send("{} is not a valid module.".format(module))
    else:
        # Get status
        enabled = app_db.execute(
            'SELECT module_' + module + '_enabled '
            ' FROM guild'
            ' WHERE guild_id = ?',
            (ctx.guild.id,)
        ).fetchone()[0]

        # Update status
        app_db.execute(
            'UPDATE guild'
            ' SET module_' + module + '_enabled = ' + str(0 if enabled else 1) +
            ' WHERE guild_id = ?',
            (ctx.guild.id,)
        )
        app_db.commit()

        # Run code
        if module == "react_roles":
            await setup_roles_for_server(ctx.guild)

        # Report
        await ctx.send("Module {} is now {}.".format(module, "disabled" if enabled else "enabled"))