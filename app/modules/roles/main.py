"""
This is the roles module.

It creates a channel with a list of roles one can subscribe to.
"""
# Handle imports
from discord.utils import get

from discord_helpers import basic_embed, get_guild
from permissions import lounge_tc_read_only, lounge_tc_allow
from config import config, app_db


# Define variables

# Define methods
async def setup_roles():
    # Get all servers where this module is enabled
    guilds = app_db.execute(
        'SELECT guild_id '
        ' FROM guild'
        ' WHERE module_react_roles_enabled = 1',
    ).fetchall()

    # Go setup the module
    for guild_id in guilds:
        guild = get_guild(guild_id[0])

        if not guild is None:
            setup_roles_for_server(guild)

async def setup_roles_for_server(guild):
    # Check for a channel
    roles_channel = get(guild.text_channels, name=config["modules"]["roles_channel"])
    if roles_channel is None:
        roles_channel = await guild.create_text_channel(config["modules"]["roles_channel"])

    # Set permissions again to be safe
    await roles_channel.set_permissions(guild.default_role,
                                             overwrite=lounge_tc_read_only)
    await roles_channel.set_permissions(guild.me,
                                             overwrite=lounge_tc_allow)

    # Clear channel
    await roles_channel.purge()

    # Make posts
    react_role_groups = app_db.execute(
        'SELECT name, description, react_role_group_id'
        ' FROM react_role_group'
        ' WHERE guild_id = ?',
        (guild.id,)
    ).fetchall()

    await roles_channel.send("React to the messages below to give yourself roles!")

    for group in react_role_groups:
        react_roles = app_db.execute(
            'SELECT *'
            ' FROM react_role'
            ' WHERE react_role_group_id = ?',
            (group["react_role_group_id"],)
        ).fetchall()

        message = group["description"] + "\n"
        for role in react_roles:
            message += "{}: {}\n".format(role["emoji"], role["role"])

        embed = basic_embed(group["name"], message=message)
        msg = roles_channel.send(embed=embed)

        for role in react_roles:
            await msg.add_reaction(role["emoji"])