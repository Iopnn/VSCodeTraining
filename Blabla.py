import math
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def commands_list(ctx):
    await ctx.send("1- brainrot, 2- alpasin, 3- fuckjews, 4- meray, fuck niggers")

@bot.command()
async def brainrot(ctx):
    brainrotList = ["Meray", "Popoy", "Alpasin", "Alpablanc", "Berere"]
    brainrotFinal = random.choice(brainrotList)
    await ctx.send(f"Your random brainrot is {brainrotFinal}")

@bot.command()
async def alpasin(ctx):
    await ctx.send("Fuck les alpasin et les alpablanc")

@bot.command()
async def fuckjews(ctx):
    await ctx.send("Fuck the fucking jews")

@bot.command()
async def meray(ctx):
    await ctx.send("Popoy ay ay magazine")

@bot.command()
async def quoi(ctx):
    await ctx.send("feur")

@bot.command()
async def sixseven(ctx):
    await ctx.send("67")

@bot.command()
async def triplet(ctx):
    await ctx.send("Tung tung tung sahur")


import os

token = os.getenv("TOKEN")  # Make sure TOKEN is set in your environment
if token is None:
    raise ValueError("No Discord bot token found in environment variables")

print("TOKEN:", token[:5], "..." if token else "None")
bot.run(token)