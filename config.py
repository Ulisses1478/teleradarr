import os

radarrIp = os.getenv('RADARR_IP')
radarrPort = os.getenv('RADARR_PORT')
radarrCustomPath = os.getenv('RADARR_CUSTOM_PATH')

if not radarrIp:
	print('No ip specified')
if not radarrPort:
	print('No port specified')

radarrUrl = f'{radarrIp}:{radarrPort}'

if radarrCustomPath:
	radarrUrl += radarrCustomPath

CONFIG = {
    'radarr':{
        'baseUrl':radarrUrl or 'http://10.0.0.99:7878/radarr', # NO SLASH AT THE END
        'apiKey':os.getenv('RADARR_API_KEY') or '8dde1681b6714322a0a89516f98fbb46'
    },
    'telegram':{
        'botToken':os.getenv('TELEGRAM_BOT_TOKEN') or '1391034221:AAEzxhI5R1ZIIYnNG_NQyYug6LtvJjT9Lmo'
    }
}
