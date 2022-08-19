import os

from discord.ext import commands
from dotenv import load_dotenv

from fpl import get_player_hist_data, get_player_data

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.command(help="Responds with a player's past performance in the premier league")
async def history(ctx, name, season=1):
    response = get_player_hist_data(name.lower(), int(season))
    await ctx.send(response)

# @bot.command()
# async def teams(ctx, name):
#     pass

@bot.command(help="Responds with a player's current performance in the premier league.")
async def player(ctx, name):
    response = get_player_data(name.lower())
    await ctx.send(response)


bot.run(TOKEN)