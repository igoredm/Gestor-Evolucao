import discord
from discord.ext import commands
from services.leaderboard import Leaderboard
import os

# Class to start logic for all commands related at Xp (rank and stats)
class Xp(commands.Cog):

  def __init__(self, client):
    self.client = client

  # Command Rank
  @commands.command()
  async def rank(self, ctx):
    Leaderboard.get_rank(ctx)
    await ctx.send(file=discord.File('./assets/img/out/rank.png'))

  # Command Stats with arg (arg = mention other member)
  @commands.command()
  async def stats(self, ctx, arg):
    if len(arg) > 4:
      list_arg = [int(s) for s in arg if s.isdigit()]
      arg = ""
      for numb in list_arg:
        arg += str(numb)
    response = Leaderboard.get_stats(ctx, arg)
    if response[0]:
      await ctx.send(file=discord.File(f'./assets/img/out/stats_{response}.png'))
      os.remove(f'./assets/img/out/stats_{response}.png')
    else:
      await ctx.send(f"❌ Posição inválida! Tente um número entre 1 e {response[1]}!")


  # Command Stats without arg or with wrong arg passed
  @stats.error
  async def stats_on_error(self, ctx, error):
    Leaderboard.get_stats(ctx, None)
    if str(error) != "arg is a required argument that is missing.":
      print(error)
      await ctx.send("Você não marcou um usuário certo, então vai você mesmo 🙃") 
    await ctx.send(file=discord.File(f'./assets/img/out/stats_{str(ctx.message.author.id)}.png'))
    os.remove(f'./assets/img/out/stats_{str(ctx.message.author.id)}.png')

def setup(client):
  client.add_cog(Xp(client))
