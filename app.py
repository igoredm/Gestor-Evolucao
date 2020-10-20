import discord
import os
from settings import BOT_TOKEN, PREFIX
from discord.ext import commands

client = commands.Bot(command_prefix=PREFIX)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.' + filename[:-3])

client.run(BOT_TOKEN)
