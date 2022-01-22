import discord
from discord.ext import commands
import os
import os.path
import sys
import yaml


# disabling bytecode (__pycache__)
sys.dont_write_bytecode = True


bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())


# loading cogs
bot.load_extension(f"modules.setup")
bot.load_extension(f"modules.reset")
bot.load_extension(f"modules.hard_reset")


# reading config
if (os.path.isfile('config.yaml') == True):
    # reading config
    with open("config.yaml", "r") as stream:
        config = yaml.safe_load(stream)


# Bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = config['bot_status']))
    print('Bot started')


# creating a token.yaml file if it doesn't exists
if (os.path.isfile('token.yaml') == True):
    # reading an app token
    with open("token.yaml", "r") as stream:
        token = yaml.safe_load(stream)
    
    try:
        #starting a bot
        bot.run(token['app_token'])
    except:
        print("Error. Something is wrong with your bot's token")
else:
    with open('token.yaml', 'w') as f:
        data = {'app_token': "token"}

        f.write('# your application token goes here\n')
        yaml.dump(data, f)
    
    print("Error. Something is wrong with your bot's token or config.")
