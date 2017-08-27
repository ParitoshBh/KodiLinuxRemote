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
        labelStatus = builder.get_object('labelStatus')
        labelStatus.set_text('Connecting with Kodi...')
        kodi = Kodi(self.username, self.password, self.ip_address, self.port)
        currentPlaying = kodi.Handshake()
        if currentPlaying:
            labelStatus.set_text(currentPlaying)
        else:
            labelStatus.set_text('Unable to connect with Kodi')
