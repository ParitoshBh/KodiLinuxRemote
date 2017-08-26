import os
import configparser
from gi.repository import GLib

class Settings():
    config = configparser.ConfigParser()
    settings_path = None
    settings = None

    def __init__(self):
        data_dir = os.path.join(GLib.get_user_data_dir(), 'kodiremote')
        self.settings_path = os.path.join(data_dir, 'settings.ini')

        # check if settings path exists
        if os.path.exists(self.settings_path):
            # load settings from file
            self.settings = self.LoadSettings(self.config)
        else:
            # create the directory
            os.makedirs(data_dir)
            # intialize .ini file with defaults
            self.config['DEFAULT'] = {'username': '', 'password': '', 'ipaddress': '', 'port' : ''}
            with open(self.settings_path, 'w') as settings_file:
                self.config.write(settings_file)

    def Save(self, userSettings):
        # print(self.config.sections())
        if len(self.config.sections()) == 0:
            self.config['user.defined'] = {}
            user_defined = self.config['user.defined']
            user_defined['username'] = userSettings['username']
            user_defined['password'] = userSettings['password']
            with open(self.settings_path, 'w') as settings_file:
                self.config.write(settings_file)

    def LoadSettings(self, config):
        config.read(self.settings_path)
        if 'user.defined' in config:
            return config['user.defined']
        else:
            print('Unable to load user values')
            return None

    def GetSettings(self):
        return self.settings