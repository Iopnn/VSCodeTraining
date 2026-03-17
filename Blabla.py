import math
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def brainrot(ctx):
    brainrotList = ["Meray", "Popoy", "Alpasin", "Alpablanc", "Berere"]
    randomIndex = random.randint(1, len(brainrotList))
    brainrotFinal = brainrotList[randomIndex]
    await ctx.send(f"Your random number is {brainrotFinal}")

import os

token = os.getenv("TOKEN")  # Make sure TOKEN is set in your environment
if token is None:
    raise ValueError("No Discord bot token found in environment variables")

print("TOKEN:", token[:5], "..." if token else "None")
bot.run(token)