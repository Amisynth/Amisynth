# Instanciamos el bot


from Amisynth.client import AmiClient


bot = AmiClient(prefix="!", 
                variables_json=True)

bot.new_command("etc", 
                "text", 
                """
$title[hola;1]
$eval[$message[-1]]
""")
bot.run("")
