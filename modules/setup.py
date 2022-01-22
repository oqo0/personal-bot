import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import yaml

import main


main = main.bot


class Setup(commands.Cog, name="Setup"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    @has_permissions(administrator=True)
    async def setup(self, ctx: commands.Context):
        # reading config file
        try:
            with open("config.yaml", "r") as stream:
                config = yaml.safe_load(stream)
        except Exception as e:
            print('Error. Looks like something is wrong with your config file.')

        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }

        # channel for actions history
        channels_history = await guild.create_text_channel('history', overwrites=overwrites)
        if (config['notifications_channel'] == True):
            channels_notifications = await guild.create_text_channel('notifications', overwrites=overwrites)

        # user notes category
        if (config['notes_channels'] == True):
            notes_category = await guild.create_category('notes', overwrites=overwrites)
            channels_primary = await guild.create_text_channel('primary', overwrites=overwrites, category=notes_category)
            channels_bin = await guild.create_text_channel('bin', overwrites=overwrites, category=notes_category)

        # tasks managment category
        if (config['task_manager'] == True):
            tasks_category = await guild.create_category('tasks', overwrites=overwrites)
            channels_create = await guild.create_text_channel('create', overwrites=overwrites, category=tasks_category)
            channels_important = await guild.create_text_channel('important', overwrites=overwrites, category=tasks_category)
            channels_my_day = await guild.create_text_channel('my-day', overwrites=overwrites, category=tasks_category)
            channels_all_tasks = await guild.create_text_channel('all-tasks', overwrites=overwrites, category=tasks_category)

        with open('data/channels.yaml') as f:
            channels = yaml.safe_load(f)

        chan = []
        chan.append(channels_history.id)
        chan.append(channels_notifications.id)
        chan.append(channels_primary.id)
        chan.append(channels_bin.id)
        chan.append(channels_create.id)
        chan.append(channels_important.id)
        chan.append(channels_my_day.id)
        chan.append(channels_all_tasks.id)

        channels = chan

        # writing channels data in data/channels.yaml
        with open('data/channels.yaml', 'w') as f:
            yaml.dump(channels, f)

        print('Setup completed')
    
    
    @setup.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(content = f"You are missing permissions!", delete_after=5)


def setup(bot: commands.Bot):
    bot.add_cog(Setup(bot))