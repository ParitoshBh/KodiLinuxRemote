import requests
from requests.exceptions import ConnectionError
from settings import Settings
from urlhelper import UrlHelper

class Kodi():
    player_id = None
    username = None
    password = None
    url_helper = None
    parent_params = None

    def __init__(self, username, password, ip_address, port):
        self.url_helper = UrlHelper(ip_address, port)
        self.ip_address = ip_address
        self.port = port
        self.username = username
        self.password = password
        self.parent_params = {}

    def Connect(self):
        try:
            # TODO Save settings based on response
            response = requests.get(self.url_helper.prepare_url_without_param('Player.GetActivePlayers'), auth=(self.username, self.password))
            settings = Settings()
            settings.Save({'ip_address' : self.ip_address, 'port' : self.port, 'username' : self.username, 'password' : self.password})
            return True
        except ConnectionError as conn_error:
            print(conn_error)
            return False

    def Handshake(self):
        try:
            self.player_id = self.GetActivePlayers()
            # print(self.player_id)
            if self.player_id is None:
                currentPlaying = 'Nothing is playing'
            else:
                currentPlaying = self.PlayerGetItem()
            return currentPlaying
        except ConnectionError as conn_error:
            # print(conn_error)
            return False

    def GetActivePlayers(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Player.GetActivePlayers'), auth=(self.username, self.password))
        response = response.json()['result']
        # check if something is playing
        if len(response) == 0:
            return None
        else:
            return response[0]['playerid']

    def PlayerGetItem(self):
        params = self.url_helper.prepare_param(self.parent_params, {'name': 'playerid', 'value': self.player_id})
        response = requests.get(self.url_helper.prepare_url_with_param('Player.GetItem', params), auth=(self.username, self.password))
        self.parent_params = {}
        response = response.json()
        return response['result']['item']['label']

    def InputBack(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Back'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def InputLeft(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Left'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def InputRight(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Right'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def InputSelect(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Select'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def InputUp(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Up'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def InputDown(self):
        response = requests.get(self.url_helper.prepare_url_without_param('Input.Down'), auth=(self.username, self.password))
        self.ParseResponse(response)

    def PlayPause(self):
        params = self.url_helper.prepare_param(self.parent_params, {'name': 'playerid', 'value': self.player_id})
        response = requests.get(self.url_helper.prepare_url_with_param('Player.PlayPause', params), auth=(self.username, self.password))
        self.parent_params = {}
        self.ParseResponse(response)

    def Stop(self):
        params = self.url_helper.prepare_param(self.parent_params, {'name': 'playerid', 'value': self.player_id})
        response = requests.get(self.url_helper.prepare_url_with_param('Player.Stop', params), auth=(self.username, self.password))
        self.parent_params = {}
        self.ParseResponse(response)

    def Previous(self):
        parent_params = self.url_helper.prepare_param(self.parent_params, {'name': 'playerid', 'value': self.player_id})
        parent_params = self.url_helper.prepare_param(self.parent_params, {'name': 'to', 'value': 'previous'})
        response = requests.get(self.url_helper.prepare_url_with_param('Player.GoTo', parent_params), auth=(self.username, self.password))
        self.parent_params = {}
        self.ParseResponse(response)

    def SetVolume(self, vol_type):
        params = self.url_helper.prepare_param(self.parent_params, {'name': 'volume', 'value': vol_type})
        response = requests.get(self.url_helper.prepare_url_with_param('Application.SetVolume', params), auth=(self.username, self.password))
        self.parent_params = {}
        self.ParseResponse(response)

    def ParseResponse(self, response):
        response = response.json()
        # print(response)