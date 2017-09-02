import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from settings import Settings
from remote import Remote
from setup import Setup
from eventhandler import EventHandler

builder = Gtk.Builder()
handler = EventHandler(builder)
builder.add_from_file("view/remote.glade")
builder.connect_signals(handler)

settings = Settings()

# attempt to load user defined settings
user_defined = settings.GetSettings()

if user_defined is not None:
    remoteWin = Remote(user_defined)
    kodi = remoteWin.load_window(builder)
    handler.initKodiObj(kodi)
else:
    setupWin = Setup()
    setupWin.load_window(builder)

Gtk.main()