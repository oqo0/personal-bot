from discord.ext import commands
from discord.ext.commands import has_permissions
import os.path

import main


main = main.bot


class RestartModules(commands.Cog, name="RestartModules"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    @has_permissions(administrator=True)
    async def restart(self, ctx: commands.Context):
        # restarting all cogs from /modules
        for file in os.listdir('modules'):
            self.bot.unload_extension(f"modules.{file[:-3]}")
            self.bot.load_extension(f"modules.{file[:-3]}")
            print(f"Restarted module {file}")
        
        print('All modules were restarted.')


def setup(bot: commands.Bot):
    bot.add_cog(RestartModules(bot))