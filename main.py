import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.kredi = 0

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı!')

@bot.command(name='yardım')
async def kredi_goster(ctx):
    await ctx.send(f"!kredi - Botun kredi bakiyesini gösterir.\n"
                   f"!krediekle <miktar> - Botun kredi bakiyesine miktar ekler (Yönetici izni gerektirir).")

@bot.command(name='kredi')
async def kredi_goster(ctx):
    await ctx.send(f"Botun güncel kredi bakiyesi: **{bot.kredi}**")

@bot.command(name='krediekle')
@commands.has_permissions(administrator=True)
async def kredi_ekle(ctx, miktar: int):
    bot.kredi += miktar
    await ctx.send(f"**{miktar}** kredi eklendi. Yeni bakiye: **{bot.kredi}**")

@kredi_ekle.error
async def kredi_ekle_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu kullanma izniniz yok.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Lütfen geçerli bir sayı girin.")
    else:
        await ctx.send("Bir hata oluştu.")

bot.run(TOKEN)