# Instanciamos el bot


from Amisynth.client import AmiClient


bot = AmiClient(prefix="!")


bot.new_command("etc", 
                "text",
                """
Canal ID: $channelID[]
Author: $authorID[]
usernae = $username[]
channels: $channelNames[,]
categorias: $categorys[,]
                """)


bot.run("")
