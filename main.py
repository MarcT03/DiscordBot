# Imports the req modules
from typing import Final
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# This makes a Discord client instance and sets the command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is logged in and ready to take commands.")


@bot.command()
async def greet(ctx):
    response = f"Hello, I'm {bot.user.name}, this servers discord bot."
    await ctx.send(response)


load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('TOKEN')


def main() -> None:
    bot.run(token=DISCORD_TOKEN)


if __name__ == '__main__':
    main()
