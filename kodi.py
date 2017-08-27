import requests
from requests.exceptions import ConnectionError
from settings import Settings

class Kodi():
    protocol = 'http://'
    username = None
    password = None
    ip_address = None
    port = None
    player_id = None

    def __init__(self, username, password, ip_address, port):
        self.username = username
        self.password = password
        self.ip_address = ip_address
        self.port = port

    def Connect(self):
        try:
            response = requests.get('http://' + self.ip_address + ':' + self.port + '/jsonrpc', auth=(self.username, self.password))
            # print(response.json())
            settings = Settings()
            settings.Save({'ip_address' : self.ip_address, 'port' : self.port, 'username' : self.username, 'password' : self.password})
            return True
        except ConnectionError as conn_error:
            print(conn_error)
            return False

    def Handshake(self):
        try:
            # print(response.json())
            self.player_id = self.GetActivePlayers()
            currentPlaying = self.PlayerGetItem()
            return currentPlaying
        except ConnectionError as conn_error:
            print(conn_error)
            return False

    def GetActivePlayers(self):
        response = requests.get(self.protocol + self.ip_address + ':' + self.port + '/jsonrpc?request={"jsonrpc":"2.0","id": 1,"method":"Player.GetActivePlayers"}', auth=(self.username, self.password))
        response = response.json()
        return response['result'][0]['playerid']

    def PlayerGetItem(self):
        response = requests.get(self.protocol + self.ip_address + ':' + self.port + '/jsonrpc?request={"jsonrpc":"2.0","id": 1,"method":"Player.GetItem","params":{"playerid":' + str(self.player_id) + '}}', auth=(self.username, self.password))
        response = response.json()
        return response['result']['item']['label']

    def PlayPause(self):
        response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Player.PlayPause","params":{"playerid":1}}', auth=(self.username, self.password))

    def SetVolume(self, type):
        if type == 'increase':
            response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume":"increment"}}', auth=(self.username, self.password))
        else:
            response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume":"decrement"}}', auth=(self.username, self.password))