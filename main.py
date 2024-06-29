# Imports the req modules
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# This makes a Discord client instance and sets the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
