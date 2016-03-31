import pynotify
import time
import threading

def send():
    threading.Timer(1200, send).start()
    pynotify.init("Hey!")
    n = pynotify.Notification("Hey!", "Take a 20 second break!")
    n.show()
    return 

send()


