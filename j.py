import discord
from discord.ext import commands

intents = discord.Intents().all()
intents.members = True  # Asegúrate de habilitar los intents de miembros

# Crea una instancia de bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento on_member_join
@bot.event
async def on_member_join(member):
    # Este evento se dispara cuando un nuevo miembro se une al servidor
    print(f"{member.name} se unió al servidor!")

    # Usa el ID de canal para obtener el canal en lugar del nombre
    channel_id = 1354997612234674226  # Reemplaza con el ID de canal al que quieres enviar el mensaje
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(f"¡Bienvenido al servidor, {member.mention}! 🎉")

    # Si quieres dar un mensaje de bienvenida al canal privado del miembro
    try:
        await member.send(f"¡Hola {member.name}! Gracias por unirte al servidor.")
    except discord.Forbidden:
        print(f"No se pudo enviar un DM a {member.name}.")

# Evento on_ready
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Inicia el bot con tu token
bot.run('')
