# Instanciamos el bot


from Amisynth.client import AmiClient


bot = AmiClient(prefix="!")


bot.new_event("$onMessage", "Canal ID: $channelID[]")

bot.run("")
