import requests
from requests.exceptions import ConnectionError
from settings import Settings

class Kodi():
    username = None
    password = None
    ip_address = None
    port_number = None

    def __init__(self, username, password, ip_address, port_number):
        self.username = username
        self.password = password
        self.ip_address = ip_address
        self.port_number = port_number

    def Connect(self):
        try:
            response = requests.get('http://192.168.1.104:9000/jsonrpc', auth=(self.username, self.password))
            # print(response.json())
            settings = Settings()
            settings.Save({'username' : self.username, 'password' : self.password})
        except ConnectionError as conn_error:
            response = 'Unable to connect'
            print(response)

    def GetActivePlayers(self):
        response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Player.GetActivePlayers"}', auth=('kodi', 'kodi'))

    def PlayPause(self):
        response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Player.PlayPause","params":{"playerid":1}}', auth=(self.username, self.password))

    def SetVolume(self, type):
        if type == 'increase':
            response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume":"increment"}}', auth=(self.username, self.password))
        else:
            response = requests.get('http://192.168.1.104:9000/jsonrpc?request={"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume":"decrement"}}', auth=(self.username, self.password))