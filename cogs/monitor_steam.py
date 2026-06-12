import discord
from discord.ext import commands, tasks
import aiohttp
import os


STEAM_API_KEY = os.getenv("STEAM_API_KEY") 
CANAL_ALERTAS_ID = 339131360662913024      

class MonitorSteam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.servicios_caidos = False 
        self.verificar_steam.start()

    def cog_unload(self):
        self.verificar_steam.cancel()

    @tasks.loop(minutes=5)
    async def verificar_steam(self):
        url = f"https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key={STEAM_API_KEY}"
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        datos = await response.json()
                        services = datos.get("result", {}).get("services", {})
                        
                        comunidad = services.get("Community", "normal")
                        tienda = services.get("Web", "normal") 
                        sesiones = services.get("Sessions", "normal") 
                        
                        caida_detectada = (comunidad != "normal" or tienda != "normal" or sesiones != "normal")
                        
                        if caida_detectada and not self.servicios_caidos:
                            self.servicios_caidos = True
                            await self.enviar_alerta(caida_detectada, comunidad, tienda, sesiones)
                            
                        elif not caida_detectada and self.servicios_caidos:
                            self.servicios_caidos = False
                            await self.enviar_alerta(caida_detectada, comunidad, tienda, sesiones)
                            
                    else:
                        print(f"Error de API Steam: Código de estado {response.status}")
                        
            except Exception as e:
                print(f"Error de conexión al verificar Steam: {e}")

    async def enviar_alerta(self, hay_caida, comunidad, tienda, sesiones):
        canal = self.bot.get_channel(CANAL_ALERTAS_ID)
        if not canal:
            return

        if hay_caida:
            embed = discord.Embed(
                title="⚠️ ¡HABLAMO STEAM!",
                description="Se cayo esa mierda, not stonks valve",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjc0cXo0eWhiZmY4eTZ2d3pkcWVhYTBpbG5wNWMwNTYyaTZwODd0ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Oj8pUuT5FOpxHH9LIk/giphy.gif")
            embed.add_field(name="🌐 Inicio de Sesión", value=f"🔴 {sesiones.upper()}" if sesiones != "normal" else "🟢 NORMAL", inline=True)
            embed.add_field(name="🛒 Tienda / Web API", value=f"🔴 {tienda.upper()}" if tienda != "normal" else "🟢 NORMAL", inline=True)
            embed.add_field(name="👥 Comunidad", value=f"🔴 {comunidad.upper()}" if comunidad != "normal" else "🟢 NORMAL", inline=True)
            embed.set_footer(text="Mantenimiento habitual o caída general.")
            
            await canal.send(embed=embed)
        else:
            embed = discord.Embed(
                title="✅ Ya volvio",
                description="Ahora si stonks",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2xmdm12cHV1d3Rzb3kwejZ1ZXk2ODRycWt3NHNiMmxwYjhnNW55OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YnkMcHgNIMW4Yfmjxr/giphy.gif")
            await canal.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MonitorSteam(bot))