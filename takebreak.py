import os
import sys


default = "Take a 20 second break - look at least 20 feet away!"
message = sys.argv[1] if len(sys.argv) > 1 else default

def sendmessage(message):
    os.system('notify-send "Take a break!" "'+message+'"')
    return

sendmessage(message)
