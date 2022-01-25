from unicodedata import category
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
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
        # reading config file
        try:
            with open("config.yaml", "r") as stream:
                config = yaml.safe_load(stream)
        except Exception as e:
            print('Error. Looks like something is wrong with your config file.')
            return 0

        if (config['remove_invite'] == False):
            print('remove_invite config option is disabled')
            return 0
        
        await invite.delete()
        print("A new invite was deleted")


    # kicking everyone who joins the server
    @commands.Cog.listener()
    async def on_member_join(member: commands.Context):
        # reading config file
        try:
            with open("config.yaml", "r") as stream:
                config = yaml.safe_load(stream)
        except Exception as e:
            print('Error. Looks like something is wrong with your config file.')
            return 0

        if (config['kick_everyone'] == False):
            print('kick_everyone config option is disabled')
            return 0

        await member.kick()
        print(f"User {member.name} was kicked from the server")


def setup(bot: commands.Bot):
    bot.add_cog(Protector(bot))