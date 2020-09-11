import requests


class FBApi:
    FB_URL = "https://graph.facebook.com"

    def __init__(self, logging=None):
        self.logging = logging
        self.session = self._generate_session()

    @staticmethod
    def _generate_session():
        fb_req = requests.session()
        fb_req.headers.update(
            {'Content-Type': 'application/json'}
        )

        return fb_req

    def get_app_token(self, client_id, client_secret):
        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }

        token = self.session.get('{url}/oauth/access_token'.format(
            url=self.FB_URL
        ), params=params)

        auth_token = {'access_token': token.json()['access_token']}

        return auth_token
