# Instanciamos el bot


from Amisynth.client import AmiClient


bot = AmiClient(prefix="!")


bot.new_command("etc", "text", """$eval[$message[1]]
                """)

bot.run("")
