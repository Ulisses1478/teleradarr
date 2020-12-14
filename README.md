# Teleradarr

## Contribution
This software is 100% free and I made it as a side project, the bot conversation it doesn't even exists and if you wan't to help to make this bot check the to-do down there and make your commit

## How to install

### Config the application
To start the server you need to first config the file located in app/config_example.py and rename it to config.py

```
CONFIG = {
    'radarr':{
        'baseUrl':'http://ip:port/radarr', # Here put your base url without the slash and with the sufix like in mine the sufix is /radarr
        'apiKey':'7ay7dfas7df79ab70742709471907asdf' # Here you put your api key from radarr look for that in the Radarr Settings Credentials page
    },
    'telegram':{
        'botToken':'number:something' # Get with telegram BotFather and activate inline
    }
}
```

### Telegram config
It is 100% necessary that you after creating your bot with BotFather

Run the commands
```/setinline```
and
```/setinlinefeedback```

## Running the application
I made it as simple as possible

You will only need python3

### Install the requirements
Can be pip3 in your case

```
pip install -r requirements.txt
```

### Start command
Can be python3 in your case

```
python startBot.py
```

### Usage
To use the bot is very simple after getting the bot with the right permissions, you need to run

```
@BOT_NAME NAME_OF_THE_MOVIE
```

### Docker Variables
| Variable Name | Default | What it does
| ------------- |:-------------:| -----:|
| RADARR_IP | Null | Set radarr instance ip|
| RADARR_PORT | Null | Set radarr instance port|
| RADARR_API_KEY | Null | Set radarr api key|
| RADARR_PROFILE_ID | 1 (Any) | Change default radarr profile|
| RADARR_CUSTOM_PATH | Null | Change default path for radarr like ip:port/path/|
| RADARR_CUSTOM_FOLDER | /media/movies | Change the save folder for radarr|
| TELEGRAM_BOT_TOKEN | Null | Set Telegram api key|

radarrProfileId = os.getenv('RADARR_PROFILE_ID')
### TO-DO
- [x] Radarr inline integration
- [ ] Sonarr inline integration
- [ ] Automated tests
- [ ] Sonarr & Raddar chat integration
