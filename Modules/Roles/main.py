"""
This is the roles module.

It creates a channel with a list of roles one can subscribe to.
"""
# Handle imports
from config import config, app_db
from discord_helpers import get_guild
from discord.utils import get
from permissions import lounge_tc_read_only, lounge_tc_allow

# Define variables

# Define methods
async def setup_roles():
    # Get all servers where this module is enabled
    servers = app_db.execute(
        'SELECT s.id, '
        ' FROM server s'
        ' WHERE s.roles_enabled = TRUE',
    ).fetchall()

    # Go setup the module
    for server_id in servers:
        guild = get_guild(server_id)

        if not guild is None:
            setup_roles_for_server(guild)

async def setup_roles_for_server(guild):
    # Check for a channel
    roles_channel = get(guild.text_channels, name=config["modules"]["roles_channel"])
    if roles_channel is None:
        await guild.create_text_channel(config["modules"]["roles_channel"])
    else:
        await roles_channel.purge()

    # Set permissions again to be safe
    await roles_channel.set_permissions(guild.default_role,
                                             overwrite=lounge_tc_read_only)
    await roles_channel.set_permissions(guild.me,
                                             overwrite=lounge_tc_allow)

    # Clear channel

    # Setup channel

