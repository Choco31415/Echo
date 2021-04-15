"""
Commands for the roles module.
"""
# Import
from discord.ext import commands
from config import app_db, bot

# Define vars

# Define methods
def module_is_enabled():
    async def predicate(ctx):
        guild = app_db.execute(
            'SELECT guild_id'
            ' FROM guild'
            ' WHERE module_react_roles_enabled = 1 AND guild_id = ?',
            (ctx.guild.id,)
        ).fetchall()
        return not guild is None

    return commands.check(predicate)

@bot.command(name="rr refresh")
@module_is_enabled()
def refresh():
    pass

@bot.command(name="rr add")
@module_is_enabled()
def add_react_role_group(title, description, *, role_emoji_pair):
    pass

@bot.command(name="rr update")
@module_is_enabled()
def update_react_role_group(msg_id, title, description, *, role_emoji_pair):
    pass

@bot.command(name="rr remove")
@module_is_enabled()
def remove_react_role_group(msg_id):
    pass

@bot.command(name="rr list")
@module_is_enabled()
def list_react_role_groups():
    pass