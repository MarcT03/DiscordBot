# Imports the req modules
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# This makes a Discord client instance and sets the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is logged in and ready to take commands.")

bot.command()
async def greet(cmd):
    response: "Hello, I'm {bot.user.name}, this servers discord bot."
    await cmd.send(response)


load_dotenv()
bot.run(os.getenv('TOKEN'))
