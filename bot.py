import discord
from discord.ext import commands
import asyncio
import random
import re
import sys
import json
import os
import traceback

intent = discord.Intents.default()
intent.members = True

bot = commands.Bot(command_prefix='./', case_insensitive=True, intents=intent)

with open('config.json','r') as configjsonfile:
    configdata = json.load(configjsonfile)
    token = configdata['DISCORD_TOKEN']

bot.remove_command('help')


extensions = [
            'comm.general',
            'comm.help',
            'comm.moderation',
            'comm.fun',
            'comm.event'
]

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'error loading {extension}', file = sys.stderr)
            traceback.print_exc()

bot.run(token)