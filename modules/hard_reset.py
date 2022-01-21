import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import Button, DiscordComponents
from discord_components.component import ButtonStyle


bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())


class Hardreset(commands.Cog, name="Hardreset"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    @has_permissions(administrator=True)
    async def hard_reset(self, ctx: commands.Context):
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