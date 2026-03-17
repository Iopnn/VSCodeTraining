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
bot.run(os.getenv("TOKEN"))