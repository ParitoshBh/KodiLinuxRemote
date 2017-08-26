from kodi import Kodi
from settings import Settings
from remote import Remote
from setup import Setup

settings = Settings()

# attempt to load user defined settings
user_defined = settings.GetSettings()

if user_defined is not None:
    # self.kodi = Kodi(username, password, '', '')
    # self.kodi.Connect()
    # self.LoadRemote()
    remoteWin = Remote(user_defined)
    remoteWin.load_window()
else:
    # self.LoadSetupInterface()
    setupWin = Setup()
    setupWin.load_window()

# class RemoteWindow:
#     kodi = None

#     def test(self):
#         # Gtk.Window.__init__(self, title="Kodi Linux Remote")

#         settings = Settings()
#         # attempt to load user defined settings
#         user_defined = settings.GetSettings()
#         if user_defined is not None:
#             username = user_defined['username']
#             password = user_defined['password']
#             self.kodi = Kodi(username, password, '', '')
#             self.kodi.Connect()
#             self.LoadRemote()
#         else:
#             self.LoadSetupInterface()

#     def LoadSetupInterface(self):
#         grid = Gtk.Grid()
#         self.add(grid)

#         label_IPAddress = Gtk.Label("IP Address", margin=15)
#         label_PortNumber = Gtk.Label("Port Number", margin=15)

#         self.entry_IPAddress = Gtk.Entry()
#         self.entry_PortNumber = Gtk.Entry()

#         button_Connect = Gtk.Button(label="Connect")
#         button_Connect.connect("clicked", self.on_connect_clicked)

#         grid.add(label_IPAddress)

#         # grid.attach(child, left, top, width, height)
#         grid.attach(self.entry_IPAddress, 1, 0, 1, 1)
#         grid.attach(label_PortNumber, 0, 1, 1, 1)
#         grid.attach(self.entry_PortNumber, 1, 1, 1, 1)
#         grid.attach(button_Connect, 0, 2, 2, 1)

#     def on_connect_clicked(self, widget):
#         ip_address = self.entry_IPAddress.get_text()
#         port_number = self.entry_PortNumber.get_text()
#         # print(notes_file_path)
#         kodi = Kodi('kodi', 'kodi', ip_address, port_number)
#         kodi.Connect()

#     def LoadRemote(self):
#         # hbox = Gtk.Box(spacing=6)
#         # self.add(hbox)

#         # button_play = Gtk.Button(label="Play")
#         # button_play.connect("clicked", self.on_control_clicked)
#         # hbox.pack_start(button_play, True, True, 0)

#         # button_vol_inc = Gtk.Button(label="Volume Increase")
#         # button_vol_inc.connect("clicked", self.on_control_clicked)
#         # hbox.pack_start(button_vol_inc, True, True, 0)

#         # button_vol_dec = Gtk.Button(label="Volume Decrease")
#         # button_vol_dec.connect("clicked", self.on_control_clicked)
#         # hbox.pack_start(button_vol_dec, True, True, 0)
#         pass


#     def on_control_clicked(self, widget):
#         label = widget.get_label()
#         if label == 'Play':
#             self.kodi.PlayPause()
#             widget.set_label("Pause")
#         if label == 'Pause':
#             self.kodi.PlayPause()
#             widget.set_label("Play")
#         if label == 'Volume Increase':
#             self.kodi.SetVolume("increase")
#         if label == "Volume Decrease":
#             self.kodi.SetVolume("decrease")


# class Handler:
#     builder = None

#     def __init__(self, obj):
#         self.builder = obj

#     def onButtonClicked(self, button):
#         # self.builder.add_from_file("view/remote.glade")
#         builder.get_object("window2").hide()
#         win = builder.get_object("window3")
#         win.connect("delete-event", Gtk.main_quit)
#         win.show()
#         # window.hide()
#         print("Hello World!")