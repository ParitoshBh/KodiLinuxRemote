import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class EventHandler:
    def onConnectClicked(self):
        print(self)

class Remote:
    username = None
    password = None

    def __init__(self, user_credentials):
        self.username = user_credentials['username']
        self.password = user_credentials['password']

    def load_window(self):
        builder = Gtk.Builder()
        # handler = Handler(builder)
        # builder.add_from_file("view/test.glade")
        builder.add_from_file("view/remote.glade")
        builder.connect_signals(EventHandler())

        window = builder.get_object("windowRemote")
        window.connect("delete-event", Gtk.main_quit)
        window.show()

        Gtk.main()