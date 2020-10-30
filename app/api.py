from .config import CONFIG
import requests, urllib.parse as urllib
import json as jj
class radarr:
    def __init__(self):
        self.baseUrl = CONFIG['radarr']['baseUrl']
        self.apiKey = CONFIG['radarr']['apiKey']

    def get(self, endpoint, params=None):
        if params:
            params['apikey'] = self.apiKey
        return requests.get(self.baseUrl + '/api' + endpoint, params=params).json()

    def post(self, endpoint, json):
        params = {
            'apikey':self.apiKey
        }

        response = requests.post(self.baseUrl + '/api' + endpoint, params=params, json=json)

        if response.status_code not in ['200', '201']:
            return False

        return response.json()

    def searchMovies(self, term, limit=0):
        data = self.get('/movie/lookup/', {
            'term':term
        })
        if limit > 0:
            return data[:limit]
        else:
            return data

    def addMovie(self, movie):
        movie.update({
        "monitored":True,
        "profileId": 4,
        "episodeFileCount": 0,
        "episodeCount": 0,
        "isExisting": False,
        "saved": False,
        "deleted": False,
        "rootFolderPath": "/media/movies",
        "addOptions": {
            "ignoreEpisodesWithFiles":False,
            "ignoreEpisodesWithoutFiles":False,
            "searchForMovie":True
        },
        })
        response = self.post('/movie', json=movie)

        if response:
            return True

        return False
