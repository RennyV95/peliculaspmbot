# Cursos Pro Android by Skueletor ©️ 2021
import re
from os import environ

# Información del bot
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Ajustes del bot
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Administradores, canales y usuarios
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Información de MongoBD
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Mensajes
START_MSG = """
Hola, soy un bot de búsqueda de películas de 🌎 **PʟᴀɴᴇᴛᴀMᴏᴠɪᴇs** 🌎
Conmigo puede buscar las peliculas que estan en el canal en modo inline.

Simplemente presione los siguientes botones y comience a buscar las peliculas subidas al canal.
"""

SHARE_BUTTON_TEXT = 'Revisa {username} para buscar peliculas en forma **inline**'
