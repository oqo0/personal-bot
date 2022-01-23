from unicodedata import category
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import Button, DiscordComponents
from discord_components.component import ButtonStyle
from numpy import true_divide
import os.path
from datetime import datetime
import yaml
from random import randrange

import main


main = main.bot


class Protector(commands.Cog, name="Protector"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        await invite.delete()
        print("A new invite was deleted")


    # kicking everyone who joins the server
    @commands.Cog.listener()
    async def on_member_join(ctx, member: commands.Context):
        await member.kick()
        print(f"User {member.name} was kicked from the server")


def setup(bot: commands.Bot):
    bot.add_cog(Protector(bot))