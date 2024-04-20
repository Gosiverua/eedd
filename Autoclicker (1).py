import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.channel.id == 1173706944796692560:
        await message.add_reaction("⭐")

bot.run('MTIzMTE4NTA4MzM2NTMyNjg2OQ.GWqTcQ.I1G-YPP8W-cwbh2AqjLSkmrSfCYqfIBGbnW7t4')
