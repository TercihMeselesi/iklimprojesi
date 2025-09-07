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
async def yardim(ctx):
    await ctx.send("**Kredi Sistemi Komutları:**\n"
                   "`!kredi` - Güncel kredi bakiyenizi gösterir.\n"
                   "`!satınalımrehberi` - Satın alabileceğiniz ürünlerin listesini gösterir.\n"
                   "`!satınal <ürün numarası>` - Belirtilen ürün numarasındaki ürünü satın alır.\n")

@bot.command(name='satınalımrehberi')
async def alimrehberi(ctx):
    await ctx.send(f"1 - TEMA Vakfı'na 100 TL bağış yönlendir (10 kredi)\n"
                   f"2 - ÇEVKO Vakfı'na 100 TL bağış yönlendir (10 kredi)\n"
                   f"3 - Bir ağaç fidanı dikilmesini sağla (14 kredi)\n"
                   f"4 - Bir güneş paneli kurulmasını sağla (20 kredi)\n"
                    f"5 - Bir su kuyusu açılmasını sağla (50 kredi)\n")

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

@bot.command(name='satınal')
async def kredi_ekle(ctx, urun: int):

    if urun == 1:
        if bot.kredi < 10:
            await ctx.send(f"Yeterli krediniz yok. Şuanki bakiye: **{bot.kredi}**")
            return
        bot.kredi -= 10
        await ctx.send(f"**{10}** kredi karşılığında bir TEMA Vakfı'na 100 TL değerinde bağış yönlendirdiniz. Desteğiniz için teşekkür ederiz. Yeni bakiye: **{bot.kredi}**")

    elif urun == 2:
        if bot.kredi < 10:
            await ctx.send(f"Yeterli krediniz yok. Şuanki bakiye: **{bot.kredi}**")
            return
        bot.kredi -= 10
        await ctx.send(f"**{10}** kredi karşılığında bir ÇEVKO Vakfı'na 100 TL değerinde bağış yönlendirdiniz. Desteğiniz için teşekkür ederiz. Yeni bakiye: **{bot.kredi}**")

    elif urun == 3:
        if bot.kredi < 14:
            await ctx.send(f"Yeterli krediniz yok. Şuanki bakiye: **{bot.kredi}**")
            return
        bot.kredi -= 14
        await ctx.send(f"**{14}** kredi karşılığında bir ağaç fidanı dikilmesini sağladınız. Desteğiniz için teşekkür ederiz. Yeni bakiye: **{bot.kredi}**")

    elif urun == 4:
        if bot.kredi < 20:
            await ctx.send(f"Yeterli krediniz yok. Şuanki bakiye: **{bot.kredi}**")
            return
        bot.kredi -= 20
        await ctx.send(f"**{20}** kredi karşılığında bir güneş paneli kurulmasını sağladınız. Desteğiniz için teşekkür ederiz. Yeni bakiye: **{bot.kredi}**")

    elif urun == 5:
        if bot.kredi < 50:
            await ctx.send(f"Yeterli krediniz yok. Şuanki bakiye: **{bot.kredi}**")
            return
        bot.kredi -= 50
        await ctx.send(f"**{50}** kredi karşılığında bir su kuyusu açılmasını sağladınız. Desteğiniz için teşekkür ederiz. Yeni bakiye: **{bot.kredi}**")

bot.run(TOKEN)