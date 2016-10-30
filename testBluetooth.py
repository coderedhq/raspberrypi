import commands

all_devices = commands.getstatusoutput("sudo bluetoothctl")
print(all_devices)