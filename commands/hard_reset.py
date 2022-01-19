import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import bot


bot = bot.bot


class Hardreset(commands.Cog, name="Hardreset"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # setting up all the channels
    @commands.command()
    @has_permissions(administrator=True)
    async def hard_reset(self, ctx: commands.Context):
        print('Reset completed')
    
    
    @hard_reset.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(content = f"You are missing permissions!", delete_after=5)


def hard_reset(bot: commands.Bot):
    bot.add_cog(Hardreset(bot))