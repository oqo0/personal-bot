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


class Reset(commands.Cog, name="Reset"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    @has_permissions(administrator=True)
    async def reset(self, ctx: commands.Context):
        # reading config file
        try:
            with open("config.yaml", "r") as stream:
                config = yaml.safe_load(stream)
        except Exception as e:
            print('Error. Looks like something is wrong with your config file.')
            return 0

        if (config['reset_command'] == False):
            await ctx.send(
                '`!reset` command is disabled by default. If you want to use it enable it in your `config.yaml` file and restart your bot.',
                delete_after = 15
            )
            return 0


        with open('data/channels.yaml') as f:
            channels = yaml.safe_load(f)
        
        # deletes all the channels that were used by this bot
        guild = ctx.guild

        for c in channels:
            channel = guild.get_channel(c)
            await channel.delete()
        
        # guild = ctx.guild
        # for all_c in guild.channels:
        #     for listed_c in channels:
        #         if (all_c == listed_c):
        #             await all_c.delete()
        #             print(f"Channel #{all_c.name} ({all_c.id}) was deleted")

        print('Reset completed')


    @reset.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(content = f"You are missing permissions!", delete_after=5)


def setup(bot: commands.Bot):
    bot.add_cog(Reset(bot))