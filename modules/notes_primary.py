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


main = main.bot


class PinButton(Button):
    async def callback(self, interaction):
        await interaction.message.pin()
        print('Message was pinned')


class MoveToBinButton(Button):
    async def callback(self, interaction):
        with open('data/channels.yaml') as f:
            channels = yaml.safe_load(f)

        channel = self.bot.get_channel(channels[2])
        await channel.send(interaction.message.content)
        await interaction.message.delete()
        
        print('Message was moved to #bin')


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
                embed.add_field(name=f"Note", value=message.content)
                embed.set_footer(text=f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}")

                button_pin = PinButton(
                    label = "Pin note",
                    style=discord.ButtonStyle.gray,
                    emoji="📌",
                    custom_id="pin_note"
                )
                button_tobin = MoveToBinButton(
                    label = "Move to #bin",
                    style=discord.ButtonStyle.red,
                    emoji="🗑️",
                    custom_id="to_bin"
                )

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