import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import Button, DiscordComponents
from discord_components.component import ButtonStyle
from numpy import true_divide
import os.path
import yaml

import main


main = main.bot


class Hardreset(commands.Cog, name="Hardreset"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    @has_permissions(administrator=True)
    async def hard_reset(self, ctx: commands.Context):
        # reading config file
        try:
            with open("config.yaml", "r") as stream:
                config = yaml.safe_load(stream)
        except Exception as e:
            print('Error. Looks like something is wrong with your config file.')
        

        if (config['hard_reset_command'] == False):
            await ctx.send(
                '`!hard_reset` command is disabled by default. If you want to use it enable it in your `config.yaml` file and restart your bot.',
                delete_after = 15
            )
            return 0

        # deletes all the channels on the server
        guild = ctx.guild

        for channel in guild.channels:
            await channel.delete()
            print(f"Channel #{channel.name} ({channel.id}) was deleted")
        
        print('Hard reset completed')


    @hard_reset.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(content = f"You are missing permissions!", delete_after=5)


def setup(bot: commands.Bot):
    bot.add_cog(Hardreset(bot))