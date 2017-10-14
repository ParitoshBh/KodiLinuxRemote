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

    def onLeftClicked(self, button):
        self.kodi.InputLeft()

    def onRightClicked(self, button):
        self.kodi.InputRight()

    def onCenterClicked(self, button):
        self.kodi.InputSelect()

    def onUpClicked(self, button):
        self.kodi.InputUp()

    def onDownClicked(self, button):
        self.kodi.InputDown()

    def onMediaStopClicked(self, button):
        self.kodi.Stop()

    def onMediaPlayPauseClicked(self, button):
        self.kodi.PlayPause()

    def onMediaPreviousClicked(self, button):
        self.kodi.Previous()

    def onMediaRewindClicked(self, button):
        pass

    def onMediaNextClicked(self, button):
        self.kodi.Next()

    def onMediaForwardClicked(self, button):
        pass

    def onVolumeDecreaseClicked(self, button):
        self.kodi.SetVolume('decrement')

    def onVolumeIncreaseClicked(self, button):
        self.kodi.SetVolume('increment')

    def onVolumeToggleClicked(self, button):
        pass

    def onKeyReleaseEvent(self, key, args):
        key_code = args.get_keycode()[1]

        # Backspace
        if key_code is 22:
            self.kodi.InputBack()
        # Key left
        elif key_code is 113:
            self.kodi.InputLeft()
        # Key right
        elif key_code is 114:
            self.kodi.InputRight()
        # Key up
        elif key_code is 111:
            self.kodi.InputUp()
        # Key down
        elif key_code is 116:
            self.kodi.InputDown()
        # Enter
        elif key_code is 36:
            self.kodi.InputSelect()
        # Plus key
        elif key_code is 20:
            self.kodi.SetVolume('decrement')
        # Minus key
        elif key_code is 21:
            self.kodi.SetVolume('increment')
        # Spacebar
        elif key_code is 65:
            self.kodi.PlayPause()
        else:
            print(key_code)