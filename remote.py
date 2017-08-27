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
        window.show()