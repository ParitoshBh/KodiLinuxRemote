import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from kodi import Kodi

class Remote:
    ip_address = None
    port = None
    username = None
    password = None

    def __init__(self, user_credentials):
        self.ip_address = user_credentials['ip_address']
        self.port = user_credentials['port']
        self.username = user_credentials['username']
        self.password = user_credentials['password']

    def load_window(self, builder):
        window = builder.get_object("windowRemote")
        window.set_title('KodiLinuxRemote')
        window.show()
        # Communicate with kodi
        kodi = Kodi(self.username, self.password, self.ip_address, self.port)
        # Alter UI based on currently playing media
        self.load_now_playing(kodi, builder)
        return kodi

    def load_now_playing(self, kodi, builder):
        currentPlaying = kodi.Handshake()
        self.toggle_playback_button(builder, currentPlaying)

    def toggle_playback_button(self, builder, currentPlaying):
        buttonPlayPause = builder.get_object('buttonMediaPlayPause')
        if currentPlaying:
            if currentPlaying == 'Nothing is playing':
                image = Gtk.Image(stock=Gtk.STOCK_MEDIA_PLAY)
            else:
                image = Gtk.Image(stock=Gtk.STOCK_MEDIA_PAUSE)
        else:
            image = Gtk.Image(stock=Gtk.STOCK_MEDIA_PLAY)
        buttonPlayPause.set_image(image)