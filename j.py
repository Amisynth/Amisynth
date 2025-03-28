import xfox
import asyncio

# JSON de prueba
json_storage = {"name": [{"user": ["Alice", "Bob"]}, {"user": ["Charlie", "Dave"]}]}

@xfox.addfunc(xfox.funcs)
async def json(*args, **kwargs):
    try:
        data = json_storage  # Inicia con el JSON base

        for clave in args:
            if isinstance(data, dict) and clave in data:
                data = data[clave]  # Acceder a clave en diccionario
            elif isinstance(data, list):
                try:
                    index = int(clave)  # Convertir clave a entero si es índice
                    data = data[index]  # Acceder a índice en lista
                except ValueError:
                    return f""
                    
                except IndexError:
                    return f""
            else:
                return f""
        
        return data  # Devuelve el resultado final
    except Exception as e:
        raise ValueError(f"Error inesperado: {str(e)}")

# Pruebas con diferentes estructuras
print(asyncio.run(xfox.parse("$json[name;0;user;0]")))  # Alice
print(asyncio.run(xfox.parse("$json[name;1;user;1]")))  #
