import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import bot


bot = bot.bot


class Setup(commands.Cog, name="Setup"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # setting up all the channels
    @commands.command()
    @has_permissions(administrator=True)
    async def setup(self, ctx: commands.Context):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }

        # channel for actions history
        await guild.create_text_channel('history', overwrites=overwrites)
        await guild.create_text_channel('notifications', overwrites=overwrites)

        # user notes category
        notes_category = await guild.create_category('notes', overwrites=overwrites)
        await guild.create_text_channel('primary', overwrites=overwrites, category=notes_category)
        await guild.create_text_channel('bin', overwrites=overwrites, category=notes_category)

        # tasks managment category
        tasks_category = await guild.create_category('tasks', overwrites=overwrites)
        await guild.create_text_channel('create', overwrites=overwrites, category=tasks_category)
        await guild.create_text_channel('important', overwrites=overwrites, category=tasks_category)
        await guild.create_text_channel('my-day', overwrites=overwrites, category=tasks_category)
        await guild.create_text_channel('all-tasks', overwrites=overwrites, category=tasks_category)

        print('Setup completed')
    
    
    @setup.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(content = f"You are missing permissions!", delete_after=5)


def setup(bot: commands.Bot):
    bot.add_cog(Setup(bot))