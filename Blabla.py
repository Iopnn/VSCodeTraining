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
async def help(ctx):
    await ctx.send("1- brainrot, 2- alpasin, 3- fuckjews, 4- meray")

@bot.command()
async def brainrot(ctx):
    brainrotList = ["Meray", "Popoy", "Alpasin", "Alpablanc", "Berere"]
    brainrotFinal = random.choice(brainrotList)
    await ctx.send(f"Your random number is {brainrotFinal}")

@bot.command()
async def alpasin(ctx):
    await ctx.send("Fuck les alpasin")

@bot.command()
async def fuckjews(ctx):
    await ctx.send("Fuck the fucking jews")

@bot.command()
async def meray(ctx):
    await ctx.send("Popoy ay ay magazine")

import os

token = os.getenv("TOKEN")  # Make sure TOKEN is set in your environment
if token is None:
    raise ValueError("No Discord bot token found in environment variables")

print("TOKEN:", token[:5], "..." if token else "None")
bot.run(token)