import discord # type: ignore
from discord.ext import commands, tasks # type: ignore
import requests
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

@bot.event
async def on_ready():
    print(f"WallDrop conectado como {bot.user}")
    post_wallpapers.start()

@tasks.loop(hours=24)
async def post_wallpapers():
    try:
        response = requests.get("http://localhost:8000/wallpapers")
        response.raise_for_status()
        wallpapers = response.json().get("wallpapers", [])
        
        channel = bot.get_channel(CHANNEL_ID)
        if not channel:
            print("Canal não encontrado!")
            return
        
        await channel.send("🔥 WallDrop: Wallpapers mais hypados do Wallpaper Engine! 🔥")
        for wp in wallpapers[:3]:
            embed = discord.Embed(
                title=wp["title"],
                url=wp["link"],
                color=discord.Color.blue()
            )
            embed.set_image(url=wp["image"])
            embed.set_footer(text="Powered by WallDrop")
            await channel.send(embed=embed)
    
    except Exception as e:
        print(f"Erro ao postar wallpapers: {e}")

@bot.command()
async def wallpapers(ctx):
    """Dropa wallpapers manualmente"""
    await post_wallpapers()

bot.run(os.getenv("DISCORD_TOKEN"))