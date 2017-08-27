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
            settings = self.LoadSettings(self.config)
            if settings is not None:
                self.settings = settings
            else:
                self.initSettingsFile(data_dir)
        else:
            self.initSettingsFile(data_dir)

    def initSettingsFile(self, data_dir):
        try:
            # try to create the directory
            os.makedirs(data_dir)
        except FileExistsError as file_error:
            print('File already exists. Overwriting settings')
        finally:
            # intialize .ini file with defaults
            self.config['DEFAULT'] = {'username': '', 'password': '', 'ip_address': '', 'port' : ''}
            with open(self.settings_path, 'w') as settings_file:
                self.config.write(settings_file)

    def Save(self, userSettings):
        # print(self.config.sections())
        if len(self.config.sections()) == 0:
            self.config['user.defined'] = {}
            user_defined = self.config['user.defined']
            user_defined['username'] = userSettings['username']
            user_defined['password'] = userSettings['password']
            user_defined['ip_address'] = userSettings['ip_address']
            user_defined['port'] = userSettings['port']
            with open(self.settings_path, 'w') as settings_file:
                self.config.write(settings_file)

    def LoadSettings(self, config):
        config.read(self.settings_path)
        if 'user.defined' in config:
            return config['user.defined']
        else:
            print('Settings file found. Format corrupted.')
            return None

    def GetSettings(self):
        return self.settings