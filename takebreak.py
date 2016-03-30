import subprocess
import sys

default = "Take a 20 second break - look at least 20 feet away!"
message = sys.argv[1] if len(sys.argv) > 1 else default

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

sendmessage(message)
