import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from remote import Remote
from eventhandler import EventHandler


class Setup:
    def load_window(self, builder):
        window = builder.get_object("windowSetup")
        window.show()