import xfox
import discord
from Amisynth.utils import buttons, menu_options

@xfox.addfunc(xfox.funcs)
async def newSelectMenu(placeholder: str, min_val: int, max_val: int, menu_id: str, *args, **kwargs):
    """Crea un menú de selección interactivo con opciones."""
    ctx = kwargs["ctx_command"] or kwargs["ctx_slash_env"]
    global row_counter  # Para modificar el contador de fila

    # Extraer valores opcionales
    message_id = None
    if len(args) > 0:
        message_id = args[0]  # ID del mensaje al que se vinculará el menú

    # Obtener las opciones del menú por su ID desde menu_options
    options = menu_options.get(menu_id, [])

    # Crear el menú de selección
    select_menu = discord.ui.Select(
        placeholder=placeholder if placeholder else "Seleccione una opción",
        min_values=min_val,
        max_values=max_val,
        options=options,
        custom_id=menu_id
    )

    # Si hay un message_id, editar el mensaje existente
    if message_id:
        message_id = int(message_id)  # Convertir a número
        channel = ctx.channel  # Obtener el canal
        message = await channel.fetch_message(message_id)  # Obtener el mensaje
        if message.components:
            view = discord.ui.View.from_message(message)  # Recuperar los componentes existentes
        else:
            view = discord.ui.View()  # Crear una nueva vista si no hay componentes

        view.add_item(select_menu)  # Agregar el menú de selección
        await message.edit(view=view)  # Editar el mensaje con la nueva vista
        return ""

    # Si no hay message_id, devolver el menú como un componente independiente

    buttons.append(select_menu)
    return ""
