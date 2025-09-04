import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')

kredi = 0

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı!')
    print('------')

@bot.command(name='kredi')
async def bot_kredi_goster(ctx):
    await ctx.send(f"Mevcut kredi: **{kredi}**")

bot.run(TOKEN)