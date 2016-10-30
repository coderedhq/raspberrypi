import os
import time

while True:
    os.system("sudo bluetoothctl")
    os.system("scan on")
    time.sleep(20)
    os.system("scan off")
    os.system("devices > file.txt")