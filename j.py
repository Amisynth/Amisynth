import discord
from Amisynth.utils import menu_options
# Diccionario para almacenar las opciones de cada menú por su ID
import xfox

import asyncio



@xfox.addfunc(xfox.funcs)
async def numero(*args, **kwargs):
    """Agrega una opción al menú de selección, almacenándola en una lista por ID."""
    return "1"




print(asyncio.run(xfox.parse("$eval[$numero[]]")))


