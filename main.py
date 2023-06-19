import discord
from discord.ext import commands
from discord.ext.bridge import bot
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot =commands.Bot()

@bot.listen()
async def on_connect():
    print('connected to Discord!')

bot.load_extensions("cogs")  # Loads all cogs in the cogs folder

bot.run(os.getenv('tolken'))