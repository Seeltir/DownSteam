import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
TOKEN_DISCORD = os.getenv("DISCORD_TOKEN") 


intents = discord.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🚀 ¡Bot encendido y conectado como {bot.user}!")
    print("El monitor de Steam ya está corriendo de fondo.")

async def load_extensions():
    try:
        await bot.load_extension("cogs.monitor_steam")
        print("✅ Módulo de Steam cargado con éxito.")
    except Exception as e:
        print(f"❌ Error al cargar el módulo de Steam: {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN_DISCORD)

if __name__ == "__main__":
    asyncio.run(main())