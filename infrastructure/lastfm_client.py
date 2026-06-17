import requests

class LastFMClient:

    def __init__(self, 
                 api_key,
                 user
                    ):
        
        self.api_key = api_key
        self.user = user

    def get_recent_tracks(self):

        response = requests.get(
            'http://ws.audioscrobbler.com/2.0/',
            params={
                'method': 'user.getrecenttracks',
                'user': self.user,
                'api_key': self.api_key,
                'format': 'json',
                'limit': 5
            }
        )

        response.raise_for_status()

        return response.json()
    