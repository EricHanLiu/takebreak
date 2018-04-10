import os
import sys


message = "Take a 20 second break - look at least 20 feet away!"

def sendmessage(message):
    os.system('notify-send "Take a break!" "'+message+'"')
    return

sendmessage(message)
