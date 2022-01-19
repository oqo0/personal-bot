import discord
from discord.ext import commands
import os
import yaml


bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

bot.load_extension("cogs.commands")


# Bot is ready
@bot.event
async def on_ready():
    print('Bot started')


# Importing an app token from token.yaml
with open("token.yaml", "r") as stream:
    token = yaml.safe_load(stream)

bot.run(token['app_token'])