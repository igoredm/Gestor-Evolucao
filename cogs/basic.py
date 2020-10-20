import discord
from discord.ext import commands

# Class to basic verify and commands for bot
class Basic(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Command to log on console when bot started
  @commands.Cog.listener()
  async def on_ready(self):
    activity = discord.Game(name="Contando XPs")
    await self.client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot ta ON!")

  # Ping command to show bot latency on server
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
  client.add_cog(Basic(client))