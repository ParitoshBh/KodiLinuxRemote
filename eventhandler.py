import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from kodi import Kodi
from remote import Remote

class EventHandler:
    builder = None
    kodi = None

    def __init__(self, builder):
        self.builder = builder

    def initKodiObj(self, kodi):
        self.kodi = kodi

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

    def onBackClicked(self, button):
        self.kodi.InputBack()

    def onMediaStopClicked(self, button):
        pass

    def onMediaPlayPauseClicked(self, button):
        pass

    def onMediaPreviousClicked(self, button):
        pass

    def onMediaRewindClicked(self, button):
        pass

    def onMediaNextClicked(self, button):
        pass

    def onMediaForwardClicked(self, button):
        pass