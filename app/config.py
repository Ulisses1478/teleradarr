import os

radarrIp = os.getenv('RADARR_IP')
radarrPort = os.getenv('RADARR_PORT')
radarrCustomPath = os.getenv('RADARR_CUSTOM_PATH')
radarrProfileId = os.getenv('RADARR_PROFILE_ID')
radarrCustomFolder = os.getenv('RADARR_CUSTOM_FOLDER')

if not radarrIp:
	print('No ip specified')
if not radarrPort:
	print('No port specified')

radarrUrl = f'http://{radarrIp}:{radarrPort}'

if radarrCustomPath:
	radarrUrl += radarrCustomPath

# The os.getenv and raddarUrl is when used in docker
CONFIG = {
    'radarr':{
        'baseUrl':radarrUrl or 'http://ip:port/radarr', # NO SLASH AT THE END
        'apiKey':os.getenv('RADARR_API_KEY', '7ay7dfas7df79ab70742709471907asdf'), # Can be found in credentials
		'profileId':radarrProfileId or '1',
		'folder':radarrCustomFolder or '/media/movies'
	},
    'telegram':{
        'botToken':os.getenv('TELEGRAM_BOT_TOKEN', 'number:something')  # Get with telegram BotFatheR
    }
}
