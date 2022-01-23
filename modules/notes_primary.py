from unicodedata import category
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord_components import Button, DiscordComponents
from discord_components.component import ButtonStyle
from numpy import true_divide
import os.path
from datetime import datetime
import yaml
from random import randrange

import main


main = main.bot


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

                await channel.send(
                    embed=embed,
                    components = [
                        [
                            Button(label="Pin note", emoji="📌", custom_id = "pin_note", style=ButtonStyle.gray),
                            Button(label="Move to Bin", emoji="🗑️", custom_id = "move_to_bin", style=ButtonStyle.gray)
                        ]
                    ]
                )

                await message.delete()
                print('Note created.')


    @commands.Cog.listener()
    async def on_button_click(self, interaction: commands.Context):
        print("1123test")
        if interaction.component.id == "pin_note":
            await interaction.message.pin()
            print('Pinned a note')


def setup(bot: commands.Bot):
    bot.add_cog(Notes_Primary(bot))