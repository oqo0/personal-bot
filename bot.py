import discord
from discord.ext import commands
import os
import os.path
import yaml


bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())


bot.load_extension("commands.setup")
bot.load_extension("commands.hard_reset")


# Bot is ready
@bot.event
async def on_ready():
    print('Bot started')


# creating a token.yaml file if it doesn't exists
if (os.path.isfile('token.yaml') == True):
    # reading an app token from token.yaml
    with open("token.yaml", "r") as stream:
        token = yaml.safe_load(stream)
    
    try:
        bot.run(token['app_token'])
    except:
        print("Error. Something is wrong with your bot's token")
else:
    with open('token.yaml', 'w') as f:
        data = {'app_token': "token"}

        f.write('# your application token goes here\n')
        yaml.dump(data, f)
    
    print("Paste your bot's token in token.yaml")