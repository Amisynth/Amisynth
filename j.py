import xfox
import discord
import Amisynth.utils as utils
import asyncio
try:
    print(asyncio.run(xfox.parse("$onlyIf[1==1;Falso]")))
except ValueError as e:
    print(e)