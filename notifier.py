import threading
import time

class Notifier(threading.Thread):
   def __init__(self, kodi, labelStatus):
      threading.Thread.__init__(self)
      self.kodi = kodi
      self.labelStatus = labelStatus

   def run(self):
      query_kodi(5, self.kodi, self.labelStatus)

def query_kodi(delay, kodi, labelStatus):
   while True:
      time.sleep(delay)
      currentPlaying = kodi.Handshake()
      labelStatus.set_text(currentPlaying)