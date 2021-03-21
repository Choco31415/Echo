"""
Handles generic commmands for the bot.
"""
# Imports
from config import bot, config
from discord.ext import commands
from discord.utils import get
import discord
from datetime import date

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
        c = int(config["general"]["message color"], 16)
        embed = discord.Embed(color = c,
                          title = 'Announcement',
                          description = message)\
            .set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)\
            .set_footer(text=ctx.guild.me.name + " • " + str(date.today()), icon_url=ctx.guild.me.avatar_url)

        await channel.send(embed=embed)

        await ctx.send("Message sent!")