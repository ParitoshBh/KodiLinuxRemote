import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from kodi import Kodi
from remote import Remote

class EventHandler:
    builder = None

    def __init__(self, builder):
        self.builder = builder

    def onConnectClicked(self, button):
        ip_address = self.builder.get_object('entryIPAddress').get_text()
        port = self.builder.get_object('entryPort').get_text()
        username = self.builder.get_object('entryUsername').get_text()
        password = self.builder.get_object('entryPassword').get_text()
        self.attemptConnection(ip_address, port, username, password)

    def attemptConnection(self, ip_address, port, username, password):
        kodi = Kodi(username, password, ip_address, port)
        isConnected = kodi.Connect()
        if isConnected:
            print('Connected. Load remote window')
            self.builder.get_object('windowSetup').hide()
            remoteWin = Remote({'ip_address': ip_address, 'port': port, 'username': username, 'password': password})
            remoteWin.load_window(self.builder)
        else:
            print('Unable to connect. Keep showing setup window')

    def onDeleteClicked(self, button, args):
        Gtk.main_quit()