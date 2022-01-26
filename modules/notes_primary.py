from cProfile import label
from code import interact
from unicodedata import category
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ui import Button, View
from numpy import true_divide
from datetime import datetime
import yaml
from random import randrange

import main


bot = main.bot


class PinButton(Button):
    async def callback(self, interaction):
        await interaction.message.pin()
        print('Message was pinned')


class MoveToBinButton(Button):
    def __init__(self):
        super().__init__(
            label = "Move to #bin",
            style=discord.ButtonStyle.gray,
            emoji="🗑️",
            custom_id="to_bin"
        )

    async def callback(self, interaction):
        with open('data/channels.yaml') as f:
            channels = yaml.safe_load(f)

        channel = bot.get_channel(channels[3])

        button_delete = DeleteButton()

        view2 = View()
        view2.add_item(button_delete)

        await channel.send(embed = interaction.message.embeds[0], view = view2)
        await interaction.message.delete()
        
        print('Message was moved to #bin')


class DeleteButton(Button):
    def __init__(self: commands.Bot):
        super().__init__(
            label = "Delete",
            style=discord.ButtonStyle.red,
            emoji="❕"
        )

    async def callback(self, interaction):
        await interaction.message.delete()
        print('Message was deleted')


class Notes_Primary(commands.Cog, name="Notes_Primary"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message: commands.Context):
        # no need to respond to yourself
        if message.author.bot:
            return 0

        # reading used channels list
        with open("data/channels.yaml", "r") as stream:
            channels = yaml.safe_load(stream)
        
        if (message.channel.id in channels):
            if (message.channel.name == 'primary'):
                channel = self.bot.get_channel(message.channel.id)

                embed = discord.Embed(color=discord.Colour.from_rgb(randrange(0, 255), randrange(0, 255), randrange(0, 255))) # taking a random color for each note
                embed.add_field(name=datetime.now().strftime('%d.%m.%Y %H:%M'), value=message.content)

                if message.attachments != []:
                    embed.set_image(url=message.attachments[0])

                button_pin = PinButton(
                    label = "Pin note",
                    style=discord.ButtonStyle.gray,
                    emoji="📌",
                    custom_id="pin_note"
                )
                button_tobin = MoveToBinButton()

                view = View()
                view.add_item(button_pin)
                view.add_item(button_tobin)

                await channel.send(
                    embed=embed,
                    view=view
                )

                await message.delete()
                print('Note created.')


def setup(bot: commands.Bot):
    bot.add_cog(Notes_Primary(bot))