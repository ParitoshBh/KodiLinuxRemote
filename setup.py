import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class EventHandler:
    builder = None

    def __init__(self, builderObj):
        self.builder = builderObj

    def onConnectClicked(self, button):
        print(self.builder.get_object('entryUsername').get_text())

class Setup:
    def load_window(self):
        builder = Gtk.Builder()
        eventHandler = EventHandler(builder)
        builder.add_from_file("view/remote.glade")
        builder.connect_signals(eventHandler)

        window = builder.get_object("windowSetup")
        window.connect("delete-event", Gtk.main_quit)
        window.show()

        Gtk.main()